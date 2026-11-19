"""
Sitio de práctica psicológica: MVP en Streamlit, segunda variante de estilo.
Ejecutar:  pip install streamlit  &&  streamlit run app_second.py
Editá los bloques PRACTICA / SERVICIOS / INFORMES / ARTICULOS para cambiar el contenido.
"""
import streamlit as st

# ----------------------------------------------------------------- CONTENIDO
PRACTICA = {
    "nombre": "Dra. Ana Morales",
    "titulo": "Psicóloga clínica",
    "lema": "Un espacio seguro para hablar, comprender y avanzar.",
    "intro": (
        "Acompaño a niñas, niños, adolescentes y adultos con terapia cognitivo-conductual, "
        "orientación a familias y seguimiento cercano. Atención presencial y virtual."
    ),
    "telefono": "+506 2222 0000",
    "correo": "contacto@ejemplo.com",
    "direccion": "Torre Médica, Of. 304, San José, Costa Rica",
    "horario": "Lunes a viernes 8:00–18:00 · Sábados 8:00–12:00",
    "colegiatura": "Colegio de Psicólogos de Costa Rica, N.º 00000",
    "emergencia": "911",
}

SERVICIOS = [
    ("🧒", "Niñez y adolescencia", "Acompañamiento en emociones, conducta, estudios y relaciones."),
    ("🧑", "Terapia individual", "Ansiedad, depresión, duelo y cambios importantes de vida."),
    ("👨‍👩‍👧", "Familias y parejas", "Comunicación, límites y acuerdos para convivir mejor."),
    ("💻", "Consulta virtual", "Sesiones por videollamada segura desde cualquier lugar."),
    ("📋", "Evaluación psicológica", "Valoración estructurada con informe escrito."),
    ("🤝", "Talleres y charlas", "Actividades para escuelas, colegios y empresas."),
]

INFORMES = [
    ("Informe anual", "2025", "Resultados de la práctica, atenciones realizadas y percepción de las personas usuarias.", "#"),
    ("Guía para familias", "2025", "Qué esperar de las primeras tres sesiones y cómo apoyar el proceso en casa.", "#"),
    ("Encuesta comunitaria", "2024", "Necesidades de salud mental reportadas por 420 personas de la zona.", "#"),
]

ARTICULOS = [
    ("Ansiedad", "12 de noviembre de 2026", "Por qué la ansiedad aumenta de noche y qué ayuda",
     "Tres técnicas basadas en evidencia para calmar los pensamientos antes de dormir.", "#"),
    ("Trabajo", "29 de octubre de 2026", "Agotamiento laboral no es lo mismo que estrés",
     "Cómo notar la diferencia y cuándo conviene buscar apoyo profesional.", "#"),
    ("Crianza", "14 de octubre de 2026", "Cómo hablar con adolescentes sobre salud mental",
     "Frases para abrir la conversación y mantenerla en el tiempo.", "#"),
    ("Terapia", "2 de octubre de 2026", "Qué esperar de la primera sesión",
     "Un recorrido sencillo, desde las preguntas iniciales hasta los próximos pasos.", "#"),
]

# -------------------------------------------------------------------- TEMA
AZUL = "#0B5CAB"
CELESTE = "#2AA9E0"
AMARILLO = "#F9B233"
NARANJA = "#F26B3A"
VERDE = "#7AB648"
FONDO = "#F3F8FC"
TINTA = "#1F2D3D"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');
html, body, [class*="css"], .stApp {{ font-family: 'Nunito', Arial, sans-serif; color: {TINTA}; }}
html, body, .stApp {{ background: #fff !important; }}
#MainMenu, footer, header[data-testid="stHeader"] {{ display: none; }}
.block-container {{ padding: 0 !important; max-width: 100% !important; }}
/* Streamlit stacks each st.markdown() call with a 16px flex gap; our sections
   already provide their own spacing, so the gap only shows as a stray band
   of the page background between them (most visible at the very top). */
div[data-testid="stMainBlockContainer"] > div[data-testid="stVerticalBlock"] {{ gap: 0 !important; }}
html {{ scroll-behavior: smooth; }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding: 0 24px; }}
a {{ color: {AZUL}; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
a:focus-visible, button:focus-visible {{ outline: 3px solid {NARANJA}; outline-offset: 3px; }}

/* cabecera */
.hdr {{ background: #fff; position: sticky; top: 0; z-index: 50; box-shadow: 0 2px 8px rgba(11,92,171,.10); }}
.hdr .wrap {{ display: flex; align-items: center; justify-content: space-between; height: 80px; gap: 20px; }}
.brand {{ display: flex; align-items: center; gap: 12px; color: {AZUL}; font-weight: 900; font-size: 20px; line-height: 1.15; }}
.brand:hover {{ text-decoration: none; }}
.brand small {{ display: block; font-weight: 600; font-size: 13px; color: #5A6B7D; }}
.mark {{ width: 46px; height: 46px; border-radius: 50%; flex: none; display: grid; place-items: center;
        background: conic-gradient({AMARILLO} 0 25%, {NARANJA} 0 50%, {VERDE} 0 75%, {CELESTE} 0); }}
.mark b {{ width: 34px; height: 34px; border-radius: 50%; background: #fff; display: grid; place-items: center;
          color: {AZUL}; font-size: 15px; }}
.nav {{ display: flex; align-items: center; gap: 6px; }}
.nav a {{ color: {TINTA}; font-weight: 700; font-size: 15px; padding: 9px 16px; border-radius: 999px; }}
.nav a:hover {{ background: {FONDO}; color: {AZUL}; text-decoration: none; }}
.nav a.cta {{ background: {NARANJA}; color: #fff; margin-left: 8px; }}
.nav a.cta:hover {{ background: #D9572A; color: #fff; }}

/* héroe */
.hero {{ background: linear-gradient(135deg, {AZUL} 0%, #1479C9 60%, {CELESTE} 100%); color: #fff;
        position: relative; overflow: hidden; padding: 72px 0 110px; }}
.hero::before, .hero::after {{ content: ""; position: absolute; border-radius: 50%; opacity: .9; }}
.hero::before {{ width: 220px; height: 220px; background: {AMARILLO}; right: -60px; top: -70px; }}
.hero::after {{ width: 140px; height: 140px; background: {VERDE}; left: -40px; bottom: -50px; }}
.hero .wrap {{ display: grid; grid-template-columns: 1.3fr 1fr; gap: 48px; align-items: center; position: relative; z-index: 1; }}
.hero h1 {{ font-size: 46px; line-height: 1.12; font-weight: 900; margin: 0 0 16px; }}
.hero p {{ font-size: 19px; line-height: 1.6; margin: 0 0 28px; max-width: 560px; }}
.btn {{ display: inline-block; font-weight: 800; padding: 14px 28px; border-radius: 999px; background: {AMARILLO}; color: {TINTA} !important; }}
.btn:hover {{ background: #FFC85C; text-decoration: none; }}
.btn.out {{ background: transparent; color: #fff !important; border: 2px solid #fff; padding: 12px 26px; margin-left: 10px; }}
.btn.out:hover {{ background: rgba(255,255,255,.18); }}
.ayuda {{ background: #fff; color: {TINTA}; border-radius: 28px; padding: 28px; box-shadow: 0 10px 30px rgba(0,0,0,.18); }}
.ayuda h3 {{ margin: 0 0 8px; font-size: 22px; color: {AZUL}; font-weight: 900; }}
.ayuda p {{ font-size: 16px; margin: 0 0 14px; line-height: 1.5; }}
.ayuda .tel {{ display: block; background: {NARANJA}; color: #fff !important; text-align: center; font-size: 22px; font-weight: 900;
              padding: 12px; border-radius: 16px; }}
.ayuda .tel:hover {{ background: #D9572A; text-decoration: none; }}
.ayuda small {{ display: block; margin-top: 10px; color: #5A6B7D; font-size: 13px; }}

/* secciones */
section {{ padding: 68px 0; scroll-margin-top: 80px; }}
section.fondo {{ background: {FONDO}; }}
.sec-head {{ text-align: center; margin-bottom: 38px; }}
.sec-head h2 {{ margin: 0 0 10px; font-size: 34px; font-weight: 900; color: {AZUL}; }}
.sec-head .bar {{ display: flex; justify-content: center; gap: 6px; }}
.sec-head .bar i {{ width: 36px; height: 6px; border-radius: 3px; display: block; }}
.sec-head p {{ margin: 14px auto 0; max-width: 680px; font-size: 17px; line-height: 1.6; color: #44566A; }}
.grid {{ display: grid; gap: 26px; }}
.g3 {{ grid-template-columns: repeat(3, 1fr); }}
.g4 {{ grid-template-columns: repeat(4, 1fr); }}

/* tarjetas con ícono */
.ico {{ background: #fff; border-radius: 24px; padding: 28px 24px; text-align: center; border-bottom: 6px solid var(--c);
       box-shadow: 0 4px 16px rgba(11,92,171,.08); }}
.ico:hover {{ box-shadow: 0 8px 24px rgba(11,92,171,.16); }}
.ico .bub {{ width: 72px; height: 72px; border-radius: 50%; margin: 0 auto 16px; display: grid; place-items: center;
            font-size: 34px; background: var(--c); }}
.ico h3 {{ margin: 0 0 8px; font-size: 20px; font-weight: 800; color: {AZUL}; }}
.ico p {{ margin: 0; font-size: 15.5px; line-height: 1.55; color: #44566A; }}

/* tarjetas de contenido */
.card {{ background: #fff; border-radius: 24px; overflow: hidden; display: flex; flex-direction: column; height: 100%;
        box-shadow: 0 4px 16px rgba(11,92,171,.08); }}
.card:hover {{ box-shadow: 0 8px 24px rgba(11,92,171,.16); }}
.thumb {{ height: 140px; position: relative; background: linear-gradient(135deg, {AZUL}, {CELESTE}); }}
.thumb.t2 {{ background: linear-gradient(135deg, {NARANJA}, {AMARILLO}); }}
.thumb.t3 {{ background: linear-gradient(135deg, #3F8F2E, {VERDE}); }}
.thumb.t4 {{ background: linear-gradient(135deg, #0A7FB8, #7FD0F0); }}
.thumb::before {{ content: ""; position: absolute; inset: 0;
    background-image: radial-gradient(rgba(255,255,255,.25) 1.5px, transparent 1.5px);
    background-size: 15px 15px; }}
.thumb span {{ position: absolute; left: 20px; bottom: 12px; color: #fff; font-weight: 900; font-size: 30px; z-index: 1; }}
.thumb svg {{ position: absolute; right: 16px; bottom: 10px; width: 54px; height: 54px; opacity: .35; }}
.body {{ padding: 20px 22px 24px; display: flex; flex-direction: column; gap: 8px; flex: 1; }}
.meta {{ font-size: 13px; color: #5A6B7D; font-weight: 600; }}
.tag {{ display: inline-block; background: {FONDO}; color: {AZUL}; font-weight: 800; padding: 3px 12px; border-radius: 999px; margin-right: 6px; }}
.card h3 {{ margin: 0; font-size: 19px; line-height: 1.3; font-weight: 800; }}
.card h3 a {{ color: {TINTA}; }}
.card h3 a:hover {{ color: {AZUL}; }}
.card p {{ margin: 0; font-size: 15.5px; line-height: 1.55; color: #44566A; flex: 1; }}
.mas {{ align-self: flex-start; background: {AZUL}; color: #fff !important; font-weight: 800; font-size: 14px; padding: 8px 18px; border-radius: 999px; margin-top: 6px; }}
.mas:hover {{ background: {NARANJA}; text-decoration: none; }}

/* contacto */
.dato {{ background: #fff; border-radius: 20px; padding: 16px 20px; margin-bottom: 14px; display: flex; gap: 14px; align-items: center;
        box-shadow: 0 4px 16px rgba(11,92,171,.08); }}
.dato .e {{ width: 46px; height: 46px; border-radius: 50%; background: {AMARILLO}; display: grid; place-items: center; font-size: 22px; flex: none; }}
.dato b {{ display: block; font-size: 14px; color: #5A6B7D; font-weight: 700; }}
.dato span {{ font-size: 16.5px; font-weight: 700; }}
.aviso {{ background: #FFF1E8; border-left: 6px solid {NARANJA}; border-radius: 14px; padding: 14px 18px; font-size: 15px; line-height: 1.5; }}
div[data-testid="stForm"] {{ background: #fff; border: 0; border-radius: 24px; padding: 26px; box-shadow: 0 4px 16px rgba(11,92,171,.08); }}
div[data-testid="stFormSubmitButton"] button {{ background: {NARANJA}; color: #fff; border: 0; border-radius: 999px; font-weight: 800; padding: 8px 28px; }}
div[data-testid="stFormSubmitButton"] button:hover {{ background: #D9572A; color: #fff; }}

/* pie */
.foot {{ background: {AZUL}; color: #DCEBFA; padding: 44px 0 36px; font-size: 15px; line-height: 1.7; }}
.foot .wrap {{ display: flex; justify-content: space-between; gap: 32px; flex-wrap: wrap; }}
.foot strong {{ color: #fff; }}
.foot-bar {{ height: 8px; background: linear-gradient(90deg, {AMARILLO} 0 25%, {NARANJA} 0 50%, {VERDE} 0 75%, {CELESTE} 0); }}

@media (max-width: 900px) {{
  .hero .wrap {{ grid-template-columns: 1fr; }}
  .g3, .g4 {{ grid-template-columns: 1fr 1fr; }}
  .nav a:not(.cta) {{ display: none; }}
  .hero h1 {{ font-size: 34px; }}
}}
@media (max-width: 600px) {{ .g3, .g4 {{ grid-template-columns: 1fr; }} }}
@media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} }}
</style>
"""


# Iconos livianos en línea para las miniaturas de las tarjetas, en lugar de
# depender de la red para cargar imágenes externas.
ICONO_INFORME = ('<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5">'
                  '<path d="M6 2h9l3 3v17H6z"/><path d="M14 2v4h4"/>'
                  '<path d="M9 12h6M9 15.5h6M9 9h3"/></svg>')
ICONO_ARTICULO = ('<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5">'
                   '<path d="M3 5c3-1.3 6-1.3 9 0v14c-3-1.3-6-1.3-9 0z"/>'
                   '<path d="M21 5c-3-1.3-6-1.3-9 0v14c3-1.3 6-1.3 9 0z"/></svg>')


def html(s: str) -> None:
    # quita sangrías y líneas vacías para que Markdown no trate el HTML como bloque de código
    st.markdown("".join(line.strip() for line in s.splitlines()), unsafe_allow_html=True)


def iniciales(nombre: str) -> str:
    partes = [x for x in nombre.replace(".", " ").split() if x.lower() not in ("dr", "dra")]
    return "".join(x[0] for x in partes[:2]).upper()


def titulo_seccion(titulo: str, sub: str = "") -> str:
    barra = "".join(f'<i style="background:{c}"></i>' for c in (AMARILLO, NARANJA, VERDE, CELESTE))
    extra = f"<p>{sub}</p>" if sub else ""
    return f'<div class="sec-head"><h2>{titulo}</h2><div class="bar">{barra}</div>{extra}</div>'


# ------------------------------------------------------------------ PÁGINA
st.set_page_config(page_title=f"{PRACTICA['nombre']} · {PRACTICA['titulo']}", page_icon="🧠", layout="wide")
html(CSS)
p = PRACTICA
tel = p["telefono"].replace(" ", "")

html(f"""
<header class="hdr"><div class="wrap">
<a class="brand" href="#inicio"><span class="mark"><b>{iniciales(p['nombre'])}</b></span>
<span>{p['nombre']}<small>{p['titulo']}</small></span></a>
<nav class="nav" aria-label="Principal">
<a href="#servicios">Servicios</a><a href="#informes">Informes</a><a href="#articulos">Artículos</a>
<a class="cta" href="#contacto">Contacto</a>
</nav></div></header>
<div id="inicio"></div>
""")

html(f"""
<div class="hero"><div class="wrap">
<div>
<h1>{p['lema']}</h1>
<p>{p['intro']}</p>
<a class="btn" href="#contacto">Agendá tu cita</a>
<a class="btn out" href="#articulos">Leé nuestros artículos</a>
</div>
<aside class="ayuda" aria-label="Ayuda inmediata">
<h3>¿Necesitás ayuda?</h3>
<p>Escribinos o llamanos y coordinamos una primera consulta.</p>
<a class="tel" href="tel:{tel}">{p['telefono']}</a>
<small>En una emergencia llamá al {p['emergencia']}. Este sitio no atiende urgencias.</small>
</aside>
</div></div>
""")

# Servicios
colores = [AMARILLO, CELESTE, VERDE, NARANJA, CELESTE, AMARILLO]
servicios_html = "".join(
    f'<div class="ico" style="--c:{colores[i % len(colores)]}"><div class="bub">{e}</div><h3>{t}</h3><p>{d}</p></div>'
    for i, (e, t, d) in enumerate(SERVICIOS)
)
html(f"""
<section id="servicios"><div class="wrap">
{titulo_seccion("Servicios", "Atención profesional, cercana y confidencial.")}
<div class="grid g3">{servicios_html}</div>
</div></section>
""")

# Informes
fondos = ["", "t2", "t3", "t4"]
informes_html = "".join(
    f"""<article class="card"><div class="thumb {fondos[i % 4]}">{ICONO_INFORME}<span>{anio}</span></div>
<div class="body"><div class="meta"><span class="tag">Informe</span></div>
<h3><a href="{url}">{titulo}</a></h3><p>{desc}</p>
<a class="mas" href="{url}">Descargar PDF</a></div></article>"""
    for i, (titulo, anio, desc, url) in enumerate(INFORMES)
)
html(f"""
<section id="informes" class="fondo"><div class="wrap">
{titulo_seccion("Informes", "Documentos para conocer mejor nuestro trabajo.")}
<div class="grid g3">{informes_html}</div>
</div></section>
""")

# Artículos
articulos_html = "".join(
    f"""<article class="card"><div class="thumb {fondos[i % 4]}">{ICONO_ARTICULO}</div>
<div class="body"><div class="meta"><span class="tag">{cat}</span>{fecha}</div>
<h3><a href="{url}">{titulo}</a></h3><p>{desc}</p>
<a class="mas" href="{url}">Leer artículo</a></div></article>"""
    for i, (cat, fecha, titulo, desc, url) in enumerate(ARTICULOS)
)
html(f"""
<section id="articulos"><div class="wrap">
{titulo_seccion("Últimos artículos", "Información sencilla para cuidar tu bienestar emocional.")}
<div class="grid g4">{articulos_html}</div>
</div></section>
""")

# Contacto (el formulario debe ser un widget nativo de Streamlit)
html(f'<section id="contacto" class="fondo" style="padding-bottom:0"><div class="wrap">{titulo_seccion("Contacto", "Escribinos y te respondemos en un máximo de dos días hábiles.")}</div></section>')
html(f'<div style="background:{FONDO};height:8px"></div>')
fondo_cont = st.container()
with fondo_cont:
    _, medio, _ = st.columns([1, 10, 1])
    with medio:
        izq, der = st.columns(2, gap="large")
        with izq:
            html(f"""
<div class="dato"><div class="e">📍</div><div><b>Consultorio</b><span>{p['direccion']}</span></div></div>
<div class="dato"><div class="e">📞</div><div><b>Teléfono</b><span><a href="tel:{tel}">{p['telefono']}</a></span></div></div>
<div class="dato"><div class="e">✉️</div><div><b>Correo</b><span><a href="mailto:{p['correo']}">{p['correo']}</a></span></div></div>
<div class="dato"><div class="e">🕒</div><div><b>Horario</b><span>{p['horario']}</span></div></div>
<div class="aviso"><strong>¿Es una emergencia?</strong> Este formulario no se monitorea de forma urgente.
Llamá al {p['emergencia']} o acudí al centro de salud más cercano.</div>
""")
        with der:
            with st.form("form_contacto", clear_on_submit=True):
                nombre = st.text_input("Nombre completo")
                correo = st.text_input("Correo electrónico")
                motivo = st.selectbox("Motivo de la consulta", ["Primera consulta", "Consulta virtual", "Evaluación psicológica", "Otro"])
                mensaje = st.text_area("Mensaje", height=120)
                enviado = st.form_submit_button("Enviar mensaje")
            if enviado:
                if nombre.strip() and "@" in correo and mensaje.strip():
                    st.success("Mensaje enviado. Te responderemos en un máximo de dos días hábiles.")
                    # TODO: conectar con correo / CRM / Google Sheet
                else:
                    st.error("Ingresá tu nombre, un correo válido y un mensaje.")
html(f'<div style="background:{FONDO};height:64px"></div>')

html(f"""
<div class="foot-bar"></div>
<footer class="foot"><div class="wrap">
<div><strong>{p['nombre']}</strong><br>{p['titulo']}<br>{p['colegiatura']}</div>
<div>{p['direccion']}<br>{p['telefono']} · {p['correo']}</div>
<div>© 2026 {p['nombre']}.<br>El contenido es informativo y no sustituye la atención profesional.</div>
</div></footer>
""")
