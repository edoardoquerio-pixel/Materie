import { DatabaseSync } from 'node:sqlite';
import fs from 'fs';
import path from 'path';

const DB = 'C:/Users/edoardo.querio/.zara/memory.db';
const REPO = 'C:/Users/edoardo.querio/OneDrive - ITS ICT Piemonte/Desktop/Materie';

const db = new DatabaseSync(DB);

function store(key, value, type = 'fact', source = 'observed', scope = 'materie') {
  const now = new Date().toISOString().split('T')[0];
  try {
    db.prepare(`
      INSERT INTO semantic (key, value, confidence, source, type, scope, created, updated, reinforced, decay_score)
      VALUES (?, ?, 1.0, ?, ?, ?, ?, ?, 1, 1.0)
      ON CONFLICT(key) DO UPDATE SET
        value = excluded.value, updated = excluded.updated, reinforced = reinforced + 1, decay_score = 1.0
    `).run(key, value, source, type, scope, now, now);
    return true;
  } catch {
    return false;
  }
}

let total = 0;

// === 1. INGEST NOTE COMPLETE ===
console.log('=== Scanning Note Complete files ===');
const noteFiles = [];
const dirs = fs.readdirSync(REPO).filter(d => /^\d{2}_/.test(d) && fs.statSync(path.join(REPO, d)).isDirectory());

for (const dir of dirs) {
  const noteComplete = path.join(REPO, dir, '00_Note_COMPLETE.md');
  const noteStruct = path.join(REPO, dir, '00_Note_STRUTTURATE.md');
  const readme = path.join(REPO, dir, 'README.md');
  
  if (fs.existsSync(noteComplete)) {
    const content = fs.readFileSync(noteComplete, 'utf-8').substring(0, 8000);
    const subjectName = dir.replace(/^\d{2}_/, '').replace(/_/g, ' ');
    store(`materie:${dir}:note_complete`, content, 'fact', 'observed', 'materie');
    store(`materie:${dir}:nome`, subjectName, 'fact', 'observed', 'materie');
    total++;
    console.log(`  ✓ ${dir} (note complete)`);
  }
  if (fs.existsSync(noteStruct)) {
    const content = fs.readFileSync(noteStruct, 'utf-8').substring(0, 8000);
    store(`materie:${dir}:note_strutturate`, content, 'fact', 'observed', 'materie');
    total++;
    console.log(`  ✓ ${dir} (note strutturate)`);
  }
  if (fs.existsSync(readme)) {
    const content = fs.readFileSync(readme, 'utf-8').substring(0, 4000);
    store(`materie:${dir}:readme`, content, 'fact', 'observed', 'materie');
    total++;
    console.log(`  ✓ ${dir} (readme)`);
  }

  // List materials and projects
  const matDir = path.join(REPO, dir, '01_Materiale');
  const projDir = path.join(REPO, dir, '03_Progetti');
  const esercDir = path.join(REPO, dir, '02_Esercizi');

  if (fs.existsSync(matDir)) {
    const files = fs.readdirSync(matDir).filter(f => !f.startsWith('.'));
    store(`materie:${dir}:materiali`, files.join(', '), 'fact', 'observed', 'materie');
  }
  if (fs.existsSync(projDir)) {
    const files = fs.readdirSync(projDir).filter(f => !f.startsWith('.'));
    store(`materie:${dir}:progetti`, files.join(', '), 'fact', 'observed', 'materie');
  }
  if (fs.existsSync(esercDir)) {
    const files = fs.readdirSync(esercDir).filter(f => !f.startsWith('.'));
    store(`materie:${dir}:esercizi`, files.join(', '), 'fact', 'observed', 'materie');
  }
}

// === 2. INGEST PROJECT WORK TP GROUP ===
console.log('\n=== Scanning Project Work ===');
const tpGroup = path.join(REPO, '23_Project_Work_e_Laboratori', '03_Progetti');
function scanProjects(dir, prefix) {
  if (!fs.existsSync(dir)) return;
  for (const f of fs.readdirSync(dir)) {
    const fp = path.join(dir, f);
    if (fs.statSync(fp).isFile() && !f.startsWith('.') && (f.endsWith('.md') || f.endsWith('.json') || f.endsWith('.yaml') || f.endsWith('.yml'))) {
      const content = fs.readFileSync(fp, 'utf-8').substring(0, 5000);
      const name = `${prefix}:${f.replace(/\.(md|json|yaml|yml)$/, '')}`;
      store(`project:${name}`, content, 'architecture', 'observed', 'project-work');
      total++;
    }
  }
}
function scanProjectsRecursive(dir, prefix) {
  if (!fs.existsSync(dir)) return;
  for (const f of fs.readdirSync(dir)) {
    const fp = path.join(dir, f);
    if (fs.statSync(fp).isDirectory() && !f.startsWith('.') && !f.startsWith('node_modules')) {
      scanProjects(fp, `${prefix}:${f}`);
      scanProjectsRecursive(fp, `${prefix}:${f}`);
    }
  }
}
scanProjectsRecursive(tpGroup, 'tp_group');

// === 3. INGEST AGENTS AND PROMPTS ===
console.log('\n=== Scanning Agents and Prompts ===');
const agentsDir = path.join(REPO, '.github', 'agents');
if (fs.existsSync(agentsDir)) {
  for (const f of fs.readdirSync(agentsDir)) {
    const ap = path.join(agentsDir, f);
    if (fs.statSync(ap).isFile() && (f.endsWith('.agent.md') || f.endsWith('.md'))) {
      const content = fs.readFileSync(path.join(agentsDir, f), 'utf-8').substring(0, 5000);
      store(`agents:${f.replace(/\.(agent\.)?md$/, '')}`, content, 'workflow', 'observed', 'agents');
      total++;
    }
  }
}

const promptsDir = path.join(REPO, '.github', 'prompts');
if (fs.existsSync(promptsDir)) {
  for (const f of fs.readdirSync(promptsDir)) {
    const pp = path.join(promptsDir, f);
    if (fs.statSync(pp).isFile() && (f.endsWith('.prompt.md') || f.endsWith('.md'))) {
      const content = fs.readFileSync(path.join(promptsDir, f), 'utf-8').substring(0, 5000);
      store(`prompts:${f.replace(/\.(prompt\.)?md$/, '')}`, content, 'workflow', 'observed', 'prompts');
      total++;
    }
  }
}

// === 4. INGEST USEFUL CODE FILES ===
console.log('\n=== Scanning key code files ===');
const codeDirs = [
  ['10_Programmazione_Python', 'Python'],
  ['09_Programmazione_C_CPP', 'C_CPP'],
  ['11_Programmazione_DotNet_CSharp', 'DotNet'],
  ['12_RESTful_API', 'REST_API'],
  ['16_Linux_Server_e_Amministrazione', 'Linux'],
];

for (const [dir, prefix] of codeDirs) {
  const projDir = path.join(REPO, dir, '03_Progetti');
  if (fs.existsSync(projDir)) {
    for (const proj of fs.readdirSync(projDir)) {
      const projPath = path.join(projDir, proj);
      if (fs.statSync(projPath).isDirectory()) {
        const allFiles = fs.readdirSync(projPath);
        const files = allFiles.filter(f => {
          const fp = path.join(projPath, f);
          return fs.statSync(fp).isFile() && (f.endsWith('.py') || f.endsWith('.cs') || f.endsWith('.js') || f.endsWith('.c') || f.endsWith('.cpp'));
        });
        if (files.length) {
          store(`codice:${prefix}:${proj}`, `Progetto ${proj}: ${files.join(', ')}`, 'fact', 'observed', 'codice');
          total++;
          // Read first 2000 chars of each source file
          for (const f of files.slice(0, 3)) {
            const src = fs.readFileSync(path.join(projPath, f), 'utf-8').substring(0, 2000);
            store(`codice:${prefix}:${proj}:${f.replace(/\.\w+$/, '')}`, src, 'architecture', 'observed', 'codice');
            total++;
          }
        }
      }
    }
  }
}

console.log(`\n=== Done! Ingested ${total} items ===`);
