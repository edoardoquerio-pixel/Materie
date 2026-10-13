import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import io
from contextlib import redirect_stdout

spec = importlib.util.spec_from_file_location('fad', Path(__file__).resolve().parents[1] / 'download_fad.py')
fad = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fad)

class Response:
    def __init__(self, data=b'abc', headers=None, status=200):
        self.data = data
        self.headers = headers or {'Content-Type': 'application/pdf'}
        self.status_code = status
        self.url = 'https://example.test/file.pdf'
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def raise_for_status(self): pass
    def iter_content(self, size): yield self.data

class Session:
    def __init__(self, response): self.response = response; self.headers = None
    def get(self, url, **kwargs): self.headers = kwargs.get('headers'); return self.response

class Tests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name).resolve()
        self.state = fad.DownloadState(self.root / 'state.json', self.root)
    def tearDown(self): self.temp.cleanup()
    def test_mapping(self):
        self.assertEqual(fad.map_course('Corso Python', {'Corso Python':'Python'}), 'Python')
        self.assertEqual(fad.map_course('REST APIs', {'rest':'REST'}), 'REST')
        self.assertTrue(fad.map_course('Forest', {'rest':'REST'}).startswith('ZZ_'))
        self.assertEqual(fad.map_course('Anything', {'id:12':'Exact'},12),'Exact')
    def test_paths(self):
        for name in ('../escape','C:\\outside','/absolute','a/../../b'):
            with self.assertRaises(fad.FadError): fad.safe_path(self.root,name)
        self.assertEqual(fad.sanitize_filename('CON.txt'),'_CON.txt')
        self.assertEqual(fad.sanitize_filename('x. '),'x')
    def test_cd(self):
        self.assertEqual(fad.extract_filename_from_cd({'Content-Disposition':"attachment; filename*=iso-8859-1''caf%E9.pdf"},'fallback'),'café.pdf')
        self.assertEqual(fad.extract_filename_from_cd({'Content-Disposition':'attachment; filename="literal%20.pdf"'},'fallback'),'literal%20.pdf')
    def test_small_file_and_missing_file(self):
        p = self.root/'x.pdf'
        fad.download_file(Session(Response()),'https://example.test/x',p,self.state)
        identity = f'{p.parent.resolve().relative_to(self.root)}:https://example.test/x'
        self.assertTrue(self.state.valid(identity))
        p.unlink()
        self.assertFalse(self.state.valid(identity))
        fad.download_file(Session(Response()),'https://example.test/x',p,self.state)
        self.assertTrue(p.exists())
    def test_collision_and_force(self):
        p=self.root/'x.pdf'
        fad.download_file(Session(Response(b'first')),'https://example.test/a',p,self.state)
        other=fad.download_file(Session(Response(b'second')),'https://example.test/b',p,self.state,True)
        self.assertNotEqual(p,other)
        self.assertEqual(p.read_bytes(),b'first')
    def test_html_rejected(self):
        with self.assertRaises(fad.FadError):
            fad.download_file(Session(Response(b'<html>login</html>',{'Content-Type':'text/html'})), 'https://example.test/a',self.root/'x.pdf',self.state)
        self.assertFalse((self.root/'x.pdf').exists())
        self.assertFalse(self.state.downloaded)
    def test_failed_transfer_preserves_existing(self):
        p=self.root/'x.pdf'
        fad.download_file(Session(Response(b'original')),'https://example.test/a',p,self.state)
        with self.assertRaises(fad.FadError):
            fad.download_file(Session(Response(b'partial')),'https://example.test/a',p,self.state,True,expected_size=200)
        self.assertEqual(p.read_bytes(),b'original')
    def test_conditional(self):
        p=self.root/'x.pdf'
        fad.download_file(Session(Response(headers={'ETag':'test'})),'https://example.test/a',p,self.state)
        session=Session(Response(status=304))
        fad.download_file(session,'https://example.test/a',p,self.state)
        self.assertEqual(session.headers,{'If-None-Match':'test'})
        self.assertEqual(self.state.stats['presenti'],1)
    def test_state_integrity_and_reload(self):
        p=self.root/'x.pdf'
        fad.download_file(Session(Response()),'https://example.test/a',p,self.state)
        loaded=fad.DownloadState(self.root/'state.json',self.root)
        key=f'{p.parent.resolve().relative_to(self.root)}:https://example.test/a'
        self.assertTrue(loaded.valid(key))
        p.write_bytes(b'xyz')
        self.assertFalse(loaded.valid(key))
    def test_lock(self):
        with fad.run_lock(self.root/'lock'):
            with self.assertRaises(fad.FadError):
                with fad.run_lock(self.root/'lock'): pass
        self.assertFalse((self.root/'lock').exists())
    def test_show_mapping(self):
        output=io.StringIO()
        with patch.object(fad,'get_mapping',return_value={'one':'One','two':'Two'}),redirect_stdout(output):
            self.assertEqual(fad.main(['--show-mapping']),0)
        self.assertIn('one',output.getvalue())
        self.assertIn('two',output.getvalue())
    def test_url(self):
        self.assertEqual(fad.canonical_url('https://example.test/a?x=1&token=secret&z=2'), 'https://example.test/a?x=1&z=2')
    def test_discovery_html_dispatch(self):
        soup=fad.BeautifulSoup('<a href="/mod/page/view.php?other=1&id=2">Page</a><a href="/mod/folder/view.php?id=3">Folder</a>','html.parser')
        with patch.object(fad,'call_ajax',return_value=None),patch.object(fad,'html_soup',return_value=(soup,fad.BASE_URL)):
            acts=fad.get_course_resources(None,{'id':1,'url':fad.BASE_URL})
        self.assertEqual(len(acts),2)
        self.assertNotIn('download_url',acts[0])
        self.assertNotIn('download_url',acts[1])

    def test_html_export_updates_and_assets(self):
        act={'id':2,'type':'page','url':fad.BASE_URL+'/mod/page/view.php?id=2','name':'Page'}
        directory=self.root/'page'
        soup=fad.BeautifulSoup('<div class="resourcecontent"><p>Hello</p><img src="/pluginfile.php/1/mod_page/content/0/photo.png"></div>','html.parser')
        with patch.object(fad,'html_soup',return_value=(soup,act['url'])):
            fad.export_html(Session(Response(b'image',{'Content-Type':'image/png'})),act,directory,self.state,False)
        html=(directory/'index.html').read_text(encoding='utf-8')
        self.assertIn('Hello',html)
        self.assertIn('assets/',html)
        self.assertEqual(len(list((directory/'assets').iterdir())),1)
        soup=fad.BeautifulSoup('<div class="resourcecontent"><p>Updated</p></div>','html.parser')
        with patch.object(fad,'html_soup',return_value=(soup,act['url'])):
            fad.export_html(None,act,directory,self.state,False)
        self.assertIn('Updated',(directory/'index.html').read_text(encoding='utf-8'))
    def test_pagination(self):
        batch=[{'id':i,'fullname':str(i)} for i in range(1,101)]
        empty=fad.BeautifulSoup('','html.parser')
        with patch.object(fad,'call_ajax',side_effect=[{'courses':batch},{'courses':[{'id':101,'fullname':'last'}]}]) as ajax,patch.object(fad,'html_soup',return_value=(empty,fad.DASHBOARD_URL)):
            self.assertEqual(len(fad.get_enrolled_courses(None)),101)
        self.assertEqual(ajax.call_args_list[1].args[2]['offset'],100)
    def test_folder_paths(self):
        self.assertEqual(fad.folder_relative('https://example.test/pluginfile.php/12/mod_folder/content/0/sub/deep/a.pdf'),'sub/deep')
    def test_corrupt_state(self):
        (self.root/'state.json').write_text('{"version":2,"downloaded":{"bad":{"size":3,"sha256":null}}}')
        with self.assertRaises(fad.FadError): fad.DownloadState(self.root/'state.json',self.root)

    def test_download_reuses_stream_hash(self):
        with patch.object(fad, 'file_hash', side_effect=AssertionError('Unexpected disk hash')):
            fad.download_file(Session(Response()), 'https://example.test/a', self.root/'x.pdf', self.state)
        self.assertEqual(len(self.state.owned_paths), 1)

    def test_direct_activity_uses_one_request(self):
        session=Session(Response())
        with patch.object(session, 'get', wraps=session.get) as get:
            fad.download_activity(session, {'id':1, 'type':'resource', 'name':'PDF',
                'url':'https://example.test/mod/resource/view.php?id=1'}, self.root, self.state)
        self.assertEqual(get.call_count, 1)
        self.assertEqual(self.state.stats['scaricati'], 1)

    def test_force_skips_old_integrity_scan(self):
        p=self.root/'x.pdf'
        fad.download_file(Session(Response()), 'https://example.test/a', p, self.state)
        with patch.object(self.state, 'valid', side_effect=AssertionError('Unexpected scan')):
            fad.download_file(Session(Response(b'updated')), 'https://example.test/a', p, self.state, True)
        self.assertEqual(p.read_bytes(), b'updated')

if __name__=='__main__': unittest.main()
