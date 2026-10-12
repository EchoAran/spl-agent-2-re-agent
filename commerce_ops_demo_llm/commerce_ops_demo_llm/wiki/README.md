# Repository LLM Wiki

This directory contains an SPL-first LLM Wiki: compiled wiki pages preserve complete SPL content as the primary body, while JSON fields provide navigation, links, backlinks, search, and graph metadata.

Single-file exports:

- `LLM_WIKI.md`: human-readable SPL-first wiki export suitable for sharing.
- `LLM_WIKI.full.md`: detailed SPL-first export with links, source refs, symbols, and graph refs.

Run a local static server from this `wiki` directory:

```powershell
python -m http.server 8765
```

Then open:

```text
http://localhost:8765/frontend/index.html
```

Do not open `frontend/index.html` directly with `file://`, because browsers may block JSON fetches.
