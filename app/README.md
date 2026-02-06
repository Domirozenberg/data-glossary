# Data Glossary Web App

Web UI for the Data Pipeline Glossary. Browse topics by category, read content, print or save as PDF, and download topics as Markdown.

## Setup

1. **Install dependencies** (from this `app/` directory):

   ```bash
   npm install
   ```

2. **Build the topic index** (scans the parent directory for glossary markdown and copies files for download):

   ```bash
   node scripts/build-topics-index.js
   ```

3. **Run locally**:

   ```bash
   npm run dev
   ```

   Open [http://localhost:4321](http://localhost:4321).

4. **Production build**:

   ```bash
   npm run build
   ```

   Output is in `dist/`. Preview with `npm run preview`.

## Deploy on Vercel

1. Push the repo to GitHub (or connect your Git provider in Vercel).
2. In [Vercel](https://vercel.com), create a new project and import this repository.
3. Set **Root Directory** to `app` so Vercel builds from this folder.
4. Deploy. Vercel will run `npm run build` (which runs the topic index script then Astro build).
5. To protect the site with a password: upgrade to **Vercel Pro** and enable **Password Protection** in the project settings.

## Structure

- `scripts/build-topics-index.js` – Scans `../` for category folders and topic `.md` files; writes `src/data/topics.json` and copies markdown to `public/content/` for “Download as Markdown”.
- `src/pages/` – Home, category list, and topic pages (static routes).
- `src/layouts/Layout.astro` – Sidebar navigation and main layout.
- `src/styles/global.css` – Layout and print styles.

Topic content is read from the parent glossary directory at build time (e.g. `../architecture/data-pipeline-architecture.md`), so the repo root must be the glossary when building.
