import { DatabaseSync } from 'node:sqlite';
import fs from 'fs';
import path from 'path';

const VAULT = 'C:/Users/edoardo.querio/Obsidian_Vault';
const MEMORY_DIR = path.join(VAULT, 'Zara Memory');
const DB = 'C:/Users/edoardo.querio/.zara/memory.db';

fs.mkdirSync(MEMORY_DIR, { recursive: true });

// Clean previous export
for (const f of fs.readdirSync(MEMORY_DIR)) {
  if (f.endsWith('.md')) fs.unlinkSync(path.join(MEMORY_DIR, f));
}

const db = new DatabaseSync(DB);
const rows = db.prepare("SELECT key, value, type, source, reinforced, confidence, scope, created, updated FROM semantic WHERE value != '' ORDER BY type, key").all();

// ── Helpers ──
const safeName = (key) => key.includes(':')
  ? key.split(':').pop().replace(/[/\\:?<>|*"]/g, '_').substring(0, 50)
  : key.replace(/[/\\?<>|*"]/g, '_').substring(0, 50);

const safeFile = (name) => name.replace(/[/\\:?<>|*"]/g, '_').substring(0, 80) + '.md';

const sourceEmoji = (src) => ({ user_explicit: '🧑', observed: '👁', inferred: '🤖', api_external_unverified: '🌐' }[src] || '📄');

const typeEmoji = (t) => ({ fact: '📌', policy: '⚖️', workflow: '⚙️', architecture: '🏗️', decision: '✅', pitfall: '⚠️', preference: '⭐' }[t] || '📄');

// Build lookup maps
const keyToName = {};
const keyToFile = {};
const keyToRow = {};
for (const r of rows) {
  const n = safeName(r.key);
  keyToName[r.key] = n;
  keyToFile[r.key] = safeFile(n);
  keyToRow[r.key] = r;
}

const filesWritten = new Set();

// ── Enhanced relatedness scorer ──
const TOPIC_KEYWORDS = {
  docker: ['docker', 'container', 'compose', 'dockerfile', 'immagine'],
  kubernetes: ['kubernetes', 'k8s', 'kubectl', 'pod', 'deployment', 'service'],
  azure: ['azure', 'entra', 'function', 'blob', 'cosmos', 'vnet'],
  aws: ['aws', 'ec2', 's3', 'lambda', 'eks'],
  gcp: ['gcp', 'google', 'gke', 'cloud function'],
  python: ['python', 'flask', 'django', 'pandas', 'jupyter'],
  csharp: ['csharp', 'c#', '.net', 'dotnet', 'asp.net', 'linq', 'async'],
  sql: ['sql', 'database', 'nosql', 'sqlite', 'sql server'],
  git: ['git', 'version control', 'github'],
  linux: ['linux', 'bash', 'shell', 'server'],
  progetto: ['project work', 'tp_group', 'thema', 'pro studio'],
  rete: ['rete', 'network', 'sicurezza', 'firewall', 'vpn'],
};

function extractTags(key, value, type, scope) {
  const tags = new Set();
  tags.add(type);
  tags.add(scope || 'general');
  const lower = (key + ' ' + value).toLowerCase();
  for (const [topic, kws] of Object.entries(TOPIC_KEYWORDS)) {
    for (const kw of kws) {
      if (lower.includes(kw)) { tags.add(topic); break; }
    }
  }
  // Extract subject code from materie keys
  const m = key.match(/materie:(\d+_\w+)/);
  if (m) tags.add('materie-' + m[1].toLowerCase());
  return [...tags].sort();
}

function computeRelated(key, value) {
  const parts = key.split(':');
  const scores = [];
  const lower = (key + ' ' + value).toLowerCase();
  const tags = extractTags(key, value, rows.find(r => r.key === key)?.type, rows.find(r => r.key === key)?.scope);

  for (const r of rows) {
    if (r.key === key) continue;
    let score = 0;

    // Same first prefix = +3
    if (r.key.startsWith(parts[0] + ':')) score += 3;

    // Same scope = +2
    if (r.scope && rows.find(x => x.key === key)?.scope === r.scope) score += 2;

    // Same type = +1
    if (r.type === rows.find(x => x.key === key)?.type) score += 1;

    // Shared topic tags = +2 per match
    const otherTags = extractTags(r.key, r.value, r.type, r.scope);
    for (const t of tags) {
      if (otherTags.includes(t)) score += 2;
    }

    // Cross-topic: docker ↔ kubernetes, azure ↔ aws ↔ gcp = +4
    const isCloud = (k) => /azure|aws|gcp/.test(k);
    const isContainer = (k) => /docker|kubernetes/.test(k);
    if ((isCloud(key) && isCloud(r.key)) || (isContainer(key) && isContainer(r.key))) score += 4;

    // Strong keyword co-occurrence in value = +3
    const sharedWords = new Set(lower.split(/\W+/).filter(w => w.length > 3));
    const rWords = new Set(r.value.toLowerCase().split(/\W+/).filter(w => w.length > 3));
    let matches = 0;
    for (const w of sharedWords) if (rWords.has(w)) matches++;
    score += Math.min(matches, 5);

    if (score > 0) scores.push({ key: r.key, score });
  }

  return scores.sort((a, b) => b.score - a.score).slice(0, 8);
}

function buildBacklinks(key) {
  const links = [];
  const normalVal = (key + ' ' + (keyToRow[key]?.value || '')).toLowerCase();
  for (const r of rows) {
    if (r.key === key) continue;
    const refStr = (r.key + ' ' + r.value).toLowerCase();
    if (refStr.includes(keyToName[key].toLowerCase())) {
      links.push(r.key);
    } else if (key.split(':').length > 1) {
      const subject = key.split(':')[1]?.toLowerCase();
      if (subject && refStr.includes(subject)) links.push(r.key);
    }
  }
  return [...new Set(links)].slice(0, 6);
}

// ── Build a topic tag → keys map for MOC notes ──
const topicToKeys = {};
for (const r of rows) {
  const tags = extractTags(r.key, r.value, r.type, r.scope);
  for (const t of tags) {
    if (!topicToKeys[t]) topicToKeys[t] = [];
    topicToKeys[t].push(r.key);
  }
}

// ── Write each memory file ──
let total = 0;
for (const r of rows) {
  const name = safeName(r.key);
  const file = safeFile(name);
  const related = computeRelated(r.key, r.value);
  const backlinks = buildBacklinks(r.key);
  const tags = extractTags(r.key, r.value, r.type, r.scope);
  const shortVal = r.value.replace(/"/g, "'").substring(0, 120);

  const relatedLinks = related.map(item => {
    const n = keyToName[item.key];
    return `- [[${n}|${n}]] (score: ${item.score})`;
  }).join('\n');

  const backlinksStr = backlinks.map(k => {
    const n = keyToName[k];
    return `- [[${n}|${n}]]`;
  }).join('\n');

  const content = `---
memory_key: "${r.key}"
type: ${r.type}
source: ${r.source}
reinforced: ${r.reinforced}
confidence: ${r.confidence}
scope: "${r.scope || ''}"
created: ${r.created || ''}
updated: ${r.updated || ''}
tags: [${tags.map(t => t.toLowerCase().replace(/\s+/g, '-')).join(', ')}]
aliases: [${name}]
---

# ${sourceEmoji(r.source)} ${typeEmoji(r.type)} ${name}

> **Key:** \`${r.key}\` · **Type:** \`${r.type}\` · **Reinforced:** ${r.reinforced}x · **Confidence:** ${r.confidence}

---

${r.value}

---

${relatedLinks ? '### 🔗 Related\n\n' + relatedLinks + '\n\n---\n' : ''}
${backlinksStr ? '### 🔙 Backlinks\n\n' + backlinksStr + '\n\n---\n' : ''}

*Memory created: ${r.created || 'N/A'} · Last updated: ${r.updated || 'N/A'}*
`;

  fs.writeFileSync(path.join(MEMORY_DIR, file), content);
  filesWritten.add(file);
  total++;
}

// ── Generate MOC (Map of Content) hub notes ──
const MOC_THEMES = {
  'Docker': ['docker', 'container', '17_container'],
  'Kubernetes': ['kubernetes', 'k8s', 'pod'],
  'Azure': ['azure', 'materie-14_cloud_azure'],
  'AWS': ['aws', 'materie-13_cloud_aws'],
  'GCP': ['gcp', 'materie-15_cloud_gcp'],
  'Python': ['python', 'materie-10_programmazione_python', 'codice:Python'],
  'C# .NET': ['csharp', 'materie-11_programmazione_dotnet_csharp', 'codice:DotNet'],
  'SQL & Database': ['sql', 'materie-08_basi_di_dati_sql_nosql'],
  'Git & Version Control': ['git', 'materie-07_version_control_git'],
  'Linux': ['linux', 'materie-16_linux_server_e_amministrazione'],
  'REST API': ['api', 'materie-12_restful_api', 'codice:REST_API'],
  'C/C++': ['c_cpp', 'materie-09_programmazione_c_cpp', 'codice:C_CPP'],
  'Reti & Sicurezza': ['rete', 'sicurezza', 'materie-06_reti_e_sicurezza_informatica'],
  'Project Work TP_Group': ['progetto', 'tp_group', 'project-work'],
  'Cloud (Generale)': ['cloud', 'aws', 'azure', 'gcp'],
  'Web Research': ['web-research'],
  'Agenti & Prompt': ['agents', 'prompts', 'agente'],
};

for (const [theme, searchTags] of Object.entries(MOC_THEMES)) {
  const matched = [];
  for (const r of rows) {
    const tags = extractTags(r.key, r.value, r.type, r.scope);
    const keyLower = r.key.toLowerCase();
    const valLower = r.value.toLowerCase();
    for (const st of searchTags) {
      if (tags.includes(st) || keyLower.includes(st) || valLower.includes(st)) {
        matched.push(r);
        break;
      }
    }
  }
  if (matched.length < 2) continue;

  const file = safeFile(`MOC ${theme}`);
  let content = `# 🗺️ ${theme} — Map of Content\n\n`;
  content += `This MOC groups **${matched.length}** related memory nodes.\n\n---\n\n`;

  // Group by sub-topic
  const subgroups = {};
  for (const r of matched) {
    const sub = r.key.includes(':') ? r.key.split(':')[0] : 'general';
    if (!subgroups[sub]) subgroups[sub] = [];
    subgroups[sub].push(r);
  }

  for (const [sub, items] of Object.entries(subgroups)) {
    const emoji = { materie: '📚', web: '🌐', codice: '💻', project: '📋', agents: '🤖', prompts: '📝', agents_workspace: '🤖' }[sub] || '📄';
    content += `### ${emoji} ${sub.toUpperCase()} (${items.length})\n\n`;
    for (const r of items) {
      const name = keyToName[r.key];
      const val = r.value.substring(0, 80).replace(/\n/g, ' ');
      content += `- [[${name}|${name}]] — ${val}...\n`;
    }
    content += '\n';
  }

  content += `---\n*MOC auto-generated on ${new Date().toISOString()}*\n`;
  fs.writeFileSync(path.join(MEMORY_DIR, file), content);
  filesWritten.add(file);
  total++;
  console.log(`  MOC: ${theme} (${matched.length} items)`);
}

// ── Generate enhanced index ──
const byType = {};
for (const r of rows) {
  if (!byType[r.type]) byType[r.type] = [];
  byType[r.type].push(r);
}

let index = `# 🧠 Zara Memory Index\n\n**Total:** ${rows.length} memories\n\n`;

// Quick links to MOCs
index += `## 🗺️ Maps of Content\n\n`;
for (const theme of Object.keys(MOC_THEMES)) {
  index += `- [[Zara Memory/${safeFile(`MOC ${theme}`)}|${theme}]]\n`;
}
index += '\n---\n\n';

// Stats
index += `## 📊 Memory Stats\n\n`;
index += `| Type | Count |\n|------|-------|\n`;
for (const [type, items] of Object.entries(byType).sort((a, b) => b[1].length - a[1].length)) {
  const emoji = typeEmoji(type);
  index += `| ${emoji} ${type} | ${items.length} |\n`;
}
index += '\n---\n\n';

// By type
for (const [type, items] of Object.entries(byType).sort((a, b) => b[1].length - a[1].length)) {
  const emoji = typeEmoji(type);
  index += `## ${emoji} ${type.toUpperCase()} (${items.length})\n\n`;
  for (const r of items) {
    const name = keyToName[r.key];
    const srcBadge = sourceEmoji(r.source);
    const val = r.value.substring(0, 80).replace(/\n/g, ' ');
    index += `- [[Zara Memory/${safeFile(name)}|${name}]] ${srcBadge} — ${val}...\n`;
  }
  index += '\n';
}

index += `\n---\n*Generated from Zara SQLite memory database · ${new Date().toISOString()}*\n`;
fs.writeFileSync(path.join(VAULT, 'Zara Memory Index.md'), index);

console.log(`\n=== Done! Exported ${rows.length} memories + ${Object.keys(MOC_THEMES).length} MOC notes to ${MEMORY_DIR} ===`);
