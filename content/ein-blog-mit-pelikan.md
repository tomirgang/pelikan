Title: Ein Blog mit Pelikan
Date: 2022-09-03 10:55
Category: Web

Hi,

dies ist mein neuer Blog!

Mein Ziel ist es einen 100%dig wartungsfreien, sicheren und kostengünstigen Blog aufzusetzen.
Um dies zu erreichen habe ich mir für folgendes Setup entschieden:

- eigene Domain (kostet ein paar Euro im Jahr) -> Hetzner Domains
- statisch generierter Inhalt (wartungsfrei, 100%dig sicher) -> Pelican Static-Site-Generator
- Github Pages (kostenloses Hosting für statische Inhalte)

## Pelican einrichten

- [Pelican Quickstart](https://getpelican.com/#quickstart)
- [A Pelican Tutorial: Static, Python-Powered Blog with Search & Comments](https://snipcart.com/blog/pelican-blog-tutorial-search-comments)
- [Rasor's Tech Blog: Using Pelican Themes](https://rasor.github.io/using-pelican-themes.html)
- [Pelikan Doku](https://docs.getpelican.com/en/stable/index.html)
- [Mein Theme](https://github.com/tcarwash/blue-penguin-dark)
- [Such-Plugin](https://github.com/pelican-plugins/search)

### Vorbereitung (nicht notwendig)

Klonen der [Pelican Plugins](https://github.com/getpelican/pelican-plugins) und der [Pelican Themes](https://github.com/getpelican/pelican-themes)
Die Repos sind in git Submodulen organisert. Checkout der vollständigen Inhalte funktioniert mit:

```bash
it submodule update --init --recursive
```

### Projekt 

Einrichten des Pelikan Projekts:

- Projektordner anlegen und hinein wechseln
- Python venv anlegen: `python -m venv venv`
- Python venv aktivieren: `source ./venv/bin/activate`
- Pelican installieren: `pip install "pelican[markdown]"`
- Pelican Projekt anlegen: `pelican-quickstart`
- [Artikel anlegen](https://getpelican.com/#quickstart)

### Theme einrichten

- Theme auswählen
- Theme in den Projektordner kopieren
- Theme installieren: `pelican-themes -i {Ordner}`
- Theme aktivieren: In `pelicanconf.py` folgende Zeilen hinzufügen:

```Python
# Enalbe theme
THEME = 'blue-penguin-dark'
```

### Such-Plugin einrichten: Pelikan search

#### Abhängigkeiten installieren

- Pelikan search benötigt [Stork](https://stork-search.net/docs/install)
- Installieren mit Cargo: `cargo install stork-search --locked`
- Stork überprüfen: `stork --help`
- Pelikan search installieren: `pip install pelican-search`

#### Plugin einbauen

- Plugin aktivieren / Such-Index generieren: In `pelicanconf.py` folgende Zeilen hinzufügen:

```Python
# Search settings
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "article"
```
Default-Selektor ist "main". Dieser wird von meinem Theme nicht verwendet.

- Plugin in Templates integrieren: In `blue-penguin-dark/templates/base.html` folgende Zeilen hinzufügen:

Im Header-Block

```HTML
        <div>
        Search: <input data-stork="sitesearch" />
        <div data-stork="sitesearch-output"></div>
        </div>
```

Vor dem "</body>"-Tag:

```HTML
    <!-- Stork search -->
    <link rel="stylesheet" media="screen and (prefers-color-scheme: dark)" href="https://files.stork-search.net/dark.css">
    <script src="https://files.stork-search.net/releases/v1.5.0/stork.js"></script>
    <script>
        stork.register("sitesearch", "{{ SITEURL }}/search-index.st")
    </script>
```

### Abschluss

- Abhängigkeiten dokumentieren: `pip freeze > dependencies.txt`
- .gitignore erstellen ([Generator](https://www.toptal.com/developers/gitignore): Python, Linux, Windows, macOS, VisualStudioCode)
