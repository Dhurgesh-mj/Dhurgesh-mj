import html

# ================= EDIT ME =================
NAME = "DHURGESH MJ"
TAGLINE = "WRITTEN · DIRECTED · EXPLOITED BY"
BAR_TOP = "A FILM BY NOBODY ELSE"
BAR_BOTTOM = "NO SYSTEMS WERE HARMED IN THE MAKING OF THIS PROFILE (SOME WERE POPPED)"
PROJECTS = [  # title, tagline, genre, rating, hue
  ("SUBDOMINATOR V2", "Every subdomain. Found before it finishes loading.", "THRILLER · 2025", "9.8", "#f5b971"),
  ("SHINOBIJS",       "Reads your JavaScript. Leaves no trace.",          "NOIR · 2025",    "9.6", "#6fa8dc"),
  ("QUANTUMVAULT",    "Encrypted. Layered. Not your files anymore.",      "SCI-FI · 2026",  "9.9", "#c9707f"),
]
CREDITS = [
  ("STARRING", [("LANGUAGES","Python · C · C++ · PHP"),("RECON & WEB","Subdomain Enum · LFI · JS Recon"),("OFFENSIVE","Process Injection · Malware Dev")]),
  ("SPECIAL EFFECTS", [("PLATFORMS","Kali Linux · Ubuntu"),("CRYPTO","Multi-layer Encryption"),("ASYNC ENGINE","Python asyncio, built for speed")]),
  ("STUNTS PERFORMED BY", [("BUG BOUNTY HUNTS","Himself"),("AUTH BYPASSES","Himself"),("3 AM RECON RUNS","Himself")]),
]
# ===========================================
INK="#f1ede4"; DIM="#8a8f9c"; GOLD="#f5b971"; BG="#07080c"
SERIF="Georgia,'Times New Roman',serif"; SANS="'Helvetica Neue',Helvetica,Arial,sans-serif"
e=html.escape
def save(n,s): open(f"assets/{n}.svg","w",encoding="utf-8").write(s)

# ---------- HERO ----------
W,H=900,420
hero=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="55"/></filter>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch" seed="1"><animate attributeName="seed" values="1;2;3;4;5;6" dur=".5s" calcMode="discrete" repeatCount="indefinite"/></feTurbulence><feColorMatrix values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .55 0"/></filter>
<radialGradient id="vig" cx="50%" cy="50%" r="75%"><stop offset=".45" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".85"/></radialGradient>
</defs>
<style>
.o1{{animation:d1 16s ease-in-out infinite alternate}} .o2{{animation:d2 20s ease-in-out infinite alternate}} .o3{{animation:d3 13s ease-in-out infinite alternate}}
@keyframes d1{{to{{transform:translate(260px,40px)}}}} @keyframes d2{{to{{transform:translate(-240px,-30px)}}}} @keyframes d3{{to{{transform:translate(120px,-60px) scale(1.4)}}}}
.title{{font:400 80px {SERIF};fill:{INK};text-anchor:middle;animation:rev 14s ease-out infinite}}
@keyframes rev{{0%{{opacity:0;letter-spacing:44px}}10%{{opacity:0}}38%{{opacity:1;letter-spacing:15px}}88%{{opacity:1;letter-spacing:15px}}100%{{opacity:0;letter-spacing:15px}}}}
.sub{{font:11px {SANS};fill:{INK};letter-spacing:7px;text-anchor:middle;animation:sub 14s ease-out infinite}}
@keyframes sub{{0%,30%{{opacity:0}}48%,86%{{opacity:.75}}100%{{opacity:0}}}}
.ln{{fill:{GOLD};transform-box:fill-box;transform-origin:center;animation:ln 14s ease-in-out infinite}}
@keyframes ln{{0%,22%{{transform:scaleX(0);opacity:1}}45%,86%{{transform:scaleX(1);opacity:1}}100%{{transform:scaleX(1);opacity:0}}}}
.bar{{font:9px {SANS};fill:{DIM};letter-spacing:4px}}
</style>
<rect width="{W}" height="{H}" fill="{BG}"/>
<g filter="url(#blur)">
<circle class="o1" cx="170" cy="190" r="110" fill="{GOLD}" opacity=".38"/>
<circle class="o2" cx="720" cy="230" r="140" fill="#2c4f86" opacity=".6"/>
<circle class="o3" cx="450" cy="300" r="70" fill="#b5566b" opacity=".35"/>
</g>
<rect width="{W}" height="{H}" fill="url(#vig)"/>
<rect width="{W}" height="{H}" filter="url(#grain)" opacity=".09"/>
<text class="title" x="{W/2+7}" y="222">{NAME}</text>
<rect class="ln" x="330" y="248" width="240" height="1.5"/>
<text class="sub" x="{W/2+3}" y="282">{e(TAGLINE)}</text>
<rect width="{W}" height="46" fill="#000"/><rect y="{H-46}" width="{W}" height="46" fill="#000"/>
<text class="bar" x="28" y="28">{e(BAR_TOP)}</text>
<text class="bar" x="{W-28}" y="28" text-anchor="end">2026 · 2.39:1</text>
<text class="bar" x="{W/2}" y="{H-18}" text-anchor="middle">{e(BAR_BOTTOM)}</text>
</svg>'''
save("hero",hero)

# ---------- LABELS ----------
def label(name,text):
    save(name,f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="70" viewBox="0 0 900 70">
<style>.l{{font:12px {SANS};fill:{GOLD};letter-spacing:10px;text-anchor:middle}}.g{{stroke:{DIM};stroke-opacity:.35}}</style>
<line class="g" x1="60" y1="35" x2="320" y2="35"/><line class="g" x1="580" y1="35" x2="840" y2="35"/>
<text class="l" x="455" y="39">{e(text)}</text>
<circle r="2" cy="35" fill="{GOLD}"><animate attributeName="cx" values="60;320;60" dur="7s" repeatCount="indefinite"/></circle>
<circle r="2" cy="35" fill="{GOLD}"><animate attributeName="cx" values="840;580;840" dur="7s" repeatCount="indefinite"/></circle>
</svg>''')
for n,t in [("l_showing","NOW SHOWING"),("l_credits","END CREDITS"),("l_city","THE CITY")]: label(n,t)

# ---------- POSTERS ----------
cards=""
for i,(t,tag,genre,rate,hue) in enumerate(PROJECTS):
    x=30+i*285
    cards+=f'''<g transform="translate({x},20)">
<clipPath id="c{i}"><rect width="270" height="330" rx="6"/></clipPath>
<g clip-path="url(#c{i})">
<rect width="270" height="330" fill="#0c0e15"/>
<g filter="url(#pb)"><circle cx="135" cy="120" r="70" fill="{hue}" opacity=".55"><animate attributeName="cx" values="90;180;90" dur="{9+i*3}s" repeatCount="indefinite"/><animate attributeName="cy" values="100;150;100" dur="{11+i*2}s" repeatCount="indefinite"/></circle></g>
<rect width="270" height="330" fill="url(#pf)"/>
<text x="135" y="212" text-anchor="middle" font-family="{SERIF}" font-size="26" letter-spacing="4" fill="{INK}">{e(t)}</text>
<line x1="105" x2="165" y1="228" y2="228" stroke="{hue}"/>
<text x="135" y="252" text-anchor="middle" font-family="{SERIF}" font-style="italic" font-size="13" fill="{INK}" opacity=".75">{e(tag)}</text>
<text x="135" y="300" text-anchor="middle" font-family="{SANS}" font-size="9" letter-spacing="4" fill="{DIM}">{e(genre)}</text>
<text x="135" y="318" text-anchor="middle" font-family="{SANS}" font-size="10" letter-spacing="3" fill="{hue}">★ {rate}</text>
</g><rect width="270" height="330" rx="6" fill="none" stroke="{hue}" stroke-opacity=".35"/></g>'''
save("posters",f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="370" viewBox="0 0 900 370">
<defs><filter id="pb" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="30"/></filter>
<linearGradient id="pf" x1="0" y1="0" x2="0" y2="1"><stop offset=".35" stop-color="#0c0e15" stop-opacity="0"/><stop offset=".7" stop-color="#0c0e15" stop-opacity=".95"/></linearGradient></defs>
{cards}</svg>''')

# ---------- CREDITS ROLL ----------
y=40; rows=""
for head,items in CREDITS:
    rows+=f'<text class="h" x="450" y="{y}">{e(head)}</text>'; y+=36
    for r,n in items:
        rows+=f'<text class="r" x="430" y="{y}">{e(r)}</text><text class="n" x="470" y="{y}">{e(n)}</text>'; y+=30
    y+=44
rows+=f'<text class="end" x="450" y="{y+10}">{NAME}</text><text class="r2" x="450" y="{y+40}">THANKS FOR WATCHING</text>'
total=y+120
save("credits",f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="420" viewBox="0 0 900 420">
<defs><linearGradient id="fg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".22" stop-color="#fff"/><stop offset=".78" stop-color="#fff"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<mask id="m"><rect width="900" height="420" fill="url(#fg)"/></mask></defs>
<style>
.h{{font:11px {SANS};fill:{GOLD};letter-spacing:8px;text-anchor:middle}}
.r{{font:11px {SANS};fill:{DIM};letter-spacing:3px;text-anchor:end}}
.n{{font:italic 17px {SERIF};fill:{INK}}}
.end{{font:400 40px {SERIF};fill:{INK};letter-spacing:14px;text-anchor:middle}}
.r2{{font:10px {SANS};fill:{DIM};letter-spacing:6px;text-anchor:middle}}
.roll{{animation:roll 26s linear infinite}}
@keyframes roll{{from{{transform:translateY(420px)}}to{{transform:translateY({-total}px)}}}}
</style>
<rect width="900" height="420" fill="{BG}"/>
<g mask="url(#m)"><g class="roll">{rows}</g></g>
<rect x=".5" y=".5" width="899" height="419" fill="none" stroke="{DIM}" stroke-opacity=".25"/>
</svg>''')

# ---------- THE END ----------
save("end",f'''<svg xmlns="http://www.w3.org/2000/svg" width="900" height="240" viewBox="0 0 900 240">
<defs><filter id="b" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="40"/></filter></defs>
<style>.e{{font:400 54px {SERIF};fill:{INK};letter-spacing:22px;text-anchor:middle;animation:f 8s ease-in-out infinite}}
@keyframes f{{0%{{opacity:0}}30%,75%{{opacity:1}}100%{{opacity:0}}}}
.s{{font:italic 14px {SERIF};fill:{DIM};text-anchor:middle}}</style>
<rect width="900" height="240" fill="{BG}"/>
<circle cx="450" cy="110" r="90" fill="{GOLD}" opacity=".22" filter="url(#b)"><animate attributeName="opacity" values=".1;.3;.1" dur="8s" repeatCount="indefinite"/></circle>
<text class="e" x="461" y="120">THE END</text>
<text class="s" x="450" y="175">No sequels planned. (There will be sequels.)</text>
</svg>''')
