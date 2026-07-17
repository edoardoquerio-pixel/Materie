import { DatabaseSync } from 'node:sqlite';
import fs from 'fs';

const db = new DatabaseSync('C:/Users/edoardo.querio/.zara/memory.db');

const rows = db.prepare("SELECT key, value, type, source, reinforced, confidence, scope FROM semantic WHERE value != '' ORDER BY reinforced DESC, confidence DESC").all();

const TYPE_COLORS = { fact: '#90be6d', policy: '#f9c74f', workflow: '#577590', architecture: '#43aa8b', decision: '#f94144', pitfall: '#f8961e', preference: '#277da1' };
const SOURCE_COLORS = { user_explicit: '#ffd700', observed: '#4ecdc4', inferred: '#95e1d3', api_external_unverified: '#ff6b6b' };

let dot = 'digraph ZaraMemory {\n';
dot += '  rankdir=LR;\n';
dot += '  bgcolor="#1a1a2e";\n';
dot += '  node [shape=box, style=filled, fontname="Segoe UI", fontsize=9, fontcolor=white, color=white, penwidth=0.5];\n';
dot += '  edge [color="#555", arrowhead=open, arrowsize=0.4];\n';
dot += '  graph [fontname="Segoe UI", fontcolor=white, label="\\nZara Knowledge Graph\\n363 memories · node size = reinforced count · color = source", labelloc=t, fontsize=16, pad=1];\n';
dot += '  splines=true;\n';
dot += '  overlap=false;\n';
dot += '  ranksep=1.5;\n';
dot += '  nodesep=0.5;\n\n';

// Root node
dot += '  zara_root [label="Zara Memory\\n363 entries", shape=doubleoctagon, fillcolor="#e94560", fontsize=16, fontweight=bold];\n\n';

// Type hub nodes
const typeNames = { fact: 'Facts', policy: 'Policies', workflow: 'Workflows', architecture: 'Architecture', decision: 'Decisions', pitfall: 'Pitfalls', preference: 'Preferences' };

for (const [type, name] of Object.entries(typeNames)) {
  const items = rows.filter(r => r.type === type);
  const color = TYPE_COLORS[type];
  const srcCount = items.length;
  dot += `  hub_${type} [label="${name} (${srcCount})", fillcolor="${color}44", fontsize=13, fontweight=bold, shape=octagon];\n`;
  dot += `  zara_root -> hub_${type} [weight=2, color="${color}88", penwidth=1.5];\n`;

  // Top 15 items per type
  const top = items.slice(0, 15);
  for (const r of top) {
    const shortKey = r.key.replace(/[^a-zA-Z0-9]/g, '_').substring(0, 35);
    const label = r.key.includes(':') ? r.key.split(':').pop().substring(0, 22) : r.key.substring(0, 22);
    const shortVal = r.value.replace(/"/g, "'").replace(/\n/g, ' ').substring(0, 45);
    const size = Math.max(8, Math.min(14, 9 + Math.min(r.reinforced, 5)));
    const srcColor = SOURCE_COLORS[r.source] || '#888';
    dot += `  "${shortKey}" [label="${label}", fillcolor="${srcColor}22", fontsize=${size}, tooltip="${shortVal}"];\n`;
    dot += `  hub_${type} -> "${shortKey}" [weight=1, color="${color}44"];\n`;
  }
}

// Edges between related memories (by topic prefix)
const topicGroups = {};
const nodeKeys = {};
for (const r of rows) {
  const sk = r.key.replace(/[^a-zA-Z0-9]/g, '_').substring(0, 35);
  nodeKeys[sk] = true;
  const parts = r.key.split(/[:.-]/);
  if (parts.length >= 2) {
    const topic = parts[0].toLowerCase();
    if (topic.length > 2 && !['knowledge', 'project', 'workspace', 'materie', 'regola', 'decisione', 'fullcloudazure', 'azure'].includes(topic)) {
      if (!topicGroups[topic]) topicGroups[topic] = [];
      topicGroups[topic].push(sk);
    }
  }
}

// Also add edges from key topic prefixes
for (const r of rows) {
  const sk = r.key.replace(/[^a-zA-Z0-9]/g, '_').substring(0, 35);
  const parts = r.key.split(/[:.-]/);
  if (parts.length >= 2 && parts[0] !== 'knowledge') {
    const topic = parts[0].toLowerCase();
    const hub = `hub_${rows.find(r2 => r2.key.startsWith(topic))?.type || 'fact'}`;
    // Already connected via type hub
  }
}

let edgeCount = 0;
// Connect memories within the same detailed topic (more specific)
for (const [topic, keys] of Object.entries(topicGroups)) {
  if (keys.length >= 2 && keys.length <= 8) {
    for (let i = 0; i < keys.length; i++) {
      for (let j = i+1; j < keys.length; j++) {
        dot += `  "${keys[i]}" -> "${keys[j]}" [style=dotted, color="#666", weight=0.2, arrowhead=none];\n`;
        edgeCount++;
      }
    }
  }
}

// Legend
dot += `
  subgraph cluster_legend {
    label="LEGEND";
    style=filled; fillcolor="#0d1b2a"; fontcolor=white; fontsize=12; color="#555";
    l1 [label=" ● user_explicit", fillcolor="#ffd70022", fontsize=9, shape=point, width=0.01, height=0.01];
    l2 [label=" ● observed", fillcolor="#4ecdc422", fontsize=9, shape=point, width=0.01, height=0.01];
    l3 [label=" ● inferred", fillcolor="#95e1d322", fontsize=9, shape=point, width=0.01, height=0.01];
    l4 [label=" ● external", fillcolor="#ff6b6b22", fontsize=9, shape=point, width=0.01, height=0.01];
  }
`;

dot += '}\n';

fs.writeFileSync('C:/Users/edoardo.querio/OneDrive - ITS ICT Piemonte/Desktop/Materie/zara_knowledge_graph.dot', dot);
console.log(`DOT written. Nodes: ${rows.length + 8}, Edges: ${edgeCount + 7 + 60}`);
