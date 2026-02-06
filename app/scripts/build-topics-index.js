/**
 * Scans the glossary directory (parent of app/) for category folders and
 * markdown topic files. Writes src/data/topics.json for navigation.
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const APP_DIR = path.join(__dirname, '..');
const GLOSSARY_ROOT = path.join(APP_DIR, '..');

const ROOT_MD_SKIP = new Set(['README.md', 'INDEX.md', 'TOPICS.md', 'TEMPLATE.md', 'GENERATION_GUIDE.md']);

const CATEGORY_LABELS = {
  'architecture': 'Architecture & Design Patterns',
  'ingestion': 'Data Ingestion',
  'storage': 'Data Storage',
  'databases': 'Database Types & Technologies',
  'transformation': 'Data Transformation',
  'modeling': 'Data Modeling',
  'patterns': 'Integration Patterns',
  'quality': 'Data Quality & Validation',
  'orchestration': 'Data Orchestration',
  'formats': 'Data Formats & Serialization',
  'governance': 'Data Governance',
  'observability': 'Data Observability',
  'advanced': 'Advanced Concepts',
  'ai-ml': 'AI & Machine Learning',
  'conversational-analytics': 'Conversational Analytics',
  'analytics': 'Analytics & Business Intelligence',
  'cross-cutting': 'Cross-Cutting Topics',
};

function getTitleFromFile(filePath) {
  try {
    const raw = fs.readFileSync(filePath, 'utf-8');
    const firstLine = raw.split('\n')[0] || '';
    const match = firstLine.match(/^#\s+(.+)$/);
    return match ? match[1].trim() : path.basename(filePath, '.md');
  } catch {
    return path.basename(filePath, '.md');
  }
}

function slugFromFilename(name) {
  return name.replace(/\.md$/, '');
}

function buildIndex() {
  const categories = [];
  const entries = fs.readdirSync(GLOSSARY_ROOT, { withFileTypes: true });
  const dirs = entries.filter((e) => e.isDirectory() && !e.name.startsWith('.'));
  const categoryDirs = dirs.map((d) => d.name).sort();

  for (const cat of categoryDirs) {
    const catPath = path.join(GLOSSARY_ROOT, cat);
    let files = [];
    try {
      files = fs.readdirSync(catPath);
    } catch {
      continue;
    }
    const mdFiles = files
      .filter((f) => f.endsWith('.md') && !ROOT_MD_SKIP.has(f))
      .sort();
    if (mdFiles.length === 0) continue;

    const topics = mdFiles.map((f) => {
      const slug = slugFromFilename(f);
      const fullPath = path.join(catPath, f);
      const title = getTitleFromFile(fullPath);
      return { slug, title };
    });

    categories.push({
      id: cat,
      label: CATEGORY_LABELS[cat] || cat.replace(/-/g, ' '),
      topics,
    });
  }

  const outPath = path.join(APP_DIR, 'src', 'data', 'topics.json');
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, JSON.stringify({ categories }, null, 2), 'utf-8');
  console.log('Wrote', outPath, '—', categories.length, 'categories');

  // Copy topic .md files to public/content/ for "Download as Markdown"
  const contentDir = path.join(APP_DIR, 'public', 'content');
  for (const cat of categories) {
    const destCat = path.join(contentDir, cat.id);
    fs.mkdirSync(destCat, { recursive: true });
    for (const t of cat.topics) {
      const src = path.join(GLOSSARY_ROOT, cat.id, t.slug + '.md');
      const dest = path.join(destCat, t.slug + '.md');
      try {
        fs.copyFileSync(src, dest);
      } catch (e) {
        console.warn('Skip copy', src, e.message);
      }
    }
  }
  console.log('Copied topic markdown to public/content/');
}

buildIndex();
