"""
Psychology practice site: Streamlit MVP, styled after who.int.
Run:  pip install streamlit  &&  streamlit run app.py
Edit the PRACTICE / REPORTS / ARTICLES blocks below to change content.
"""
import streamlit as st

# ----------------------------------------------------------------- CONTENT
PRACTICE = {
    "name": "Dr. Ana Morales",
    "title": "Clinical Psychologist",
    "tagline": "Evidence-based care for anxiety, depression, and life transitions.",
    "intro": (
        "I work with adults and adolescents using cognitive behavioural therapy, "
        "acceptance-based approaches, and structured follow-up. Sessions are "
        "available in person and online, in English and Spanish."
    ),
    "phone": "+506 2222 0000",
    "email": "contact@example.com",
    "address": "Torre Médica, Of. 304, San José, Costa Rica",
    "hours": "Mon–Fri 8:00–18:00 · Sat 8:00–12:00",
    "license": "Colegio de Psicólogos de Costa Rica, No. 00000",
}

SERVICES = [
    ("Individual therapy", "One-to-one sessions for adults and adolescents."),
    ("Couples and family", "Communication, conflict, and shared goals."),
    ("Online consultation", "Secure video sessions from anywhere."),
    ("Psychological assessment", "Structured evaluation with a written report."),
]

REPORTS = [
    ("Annual report", "2025", "Practice outcomes, session volumes, and patient-reported results.", "#"),
    ("Clinical guide", "2025", "A patient guide to what happens in the first three sessions.", "#"),
    ("Community survey", "2024", "Mental health needs reported by 420 local respondents.", "#"),
]

ARTICLES = [
    ("Anxiety", "12 November 2026", "Why anxiety peaks at night, and what helps",
     "Three evidence-based techniques to quiet racing thoughts before sleep.", "#"),
    ("Workplace", "29 October 2026", "Burnout is not the same as stress",
     "How to tell the difference, and when to ask for professional support.", "#"),
    ("Parenting", "14 October 2026", "Talking with teenagers about their mental health",
     "Practical openers that keep the conversation going.", "#"),
    ("Therapy", "2 October 2026", "What to expect from your first session",
     "A plain-language walkthrough, from intake questions to next steps.", "#"),
]

# ------------------------------------------------------------------ THEME
BLUE = "#009ADE"      # WHO brand blue
NAVY = "#003A5D"
INK = "#1A1A1A"
GREY = "#F2F5F8"
LINE = "#D9DFE5"

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;600;700&display=swap');
html, body, [class*="css"], .stApp {{ font-family: 'Noto Sans', Arial, sans-serif; color: {INK}; }}
html, body, .stApp {{ background: #fff !important; }}
#MainMenu, footer, header[data-testid="stHeader"] {{ display: none; }}
.block-container {{ padding: 0 !important; max-width: 100% !important; }}
/* Streamlit stacks each st.markdown() call with a 16px flex gap; our sections
   already provide their own spacing, so the gap only shows as a stray band
   of the page background between them (most visible at the very top). */
div[data-testid="stMainBlockContainer"] > div[data-testid="stVerticalBlock"] {{ gap: 0 !important; }}
.wrap {{ max-width: 1180px; margin: 0 auto; padding: 0 24px; }}
html {{ scroll-behavior: smooth; }}
a {{ color: {BLUE}; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
a:focus-visible, button:focus-visible {{ outline: 3px solid {NAVY}; outline-offset: 2px; }}

/* top utility bar + header */
.util {{ background: {NAVY}; color: #fff; font-size: 13px; padding: 7px 0; }}
.util .wrap {{ display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap; }}
.hdr {{ background: #fff; border-bottom: 1px solid {LINE}; position: sticky; top: 0; z-index: 50; }}
.hdr .wrap {{ display: flex; align-items: center; justify-content: space-between; height: 72px; gap: 24px; }}
.brand {{ display: flex; align-items: center; gap: 12px; color: {INK}; font-weight: 700; font-size: 18px; line-height: 1.2; }}
.brand:hover {{ text-decoration: none; }}
.brand small {{ display: block; font-weight: 400; font-size: 13px; color: #555; }}
.mark {{ width: 40px; height: 40px; border-radius: 50%; background: {BLUE}; color: #fff;
        display: grid; place-items: center; font-weight: 700; font-size: 18px; flex: none; }}
.nav {{ display: flex; gap: 28px; }}
.nav a {{ color: {INK}; font-weight: 600; font-size: 15px; padding: 24px 0; border-bottom: 3px solid transparent; }}
.nav a:hover {{ color: {BLUE}; border-bottom-color: {BLUE}; text-decoration: none; }}

/* hero */
.hero {{ background: linear-gradient(120deg, {NAVY} 0%, #005F8F 55%, {BLUE} 100%); color: #fff; padding: 72px 0 96px; }}
.hero .wrap {{ display: grid; grid-template-columns: 1.4fr 1fr; gap: 48px; align-items: center; }}
.hero h1 {{ font-size: 44px; line-height: 1.15; font-weight: 700; margin: 0 0 16px; }}
.hero p {{ font-size: 18px; line-height: 1.6; max-width: 560px; margin: 0 0 28px; }}
.btn {{ display: inline-block; background: #fff; color: {NAVY} !important; font-weight: 700; padding: 12px 24px; border-radius: 2px; }}
.btn:hover {{ background: {GREY}; text-decoration: none; }}
.btn.alt {{ background: transparent; color: #fff !important; border: 2px solid #fff; margin-left: 10px; padding: 10px 22px; }}
.btn.alt:hover {{ background: rgba(255,255,255,.15); }}
.profile {{ background: #fff; color: {INK}; padding: 28px; border-top: 6px solid {BLUE}; }}
.profile h3 {{ margin: 0 0 4px; font-size: 22px; }}
.profile .role {{ color: #555; margin-bottom: 16px; font-size: 15px; }}
.profile dl {{ margin: 0; font-size: 14px; line-height: 1.5; }}
.profile dt {{ font-weight: 700; margin-top: 10px; }}
.profile dd {{ margin: 0; }}

/* sections */
section {{ padding: 64px 0; scroll-margin-top: 72px; }}
section.alt {{ background: {GREY}; }}
.sec-head {{ display: flex; justify-content: space-between; align-items: baseline;
            border-bottom: 3px solid {BLUE}; padding-bottom: 10px; margin-bottom: 32px; }}
.sec-head h2 {{ margin: 0; font-size: 28px; font-weight: 700; }}
.grid {{ display: grid; gap: 24px; }}
.g3 {{ grid-template-columns: repeat(3, 1fr); }}
.g4 {{ grid-template-columns: repeat(4, 1fr); }}

.svc {{ background: #fff; border: 1px solid {LINE}; border-left: 5px solid {BLUE}; padding: 22px; }}
.svc h3 {{ margin: 0 0 8px; font-size: 18px; }}
.svc p {{ margin: 0; font-size: 15px; line-height: 1.55; color: #444; }}

.card {{ background: #fff; border: 1px solid {LINE}; display: flex; flex-direction: column; height: 100%; }}
.card:hover {{ border-color: {BLUE}; box-shadow: 0 2px 10px rgba(0,58,93,.12); }}
.thumb {{ height: 150px; background: linear-gradient(135deg, {NAVY}, {BLUE}); position: relative; overflow: hidden; }}
.thumb.t2 {{ background: linear-gradient(135deg, #00669C, #5CC3EC); }}
.thumb.t3 {{ background: linear-gradient(135deg, #0B2E4A, #2F8DBE); }}
.thumb::before {{ content: ""; position: absolute; inset: 0;
    background-image: radial-gradient(rgba(255,255,255,.22) 1.5px, transparent 1.5px);
    background-size: 15px 15px; }}
.thumb span {{ position: absolute; left: 16px; bottom: 12px; color: #fff; font-weight: 700; font-size: 26px; z-index: 1; }}
.thumb svg {{ position: absolute; right: 14px; bottom: 10px; width: 56px; height: 56px; opacity: .32; }}
.body {{ padding: 18px 20px 22px; display: flex; flex-direction: column; gap: 8px; flex: 1; }}
.meta {{ font-size: 13px; color: #555; }}
.tag {{ color: {BLUE}; font-weight: 700; }}
.card h3 {{ margin: 0; font-size: 18px; line-height: 1.35; }}
.card h3 a {{ color: {INK}; }}
.card h3 a:hover {{ color: {BLUE}; }}
.card p {{ margin: 0; font-size: 15px; line-height: 1.55; color: #444; flex: 1; }}
.more {{ font-weight: 700; font-size: 14px; }}

/* contact */
.contact {{ display: grid; grid-template-columns: 1fr 1fr; gap: 48px; }}
.contact dl {{ margin: 0; }}
.contact dt {{ font-weight: 700; margin-top: 18px; }}
.contact dd {{ margin: 2px 0 0; font-size: 16px; }}
div[data-testid="stForm"] {{ border: 1px solid {LINE}; border-top: 5px solid {BLUE}; border-radius: 0; padding: 24px; background: #fff; }}
div[data-testid="stFormSubmitButton"] button {{ background: {BLUE}; color: #fff; border: 0; border-radius: 2px; font-weight: 700; padding: 8px 24px; }}
div[data-testid="stFormSubmitButton"] button:hover {{ background: {NAVY}; color: #fff; }}

/* footer */
.foot {{ background: {NAVY}; color: #d7e6f0; padding: 40px 0; font-size: 14px; line-height: 1.7; }}
.foot .wrap {{ display: flex; justify-content: space-between; gap: 32px; flex-wrap: wrap; }}
.foot strong {{ color: #fff; }}
.notice {{ background: #FFF4D6; border-left: 5px solid #E0A800; padding: 14px 18px; font-size: 14px; margin-top: 28px; }}

@media (max-width: 900px) {{
  .hero .wrap, .contact {{ grid-template-columns: 1fr; }}
  .g3, .g4 {{ grid-template-columns: 1fr 1fr; }}
  .nav {{ display: none; }}
  .hero h1 {{ font-size: 34px; }}
}}
@media (max-width: 600px) {{ .g3, .g4 {{ grid-template-columns: 1fr; }} }}
@media (prefers-reduced-motion: reduce) {{ html {{ scroll-behavior: auto; }} }}
</style>
"""


# Lightweight inline icons for the card thumbnails, standing in for photography
# without depending on the network to load any external images.
ICON_REPORT = ('<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5">'
               '<path d="M6 2h9l3 3v17H6z"/><path d="M14 2v4h4"/>'
               '<path d="M9 12h6M9 15.5h6M9 9h3"/></svg>')
ICON_ARTICLE = ('<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5">'
                '<path d="M3 5c3-1.3 6-1.3 9 0v14c-3-1.3-6-1.3-9 0z"/>'
                '<path d="M21 5c-3-1.3-6-1.3-9 0v14c3-1.3 6-1.3 9 0z"/></svg>')


def html(s: str) -> None:
    # collapse blank lines/indentation so Markdown never treats the HTML as a code block
    st.markdown("".join(line.strip() for line in s.splitlines()), unsafe_allow_html=True)


def initials(name: str) -> str:
    parts = [p for p in name.replace(".", " ").split() if p.lower() not in ("dr", "dra", "dr.")]
    return "".join(p[0] for p in parts[:2]).upper()


# ------------------------------------------------------------------- PAGE
st.set_page_config(page_title=f"{PRACTICE['name']} · {PRACTICE['title']}", page_icon="🧠", layout="wide")
html(CSS)

p = PRACTICE

html(f"""
<div class="util"><div class="wrap">
<span>{p['hours']}</span><span>{p['phone']} · {p['email']}</span>
</div></div>
<header class="hdr"><div class="wrap">
<a class="brand" href="#top"><span class="mark">{initials(p['name'])}</span>
<span>{p['name']}<small>{p['title']}</small></span></a>
<nav class="nav" aria-label="Main">
<a href="#about">About</a><a href="#services">Services</a><a href="#reports">Reports</a>
<a href="#articles">Articles</a><a href="#contact">Contact</a>
</nav></div></header>
<div id="top"></div>
""")

html(f"""
<div class="hero"><div class="wrap">
<div>
<h1>{p['tagline']}</h1>
<p>{p['intro']}</p>
<a class="btn" href="#contact">Book a consultation</a>
<a class="btn alt" href="#articles">Read the latest articles</a>
</div>
<aside class="profile" id="about" aria-label="Practitioner profile">
<h3>{p['name']}</h3>
<div class="role">{p['title']}</div>
<dl>
<dt>License</dt><dd>{p['license']}</dd>
<dt>Phone</dt><dd><a href="tel:{p['phone'].replace(' ', '')}">{p['phone']}</a></dd>
<dt>Email</dt><dd><a href="mailto:{p['email']}">{p['email']}</a></dd>
<dt>Office</dt><dd>{p['address']}</dd>
</dl></div>
</div></div>
""")

# Services
services_html = "".join(f'<div class="svc"><h3>{t}</h3><p>{d}</p></div>' for t, d in SERVICES)
html(f"""
<section id="services"><div class="wrap">
<div class="sec-head"><h2>Services</h2></div>
<div class="grid g4">{services_html}</div>
</div></section>
""")

# Reports
thumbs = ["", "t2", "t3"]
reports_html = "".join(
    f"""<article class="card">
<div class="thumb {thumbs[i % 3]}">{ICON_REPORT}<span>{year}</span></div>
<div class="body"><div class="meta"><span class="tag">Report</span></div>
<h3><a href="{url}">{title}</a></h3><p>{desc}</p>
<a class="more" href="{url}">Download PDF</a></div></article>"""
    for i, (title, year, desc, url) in enumerate(REPORTS)
)
html(f"""
<section id="reports" class="alt"><div class="wrap">
<div class="sec-head"><h2>Reports</h2></div>
<div class="grid g3">{reports_html}</div>
</div></section>
""")

# Articles
articles_html = "".join(
    f"""<article class="card">
<div class="thumb {thumbs[i % 3]}">{ICON_ARTICLE}</div>
<div class="body"><div class="meta"><span class="tag">{cat}</span> · {date}</div>
<h3><a href="{url}">{title}</a></h3><p>{desc}</p>
<a class="more" href="{url}">Read article</a></div></article>"""
    for i, (cat, date, title, desc, url) in enumerate(ARTICLES)
)
html(f"""
<section id="articles"><div class="wrap">
<div class="sec-head"><h2>Latest articles</h2></div>
<div class="grid g4">{articles_html}</div>
</div></section>
""")

# Contact: two columns, the form must be a native Streamlit widget
html('<section id="contact" class="alt"><div class="wrap"><div class="sec-head"><h2>Contact</h2></div></div></section>')
_, mid, _ = st.columns([1, 10, 1])  # approximates the .wrap width
with mid:
    left, right = st.columns(2, gap="large")
    with left:
        html(f"""
<div class="contact" style="display:block"><dl>
<dt>Office</dt><dd>{p['address']}</dd>
<dt>Phone</dt><dd><a href="tel:{p['phone'].replace(' ', '')}">{p['phone']}</a></dd>
<dt>Email</dt><dd><a href="mailto:{p['email']}">{p['email']}</a></dd>
<dt>Hours</dt><dd>{p['hours']}</dd>
</dl>
<div class="notice"><strong>In a crisis?</strong> This form is not monitored for emergencies.
Contact your local emergency number or the nearest hospital.</div></div>
""")
    with right:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Full name")
            email = st.text_input("Email")
            topic = st.selectbox("Reason for contact", ["First consultation", "Online session", "Assessment", "Other"])
            msg = st.text_area("Message", height=120)
            sent = st.form_submit_button("Send message")
        if sent:
            if name.strip() and "@" in email and msg.strip():
                st.success("Message sent. You will receive a reply within two business days.")
                # TODO: connect to email / CRM / Google Sheet
            else:
                st.error("Enter your name, a valid email, and a message.")

html(f"""
<footer class="foot"><div class="wrap">
<div><strong>{p['name']}</strong><br>{p['title']}<br>{p['license']}</div>
<div>{p['address']}<br>{p['phone']} · {p['email']}</div>
<div>© 2026 {p['name']}. Content is for information only and does not replace professional care.</div>
</div></footer>
""")
