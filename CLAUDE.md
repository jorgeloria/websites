# web-site-doc

Two standalone, single-file Streamlit MVPs for the same fictional psychology
practice ("Dra./Dr. Ana Morales"), each styled after a different reference site:

- [app.py](app.py) — English content, styled after [who.int](https://www.who.int/) (navy/blue, squared-off cards).
- [app_pani.py](app_pani.py) — Spanish content, styled after [pani.go.cr](https://pani.go.cr/) (rounded, colorful, playful).

They are independent and not imported by one another — treat edits to one as
isolated from the other unless the user asks for both to change together.

## Running

```bash
.venv/bin/streamlit run app.py
```
```bash
.venv/bin/streamlit run app_pani.py
```

Only `streamlit` (and its transitive deps: pandas, altair, pyarrow, etc.) is
installed in `.venv`. There is no `requirements.txt` or `pyproject.toml` — if
adding a dependency, install it into `.venv` and consider adding a
requirements file at that point.

## Structure of each app

Both files follow the same pattern, just with English/Spanish naming:

1. **Content dict/lists at the top** (`PRACTICE`/`PRACTICA`, `SERVICES`/`SERVICIOS`,
   `REPORTS`/`INFORMES`, `ARTICLES`/`ARTICULOS`) — plain Python data. This is
   where page copy lives; edit here, not in the HTML-building code below.
2. **CSS block** (`CSS` f-string) — theme colors are defined as variables just
   above it (`BLUE`/`NAVY`/... in app.py, `AZUL`/`CELESTE`/... in app_pani.py)
   and interpolated into the stylesheet. Change the theme by changing those
   color constants, not by hand-editing hex codes throughout the CSS.
3. **Page body** — built by calling the local `html()` helper with f-strings
   of raw HTML (`unsafe_allow_html=True`), interleaved with native Streamlit
   widgets (`st.columns`, `st.form`) for the contact section specifically.

Key conventions:
- `html()` strips indentation/blank lines from its input so Streamlit's
  Markdown renderer doesn't mistake the HTML for a code block. Always route
  new raw-HTML output through `html()`, not a raw `st.markdown()` call.
- The Streamlit chrome (`#MainMenu`, `footer`, the default header) is hidden
  via CSS; layout is a hand-built header/hero/sections/footer using `.wrap`
  as the max-width container, mimicking a normal marketing site rather than
  a typical Streamlit data-app layout.
- The contact form is the only native Streamlit widget area. It validates
  name/email-contains-"@"/message client-side and shows `st.success`/
  `st.error`, but never actually sends anything — see the
  `# TODO: connect to email / CRM / Google Sheet` comment in both files.
  Don't assume the form works end-to-end.
- Anchor links (`#services`, `#contact`, etc. / `#servicios`, `#contacto`,
  etc.) drive the nav; keep `id="..."` attributes on sections in sync with
  the `href`s in the nav links if you rename a section.
- All "Report"/"Article" download/read links are placeholder `"#"` URLs.

## Content notes

- Dates in `ARTICLES`/`ARTICULOS` are hardcoded strings (e.g. "12 November
  2026") — there's no date logic, just literal text to edit.
- app_pani.py includes a Costa Rican emergency number (911) and a
  crisis/emergency disclaimer in both the hero and contact sections; app.py
  has an equivalent but shorter disclaimer only in the contact section. Keep
  this safety disclaimer when editing either contact area.
- Practice details (name, phone, email, address, license number) are
  placeholder/example values, independently duplicated in each file — update
  both if the user wants a real practice's info reflected consistently.

## Git

Single-branch repo (`main`) tracking `origin` =
`git@github.com:jorgeloria/websites.git`. `.venv` is gitignored.
