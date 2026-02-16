# MkDocs

## Overview
MkDocs is a static site generator that builds documentation from Markdown files. It is widely used to create browsable, searchable documentation sites—including glossaries and technical references—with minimal configuration. For data teams, MkDocs helps publish and navigate data pipeline documentation, data dictionaries, and glossary content like this one.

## Definition
MkDocs is an open-source, Python-based tool that takes a directory of Markdown files and a single YAML config file, then generates a static HTML site with navigation, search, and theming. Content stays in Markdown; MkDocs handles structure, links, and build output (e.g. for local serving or deployment to GitHub Pages, Netlify, or S3).

## Key Concepts

- **docs_dir**: The folder containing your Markdown source files (e.g. `docs/`). MkDocs builds only from this directory.
- **nav**: The navigation structure is defined in `mkdocs.yml`. You list pages and sections; MkDocs renders them as a sidebar and (with themes like Material) as tabs or expandable sections.
- **Theme**: The look and behavior of the site. The default theme is minimal; **Material for MkDocs** adds search, dark mode, and rich navigation.
- **Plugins**: Extensions that run during the build (e.g. search index, custom pre-build steps, section index updates).
- **Static output**: MkDocs produces plain HTML/CSS/JS in a `site/` directory—no server-side runtime, so it can be hosted anywhere.

## How It Works

1. You run `mkdocs build` or `mkdocs serve` from the project root.
2. MkDocs reads `mkdocs.yml` (site name, docs directory, theme, plugins, nav).
3. It collects all Markdown files under `docs_dir`, resolves the nav, and runs plugins (e.g. search, custom hooks).
4. Each Markdown file is converted to HTML; the theme wraps it with layout, sidebar, and assets.
5. Output is written to `site/`. With `serve`, a local server and live reload are started.

Key behaviors:
- **Links**: Relative links between `.md` files work; MkDocs turns them into correct URLs.
- **Index pages**: A file named `index.md` (or `README.md`) in a directory becomes the default page for that path.
- **Search**: Enabled via the search plugin; the theme provides the UI.

## Use Cases

- **Glossaries and term bases**: Browsable term lists with categories and full-text search (e.g. this Data Pipeline Glossary).
- **Data pipeline documentation**: Describing architectures, ingestion, storage, and governance in one site.
- **API or tool docs**: Technical documentation for internal or external consumers.
- **Project wikis**: Lightweight docs living in the repo, built and deployed on push.
- **Data dictionaries and catalogs**: Presenting table/column metadata and lineage in a readable, linkable format.

## Considerations

- **Content location**: All built content must live under `docs_dir`; symlinks may not be followed, so use real files or a single docs tree.
- **Nav maintenance**: Large sites need either hand-maintained nav or a plugin/script to generate section indexes and links.
- **Python dependency**: Requires Python and `pip install mkdocs` (and theme/plugins). No Node.js or separate build server.
- **Static only**: No server-side logic, auth, or dynamic data—ideal for read-only documentation.

## Best Practices

- **One docs directory**: Keep all source under `docs/` (or your chosen `docs_dir`) and point nav entries to those paths.
- **Section index pages**: Add an `index.md` per section so category URLs have a landing page and you can list topic links there.
- **Theme and plugins**: Use Material for MkDocs and only the plugins you need; disable unused features to keep builds fast.
- **Version the config**: Keep `mkdocs.yml` and any custom plugins in version control so the site is reproducible.
- **CI/CD**: Run `mkdocs build` in CI and deploy the `site/` directory to your host (e.g. GitHub Pages, S3, Netlify).

## Products & Tools

- **MkDocs**: The core generator ([mkdocs.org](https://www.mkdocs.org/)).
- **Material for MkDocs**: Popular theme with search, tabs, and dark mode ([squidfunk.github.io/mkdocs-material](https://squidfunk.github.io/mkdocs-material/)).
- **mkdocs-awesome-pages-plugin / mkdocs-awesome-nav**: Automate nav from folder structure.
- **GitHub Pages, Netlify, Read the Docs**: Common hosts for MkDocs output.
- **MkDocs section index plugins**: Custom plugins (e.g. for this glossary) that refresh section index pages and marks (e.g. Products & Tools) before each build.

## Related Topics

- [Data Pipeline Documentation](data-pipeline-documentation.md)
- [Data Dictionary](../governance/data-dictionary.md)
- [Metadata Management](../governance/metadata-management.md)
- [Version Control & Git](../version-control/index.md)

## Further Reading

- [MkDocs User Guide](https://www.mkdocs.org/user-guide/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [MkDocs Plugins](https://github.com/mkdocs/catalog)

---

**Category**: Cross-cutting  
**Last Updated**: 2026
