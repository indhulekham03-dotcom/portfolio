"""
INDHULEKHA M. — Economics & Research Portfolio  (Streamlit)

Run:   streamlit run app.py

Put these next to app.py (or inside an "assets" folder):
    profile.jpg           -> your photograph
    Indhulekha_CV.pdf     -> your resume
"""

import base64
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Indhulekha M. | Economics Portfolio", page_icon="📈",
                   layout="wide", initial_sidebar_state="collapsed")

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"


def find_file(names):
    """Look in assets/ first, then next to app.py."""
    for folder in (ASSETS, ROOT):
        for n in names:
            if (folder / n).exists():
                return folder / n
    return ASSETS / names[0]


PHOTO = find_file(["profile.jpg", "portrait.jpg", "profile.jpeg", "portrait.png", "profile.png"])
CV = find_file(["Indhulekha_CV.pdf", "CV.pdf"])

PAGES = {
    "home": "Home",
    "academics": "Academics",
    "research": "Research & Projects",
    "skills": "Skills",
    "about": "About & Contact",
}

# ----------------------------------------------------------------------------
# STYLES  (blue & white wave theme)
# ----------------------------------------------------------------------------
CSS = r"""<style>
@import url('https://fonts.googleapis.com/css2?family=Newsreader:wght@400;500;600&family=Inter:wght@400;500;600&display=swap');
:root{--bg:#f5f8fc;--card:#fff;--ink:#0a1b3d;--muted:#4b5d7a;--blue:#2563a8;--sky:#dce9f7;--line:#dbe5f1;--navy:#061a3d;--btn:#061a3d;--btnt:#fff;--bar:rgba(255,255,255,.92);}
*{box-sizing:border-box}
a{color:inherit;text-decoration:none}
h1,h2,h3,h4{font-family:Newsreader,Georgia,serif;font-weight:500;margin:0;line-height:1.1}
.w{max-width:1160px;margin:0 auto;padding:0 32px;position:relative;z-index:2}
.topbar{position:relative;z-index:50;background:var(--bar);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.topbar .w{display:flex;justify-content:space-between;align-items:center;padding-top:16px;padding-bottom:16px;gap:20px;flex-wrap:wrap}
.brand b{display:block;letter-spacing:.4px;font-size:19px}.brand span{font-size:12px;letter-spacing:1.6px;color:var(--blue);text-transform:uppercase}
.nav{display:flex;gap:34px;flex-wrap:wrap}
.nav a{font-size:15px;padding:6px 0;border-bottom:2px solid transparent;color:var(--muted)}
.nav a:hover{color:var(--ink)}.nav a.on{color:var(--ink);border-color:var(--blue)}
.page{animation:in .5s ease}
@keyframes in{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.hero{position:relative;overflow:hidden}
.waves{position:absolute;inset:0;width:100%;height:100%;z-index:0}
.drift{animation:dr 18s ease-in-out infinite alternate}@keyframes dr{to{transform:translate(14px,-10px)}}
@media(prefers-reduced-motion:reduce){.drift,.page{animation:none}}
.hg{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center;padding:96px 0 90px}
.eyebrow{font-size:12.5px;letter-spacing:3px;color:var(--blue);font-weight:600;text-transform:uppercase;margin-bottom:18px}
.hero h1{white-space:nowrap;font-size:clamp(38px,5.2vw,84px);letter-spacing:-1.5px;margin-bottom:12px}
.role{font-size:17px;color:var(--blue);letter-spacing:1px;margin-bottom:22px;font-weight:500}
.rule{width:54px;height:3px;background:var(--blue);margin-bottom:26px;border-radius:2px}
.lead{font-size:17.5px;color:var(--muted);max-width:540px;margin:0 0 34px}
.btns{display:flex;gap:14px;flex-wrap:wrap}
.btn{display:inline-flex;gap:10px;align-items:center;padding:16px 28px;border-radius:12px;background:var(--btn);color:var(--btnt);font-weight:500;box-shadow:0 10px 26px rgba(6,26,61,.22);transition:transform .2s}
.btn:hover{transform:translateY(-2px)}.btn.o{background:transparent;color:var(--ink);border:2px solid var(--ink);box-shadow:none}
.ph{justify-self:center;position:relative;width:100%;max-width:410px}
.ph img{display:block;width:100%;aspect-ratio:3/4;object-fit:cover;border-radius:32px;border:4px solid #fff;box-shadow:0 28px 64px rgba(6,26,61,.3)}
.badge{position:absolute;left:-26px;bottom:34px;background:var(--card);border:1px solid var(--line);border-radius:16px;padding:14px 18px;box-shadow:0 14px 34px rgba(6,26,61,.18);font-size:13.5px;line-height:1.35}
.badge b{display:block;font-family:Newsreader,serif;font-size:21px;font-weight:600;color:var(--blue)}
.dots{position:absolute;width:92px;height:92px;background-image:radial-gradient(var(--blue) 1.6px,transparent 1.8px);background-size:18px 18px;opacity:.45;z-index:1}
.stats{background:var(--card);border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
.stats .w{display:grid;grid-template-columns:repeat(4,1fr)}
.st{padding:30px 22px;border-right:1px solid var(--line)}.st:last-child{border:0}
.st b{display:block;font-family:Newsreader,serif;font-size:36px;font-weight:500;color:var(--blue);line-height:1.1}
.st span{font-size:14px;color:var(--muted)}
.band{background:var(--navy);color:#fff;padding:64px 0 70px}
.band h3{text-align:center;font-family:Inter,sans-serif;font-size:14px;letter-spacing:5px;color:#7fb2ea;font-weight:500;margin-bottom:40px}
.ig{display:grid;grid-template-columns:repeat(4,1fr)}
.it{text-align:center;padding:6px 18px;border-right:1px solid #1d4478;font-size:19px;line-height:1.4}.it:last-child{border:0}
.ic{width:92px;height:92px;border:1.5px solid #2f6fb5;border-radius:50%;margin:0 auto 20px;display:grid;place-items:center}
.ic svg{width:46px;height:46px;stroke:#9cc4f0;fill:none;stroke-width:1.6;stroke-linecap:round;stroke-linejoin:round}
.ph2{position:relative;overflow:hidden;padding:86px 0 54px}
.ph2 h2{font-size:clamp(40px,5.5vw,64px);margin-bottom:14px;position:relative;z-index:2}
.ph2 p{color:var(--muted);font-size:19px;max-width:620px;margin:0;position:relative;z-index:2}
.sec{padding:20px 0 96px}
.card{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:32px 34px;box-shadow:0 10px 30px rgba(6,26,61,.06)}
.num{font-size:12.5px;letter-spacing:2.4px;color:var(--blue);font-weight:600;text-transform:uppercase;margin-bottom:10px}
.card h4{font-size:27px;margin-bottom:8px;line-height:1.25}.m{color:var(--muted)}
.tl{position:relative;padding-left:40px;display:grid;gap:22px}
.tl::before{content:"";position:absolute;left:9px;top:12px;bottom:12px;width:2px;background:linear-gradient(var(--blue),var(--line))}
.tl .card{position:relative}
.tl .card::before{content:"";position:absolute;left:-40px;top:40px;width:18px;height:18px;border-radius:50%;background:var(--bg);border:4px solid var(--blue)}
.sc{font-family:Newsreader,serif;font-size:40px;margin-top:10px;color:var(--blue);font-weight:500;line-height:1}
.ms{background:var(--navy);color:#fff;border-radius:22px;padding:32px 34px;position:relative;overflow:hidden}
.ms::before{content:"";position:absolute;left:-40px;top:40px;width:18px;height:18px;border-radius:50%;background:#2f6fb5;border:4px solid var(--bg)}
.ms .num{color:#7fb2ea}.ms h4{font-size:30px;color:#fff;margin-bottom:6px}.ms .m{color:#c4d6ec}
.tag{display:inline-block;background:var(--sky);color:var(--blue);font-size:12px;letter-spacing:1.4px;font-weight:600;padding:6px 14px;border-radius:30px;text-transform:uppercase;margin-bottom:14px}
.proj{display:grid;grid-template-columns:1fr 240px;gap:34px;align-items:center;margin-bottom:24px}
.topic{border-left:3px solid var(--blue);padding-left:16px;margin:14px 0;font:500 20px/1.4 Newsreader,serif}
.two{display:grid;grid-template-columns:1fr 1fr;gap:24px}
.chips{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
.chip{border:1px solid var(--line);background:var(--bg);padding:10px 18px;border-radius:40px;font-size:15px}
.chip.d{background:var(--navy);color:#fff;border-color:var(--navy)}
dl{margin:0;display:grid;grid-template-columns:130px 1fr;gap:12px 14px}dt{color:var(--blue);font-weight:600;font-size:13px;letter-spacing:1.4px;text-transform:uppercase;padding-top:3px}dd{margin:0}
.ct{background:var(--navy);color:#fff;border-radius:26px;padding:46px;margin-top:24px;position:relative;overflow:hidden}
.ct h3{font-size:38px;margin-bottom:12px}.ct p{color:#c4d6ec;max-width:620px;margin:0 0 28px}
.cr{display:grid;grid-template-columns:repeat(2,1fr);gap:22px}
.cr a{display:block;background:rgba(255,255,255,.07);border:1px solid #1d4478;border-radius:16px;padding:18px 20px;transition:background .2s}
.cr a:hover{background:rgba(255,255,255,.14)}
.cr small{display:block;letter-spacing:2px;color:#7fb2ea;font-size:11.5px;margin-bottom:4px}.cr span{font-size:16px;word-break:break-all}
.sitefoot{background:var(--navy);color:#8ea6c9;text-align:center;padding:26px;font-size:14px}
@media(max-width:860px){.w{padding:0 20px}.hg{grid-template-columns:1fr;padding:48px 0;gap:40px}.ph{order:-1;max-width:320px}.badge{left:8px}
.ig{grid-template-columns:1fr 1fr}.cr,.two{grid-template-columns:1fr}.proj{grid-template-columns:1fr}.proj svg{max-width:200px}
.it{border:0;margin-bottom:18px}.st:nth-child(2){border-right:0}.nav{gap:18px}.tl .card{flex-direction:column;align-items:flex-start}dl{grid-template-columns:1fr}.ct{padding:30px 24px}}
.stApp{background:var(--bg);color:var(--ink);font:16px/1.65 Inter,system-ui,sans-serif;}
header[data-testid="stHeader"],[data-testid="stToolbar"],[data-testid="stDecoration"],#MainMenu,footer{display:none!important;}
.block-container{padding:0!important;max-width:100%!important;}
[data-testid="stVerticalBlock"]{gap:0!important;}
[data-testid="stMarkdownContainer"]{font-family:Inter,system-ui,sans-serif;}
.stApp h1,.stApp h2,.stApp h3,.stApp h4{font-family:Newsreader,Georgia,serif;font-weight:500;color:var(--ink);padding:0;margin-top:0;line-height:1.1;letter-spacing:normal;}
.stApp .hero h1{letter-spacing:-1.5px;}
.stApp .ct h3,.stApp .ms h4{color:#fff;}
.stApp h1 a,.stApp h2 a,.stApp h3 a,.stApp h4 a{display:none!important;}
.stDownloadButton{max-width:1160px;margin:0 auto;padding:26px 32px 60px;}
.stDownloadButton button{background:var(--btn)!important;color:var(--btnt)!important;border:none!important;border-radius:12px!important;padding:14px 28px!important;font-weight:500!important;}
.stDownloadButton button:hover{filter:brightness(1.2);}
@media(max-width:860px){.stDownloadButton{padding:20px 20px 40px;}}

</style>"""

# Shared SVG gradients / marble filter used by the wave artwork
DEFS = r"""<div style="height:0;overflow:hidden"><svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<filter id="mb" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency="0.011" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="46"/></filter>
<linearGradient id="gd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#021033"/><stop offset="1" stop-color="#0b3a7a"/></linearGradient>
<linearGradient id="gm" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1c5fa8"/><stop offset="1" stop-color="#5b9ad8"/></linearGradient>
<linearGradient id="gl" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#a9cdef"/><stop offset="1" stop-color="#e3eefa"/></linearGradient></defs></svg></div>"""

# ----------------------------------------------------------------------------
# PAGE CONTENT
# ----------------------------------------------------------------------------
HOME = r"""
<div class="hero"><svg class="waves" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<circle cx="1330" cy="90" r="210" fill="#2563a8" opacity=".12"/><circle cx="640" cy="780" r="200" fill="#2563a8" opacity=".1"/>
<g class="drift" filter="url(#mb)"><path d="M-60,-40 L470,-40 C430,60 330,110 360,210 C390,300 270,330 200,300 C130,275 110,380 -60,470Z" fill="url(#gl)"/><path d="M-60,-40 L330,-40 C300,60 220,100 240,190 C255,260 170,280 110,250 C60,230 40,300 -60,360Z" fill="url(#gm)"/><path d="M-60,-40 L190,-40 C170,40 110,70 120,140 C130,200 70,210 20,190 C-10,180 -30,220 -60,250Z" fill="url(#gd)"/>
<path d="M1500,150 C1380,170 1340,260 1380,340 C1420,420 1360,520 1500,600Z" fill="url(#gl)"/><path d="M1500,260 C1420,280 1400,350 1430,420 C1460,490 1420,560 1500,640Z" fill="url(#gm)"/>
<path d="M700,1000 L700,900 C760,800 880,820 960,760 C1060,690 1180,780 1300,700 C1380,650 1450,640 1500,600 L1500,1000Z" fill="url(#gl)"/><path d="M860,1000 L860,900 C920,830 1000,840 1080,800 C1180,750 1260,820 1380,760 C1430,735 1470,725 1500,700 L1500,1000Z" fill="url(#gm)"/><path d="M1040,1000 L1040,900 C1100,860 1180,870 1260,845 C1340,820 1420,850 1500,820 L1500,1000Z" fill="url(#gd)"/></g></svg>
<div class="dots" style="top:70px;right:27%"></div><div class="dots" style="bottom:60px;left:42%"></div>
<div class="w"><div class="hg"><div>
<h1>Indhulekha M.</h1><div class="rule"></div>
<p class="lead">Economics postgraduate interested in how markets, institutions and policy shape business decisions. I turn economic perspectives into meaningful insights through research, data and clear thinking.</p>
<div class="btns"><a class="btn" href="?page=research" target="_self">Explore my work <span>→</span></a><a class="btn o" href="?page=about" target="_self">Get in touch</a></div></div>
<div class="ph"><img alt="Portrait of Indhulekha M." src="__PORTRAIT__"></div></div></div></div>
<div class="band"><div class="w"><h3>AREAS OF INTEREST</h3><div class="ig">
<div class="it"><div class="ic"><svg viewBox="0 0 48 48"><path d="M6 42V30h7v12M18 42V22h7v20M30 42V26h7v16M6 22l10-8 8 6 14-12"/><path d="M31 8h7v7"/></svg></div>Financial<br>Markets</div>
<div class="it"><div class="ic"><svg viewBox="0 0 48 48"><circle cx="24" cy="24" r="18"/><ellipse cx="24" cy="24" rx="8" ry="18"/><path d="M6 24h36M9 14h30M9 34h30"/></svg></div>International<br>Economics</div>
<div class="it"><div class="ic"><svg viewBox="0 0 48 48"><path d="M8 6v34h34"/><circle cx="18" cy="28" r="1.5"/><circle cx="24" cy="21" r="1.5"/><circle cx="30" cy="30" r="1.5"/><circle cx="36" cy="18" r="1.5"/></svg></div>Econometrics</div>
<div class="it"><div class="ic"><svg viewBox="0 0 48 48"><path d="M6 18L24 7l18 11H6zM10 40h28M8 44h32M12 22v14M20 22v14M28 22v14M36 22v14"/></svg></div>Economic<br>Policy</div></div></div></div>
"""

ACADEMICS = r"""
<div class="ph2"><svg class="waves" viewBox="0 0 1440 420" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><g class="drift" filter="url(#mb)"><path d="M-60,-40 L360,-40 C320,50 240,90 260,170 C280,230 190,250 120,220 C70,200 40,270 -60,320Z" fill="url(#gl)"/><path d="M-60,-40 L220,-40 C190,40 130,70 140,130 C150,180 80,190 30,170 C0,160 -30,190 -60,210Z" fill="url(#gm)"/><path d="M1500,-40 C1400,40 1360,130 1400,210 C1440,290 1380,360 1500,420Z" fill="url(#gl)"/></g></svg>
<div class="w"><div class="eyebrow" style="position:relative;z-index:2;margin-left:max(0px,0px);padding-top:40px">02 / Academic Journey</div><h2>Learning that shapes perspective.</h2><p>A journey through economics, academic achievement and continuous learning.</p></div></div>
<div class="sec"><div class="w"><div class="tl">
<div class="card"><div><div class="num">01 — Current studies</div><h4>M.A. Economics</h4><div class="m">CMS College (Autonomous), Kottayam · 2025–2027</div><div class="sc" style="font-size:24px;padding-top:14px">Ongoing</div></div></div>
<div class="ms"><div class="num">Academic milestone</div><h4>UGC-NET — Economics</h4><div class="m">Qualified for Ph.D. admission in Economics · June 2026</div></div>
<div class="card"><div><div class="num">02 — Undergraduate</div><h4>B.A. Economics</h4><div class="m">Baselius College · 2021–2024</div><div class="sc">Score: 81%</div></div></div>
</div></div></div>
"""

RESEARCH = r"""
<div class="ph2"><svg class="waves" viewBox="0 0 1440 420" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><g class="drift" filter="url(#mb)"><path d="M-60,-40 L360,-40 C320,50 240,90 260,170 C280,230 190,250 120,220 C70,200 40,270 -60,320Z" fill="url(#gl)"/><path d="M1500,-40 C1400,40 1360,130 1400,210 C1440,290 1380,360 1500,420Z" fill="url(#gl)"/></g></svg>
<div class="w"><div class="eyebrow" style="position:relative;z-index:2;padding-top:40px">03 / Research &amp; Projects</div><h2>Questions worth investigating.</h2><p>Research experience, a national conference paper and an undergraduate project.</p></div></div>
<div class="sec"><div class="w">
<div class="card proj"><div><span class="tag">Research internship</span><h4>Gokhale Institute of Politics and Economics (GIPE), Pune</h4><div class="m">May–June 2026 · 120 hours</div>
<div class="topic">From Global Integration to Digital Enclaves: Data Localisation and the Changing Landscape of Financial Services Trade</div>
<p class="m" style="margin:0">A comparative study of data localisation and its implications for financial services trade, examining India, China and Turkey through regulatory developments and economic concepts.</p></div>
<svg viewBox="0 0 260 150" width="100%" aria-hidden="true"><path d="M10 120 L50 95 L90 105 L130 60 L170 75 L210 30 L250 40 L250 140 L10 140Z" fill="var(--sky)"/><path d="M10 120 L50 95 L90 105 L130 60 L170 75 L210 30 L250 40" fill="none" stroke="var(--blue)" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
<div class="card proj"><div><span class="tag">Paper presentation</span><h4>Domestic Investors and the Resilience of the Indian Stock Market over the Past Decade</h4><div class="m">National Research Conclave, St. Teresa’s College · August 2026</div>
<p class="m" style="margin:14px 0 0">Research examining the relationship between domestic and foreign institutional investor flows, Nifty 50 returns and India VIX, using monthly data from 2016–2026.</p></div>
<svg viewBox="0 0 260 150" width="100%" aria-hidden="true"><rect x="20" y="100" width="24" height="40" rx="4" fill="#a9cdef"/><rect x="58" y="70" width="24" height="70" rx="4" fill="#5b9ad8"/><rect x="96" y="85" width="24" height="55" rx="4" fill="#2f6fb5"/><rect x="134" y="40" width="24" height="100" rx="4" fill="#0a2a5c"/><rect x="172" y="55" width="24" height="85" rx="4" fill="#2f6fb5"/></svg></div>
<div class="card proj"><div><span class="tag">Undergraduate project</span><h4>Role of MSMEs in Reducing the Problem of Unemployment</h4>
<p class="m" style="margin:14px 0 0">An economics project examining the contribution of micro, small and medium enterprises to employment generation, economic growth and unemployment reduction.</p></div>
<svg viewBox="0 0 260 150" width="100%" aria-hidden="true"><circle cx="130" cy="75" r="55" fill="none" stroke="var(--sky)" stroke-width="22"/><circle cx="130" cy="75" r="55" fill="none" stroke="#2f6fb5" stroke-width="22" stroke-dasharray="210 346" transform="rotate(-90 130 75)"/></svg></div>
</div></div>
"""

SKILLS = r"""
<div class="ph2"><svg class="waves" viewBox="0 0 1440 420" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><g class="drift" filter="url(#mb)"><path d="M-60,-40 L360,-40 C320,50 240,90 260,170 C280,230 190,250 120,220 C70,200 40,270 -60,320Z" fill="url(#gl)"/><path d="M1500,-40 C1400,40 1360,130 1400,210 C1440,290 1380,360 1500,420Z" fill="url(#gl)"/></g></svg>
<div class="w"><div class="eyebrow" style="position:relative;z-index:2;padding-top:40px">04 / Skills</div><h2>Tools for research, skills for analysis.</h2><p>The technical and analytical toolkit I bring to research and business questions.</p></div></div>
<div class="sec"><div class="w"><div class="two">
<div class="card"><div class="num">Technical tools</div><h4>Software &amp; programming</h4><div class="chips"><span class="chip d">SPSS</span><span class="chip d">Stata</span><span class="chip d">EViews</span><span class="chip d">Python</span><span class="chip d">LaTeX</span><span class="chip d">Microsoft Excel</span><span class="chip d">Microsoft Word</span><span class="chip d">Microsoft PowerPoint</span><span class="chip d">Canva</span></div></div>
<div class="card"><div class="num">Research &amp; analytical</div><h4>Ways of working</h4><div class="chips"><span class="chip">Research writing</span><span class="chip">Literature review</span><span class="chip">Policy analysis</span><span class="chip">Economic analysis</span><span class="chip">Data analysis</span></div></div></div>
</div></div>
"""

ABOUT = r"""
<div class="ph2"><svg class="waves" viewBox="0 0 1440 420" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><g class="drift" filter="url(#mb)"><path d="M-60,-40 L360,-40 C320,50 240,90 260,170 C280,230 190,250 120,220 C70,200 40,270 -60,320Z" fill="url(#gl)"/><path d="M1500,-40 C1400,40 1360,130 1400,210 C1440,290 1380,360 1500,420Z" fill="url(#gl)"/><path d="M1500,40 C1440,80 1420,150 1450,210 C1470,260 1440,310 1500,350Z" fill="url(#gm)"/></g></svg>
<div class="w"><div class="eyebrow" style="position:relative;z-index:2;padding-top:40px">05 / About &amp; Contact</div><h2>Curious, analytical, collaborative.</h2><p>A little about me, and how to reach me.</p></div></div>
<div class="sec"><div class="w"><div class="two">
<div class="card"><div class="num">About me</div><h4>Learning through ideas</h4><p class="m">I enjoy exploring unfamiliar ideas, analysing information and understanding different perspectives. I value continuous learning, meaningful collaboration and the process of turning knowledge into practical insights.</p><p class="m">I aspire to contribute meaningfully to an organisation while growing as a professional and creating value through knowledge, initiative and collaboration.</p></div>
<div class="card"><div class="num">Personal information</div><h4>At a glance</h4><dl><dt>Name</dt><dd>Indhulekha M.</dd><dt>Age</dt><dd>23</dd><dt>Qualification</dt><dd>M.A. Economics (ongoing)</dd><dt>Location</dt><dd>Kerala, India</dd></dl></div>
<div class="card" style="grid-column:1/-1"><div class="num">Research interests</div><h4>Where my curiosity lies</h4><div class="chips"><span class="chip">Financial Markets</span><span class="chip">International Economics</span><span class="chip">Econometrics</span><span class="chip">Economic Policy</span></div></div>
<div class="card" style="grid-column:1/-1"><div class="num">Leadership &amp; extra-curricular</div><h4>Beyond the classroom</h4><dl style="margin-top:16px"><dt>2023 – 2024</dt><dd>College Union Vice Chairperson</dd><dt>2022 – 2023</dt><dd>College Union Lady Representative</dd><dt>2019 – 2023</dt><dd>NSS Volunteer</dd><dt>Interests</dt><dd>Book Reviewer</dd></dl></div>
<div class="card"><div class="num">Personal skills</div><h4>Strengths</h4><div class="chips"><span class="chip">Communication</span><span class="chip">Analytical thinking</span><span class="chip">Leadership</span><span class="chip">Problem solving</span><span class="chip">Time management</span><span class="chip">Teamwork</span><span class="chip">Attention to detail</span><span class="chip">Writing</span></div></div>
<div class="card"><div class="num">Languages</div><h4>Languages known</h4><dl style="margin-top:16px"><dt>English</dt><dd>Fluent</dd><dt>Malayalam</dt><dd>Native</dd><dt>Hindi</dt><dd>Basic</dd><dt>Tamil</dt><dd>Basic</dd></dl></div>
</div>
<div class="ct"><h3>Let’s start a conversation.</h3><p>I’m open to opportunities that allow me to apply my knowledge of economics, contribute to meaningful work and continue growing professionally.</p>
<div class="cr"><a href="mailto:indhulekham03@gmail.com"><small>EMAIL</small><span>indhulekham03@gmail.com</span></a><a href="https://www.linkedin.com/in/indhulekha-m-1157a0272" target="_blank" rel="noopener"><small>LINKEDIN</small><span>Indhulekha M. — LinkedIn</span></a></div></div>
</div></div>
"""

FOOTER = '<div class="sitefoot">© 2026 Indhulekha M. · Economics · Research · Data Analysis</div>'


# ----------------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------------
def html(s: str):
    """Render HTML in Streamlit (strip indentation and blank lines so markdown leaves it alone)."""
    st.markdown("\n".join(l.strip() for l in s.splitlines() if l.strip()), unsafe_allow_html=True)


def portrait_src() -> str:
    if PHOTO.exists():
        mime = "image/png" if PHOTO.suffix.lower() == ".png" else "image/jpeg"
        return f"data:{mime};base64," + base64.b64encode(PHOTO.read_bytes()).decode()
    # neutral placeholder if no photo found yet
    svg = ("<svg xmlns='http://www.w3.org/2000/svg' width='420' height='560'><rect width='100%' height='100%' fill='#e6edf5'/>"
           "<text x='50%' y='50%' text-anchor='middle' fill='#6b7c96' font-family='sans-serif' font-size='18'>Add profile.jpg next to app.py</text></svg>")
    return "data:image/svg+xml;base64," + base64.b64encode(svg.encode()).decode()


def topbar(active: str):
    links = "".join(
        f'<a href="?page={k}" target="_self" class="{"on" if k == active else ""}">{v}</a>'
        for k, v in PAGES.items()
    )
    html(f"""<div class="topbar"><div class="w">
    <a class="brand" href="?page=home" target="_self"><b>INDHULEKHA M.</b><span>Economics Postgraduate</span></a>
    <div class="nav">{links}</div></div></div>""")


def cv_button(key: str):
    if CV.exists():
        st.download_button("Download my CV (PDF)", CV.read_bytes(),
                           file_name="Indhulekha_CV.pdf", mime="application/pdf", key=key)
    else:
        st.caption("Add your resume as Indhulekha_CV.pdf next to app.py to enable the CV download.")


# ----------------------------------------------------------------------------
# ROUTER
# ----------------------------------------------------------------------------
html(CSS)
html(DEFS)

page = st.query_params.get("page", "home")
if page not in PAGES:
    page = "home"
topbar(page)

if page == "home":
    html(HOME.replace("__PORTRAIT__", portrait_src()))
    cv_button("cv_home")
elif page == "academics":
    html(ACADEMICS)
elif page == "research":
    html(RESEARCH)
elif page == "skills":
    html(SKILLS)
else:
    html(ABOUT)
    cv_button("cv_about")

html(FOOTER)
