# Browsing the glossary with MkDocs

This project uses **MkDocs** with the **Material** theme so you can browse the Data Pipeline Glossary in a local site with search and navigation.

**Where content lives:** All glossary content is under the **`docs/`** directory (index, Full index, Topic list, and category folders like `architecture/`, `storage/`, etc.). The repo root has the config and scripts only.

## Setup

```bash
pip install -r requirements-docs.txt
# or:  pip3 install -r requirements-docs.txt

# One-time: install the project so the section-index plugin runs on every build (🛠 marks update automatically)
pip install -e .
```

After `pip install -e .`, every `mkdocs serve` or `mkdocs build` will run two scripts automatically: (1) section index update so the 🛠 mark appears for topics with **Products & Tools**, and (2) **Related Topics** linking so plain topic names in each page become clickable links. New and updated topics get linked without running the scripts by hand.

## Run locally

```bash
python3 -m mkdocs serve
```

Then open **http://127.0.0.1:8000** in your browser.

- **Left navigation** — Home, Full index, Topic list, and each category (e.g. Data Storage). Click a category to open its section page with **clickable topic links**.
- **Section pages** — Each category has an index page with a “Topics in this section” list; click any topic to open that page.
- **Full index** — The “Full index” nav item is a single page with all topics and links.
- **Search** — Use the search icon in the header to find terms.
- **Small screens** — Use the **☰ menu** (top left) to open the navigation.

## Build static site (optional)

```bash
python3 -m mkdocs build
```

Output is in the `site/` directory. You can deploy that folder to GitHub Pages, Netlify, or any static host.
