import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
from mrmint_material import *
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, "..", "tools")

# ===== MATERIAL-LOOK (wie Davides eduki-Titelblätter: Mochiy Pop One, Grau, weiße Karten mit schwarzem Rand) =====
from PIL import ImageFont
BG = (229, 229, 229)        # Grau der eduki-Titelblätter
INKB = (20, 20, 20)
PET = (44, 168, 158)        # Petrol nur als Akzent
LINE = 7                    # schwarzer Rand
MAX_Y = 1180
def MOCHIY(sz): return ImageFont.truetype(os.path.join(TOOLS, "MochiyPopOne-Regular.ttf"), sz)

def m_frame(P, mid, kind="Arbeitsblatt"):
    """Grau, große weiße Karte mit schwarzem Rand, unten eduki-Zeile mit ID, Seitenzahl oben rechts."""
    no = len(P.slides) + 1
    img = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(img)
    d.rounded_rectangle([30, 30, W - 30, 1225], radius=40, fill=(255, 255, 255), outline=INKB, width=LINE)
    d.text((W - 70, 50), f"{no}/{P.total}", font=BODY(24, "SemiBold"), fill=(120, 120, 120), anchor="ra")
    lg = LOGO_GREEN; l = lg.resize((96, int(lg.height * 96 / lg.width)), Image.LANCZOS)
    img.paste(l, (44, 1238 + (100 - l.height) // 2), l)
    d.text((W // 2 + 40, 1290), f"{kind} auf eduki (ID: {mid})", font=MOCHIY(34), fill=INKB, anchor="mm")
    return img, d

def m_titlebox(d, y, title, sub=None, size=58):
    """Titelbox mit schwarzem Rand, Titel in Mochiy Pop One zentriert (wie eduki-Titelblatt)."""
    check_text(title); lines = wrap(d, title, MOCHIY(size), W - 260)
    h = 50 + len(lines) * (size + 22) + (size // 2 + 30 if sub else 0) + 20
    d.rounded_rectangle([90, y, W - 90, y + h], radius=26, fill=(255, 255, 255), outline=INKB, width=5)
    yy = y + 40
    for l in lines: d.text((W // 2, yy), l, font=MOCHIY(size), fill=INKB, anchor="mt"); yy += size + 22
    if sub: check_text(sub); d.text((W // 2, yy + 6), sub, font=MOCHIY(size // 2), fill=PET, anchor="mt")
    return y + h

def m_bullets(d, x, y, items, size=34, w=None, gap=22):
    """Quadratische Bullets wie auf den Titelblättern, Inter Medium schwarz."""
    w = w or (W - 90 - x)
    for t in items:
        check_text(t); lines = wrap(d, t, BODY(size, "Medium"), w - 50)
        d.rectangle([x, y + size // 2 - 6, x + 16, y + size // 2 + 10], fill=PET)
        for i, l in enumerate(lines): d.text((x + 40, y + i * (size + 12)), l, font=BODY(size, "Medium"), fill=INKB)
        y += len(lines) * (size + 12) + gap
    return y

def m_page(path, w):
    """AB-Seite als Karte: grauer Rand statt Mint, leichteres Wasserzeichen (Cover soll ruhig und scharf wirken)."""
    shot = Image.open(path).convert("RGB"); shot = shot.crop(content_box(path))
    shot = shot.resize((w, int(shot.height * w / shot.width)), Image.LANCZOS)
    add_watermark(shot, (0, 0, shot.width, shot.height), font_size=26, spacing_x=300, spacing_y=150, opacity=38)
    card = Image.new("RGB", (shot.width + 6, shot.height + 6), (70, 70, 70)); card.paste(shot, (3, 3))
    return card

def m_done(P, img, y):
    if y > MAX_Y: raise LayoutError(f"Material-Slide {len(P.slides)+1}: Inhalt endet bei y={y}, erlaubt {MAX_Y}")
    P.slides.append((img, False))

def m_sticker(img, kind="material", size=190, pos=(W - 255, 960)):
    s = Image.open(os.path.join(TOOLS, "sticker", f"{kind}.png")).convert("RGBA")
    s = s.resize((size, size), Image.LANCZOS).rotate(-10, resample=Image.BICUBIC, expand=True)
    img.paste(s, pos, s)

def m_cover(P, title, sub, front, back, points, mid, sticker="material"):
    """Cover: Titelbox, AB GROSS und scharf links (300 dpi, gerade, 2. Seite dahinter), rechts Stichpunkte, Sticker unten rechts."""
    img, d = m_frame(P, mid)
    top = m_titlebox(d, 96, title, sub) + 40
    cw = 540; ch = int(cw * 1.414)
    if ch > MAX_Y - top: cw = int((MAX_Y - top) / 1.414); ch = int(cw * 1.414)
    stack_card(img, m_page(back, cw), (90 + cw // 2 + 40, top + ch // 2 + 2), 4)
    stack_card(img, m_page(front, cw), (80 + cw // 2, top + ch // 2 + 6), 0)
    d = ImageDraw.Draw(img)
    x = 90 + cw + 70
    yy = m_bullets(d, x, top + 40, points, size=34, w=W - 80 - x)
    m_sticker(img, sticker)
    m_done(P, img, max(yy, top + ch))

def m_text(P, title, items, mid, shot=None):
    """Inhaltsslide: Titelbox, Stichpunkte, optional ein lesbarer Ausschnitt darunter."""
    img, d = m_frame(P, mid)
    y = m_titlebox(d, 96, title, size=50) + 60
    y = m_bullets(d, 110, y, items, size=36, w=W - 220, gap=28)
    if shot:
        fr = paste_framed_image(img, shot, (110, y + 20, W - 110, MAX_Y - 10))
        y = fr[3]
    m_done(P, img, y)

def m_shots(P, title, shots, mid):
    img, d = m_frame(P, mid)
    y = m_titlebox(d, 96, title, size=50) + 50
    room = MAX_Y - y - 30 * (len(shots) - 1)
    for s in shots:
        fr = paste_framed_image(img, s, (110, y, W - 110, y + room // len(shots) - 10))
        y = fr[3] + 30
    m_done(P, img, y - 30)

def m_end(P, mid, solution=None):
    """Schluss: Like und Bewertung, kleiner Lösungsausschnitt (zeigt: Lösungen dabei), eduki-ID-Box."""
    img, d = m_frame(P, mid)
    y = 140
    for l in ["Gefällt dir", "das Material?"]:
        d.text((W // 2, y), l, font=MOCHIY(62), fill=INKB, anchor="mt"); y += 86
    y += 20
    for l in wrap(d, "Dann freu ich mich über ein Like und auf eduki über eine Bewertung.", BODY(34, "Medium"), W - 260):
        d.text((W // 2, y), l, font=BODY(34, "Medium"), fill=(80, 80, 80), anchor="mt"); y += 48
    y += 40
    if solution:
        d.text((W // 2, y), "Lösungen sind dabei", font=MOCHIY(32), fill=PET, anchor="mt"); y += 60
        fr = paste_framed_image(img, solution, (150, y, W - 150, y + 380)); y = fr[3] + 50
    d.rounded_rectangle([120, y, W - 120, y + 140], radius=26, fill=(255, 255, 255), outline=INKB, width=5)
    d.text((W // 2 - 20, y + 70), "eduki", font=HEAD(60), fill=PET, anchor="rm")
    d.line([(W // 2 + 10, y + 32), (W // 2 + 10, y + 108)], fill=INKB, width=4)
    d.text((W // 2 + 40, y + 70), f"ID: {mid}", font=MOCHIY(46), fill=INKB, anchor="lm")
    m_done(P, img, y + 140)

def m_reel(P, folder, sec=5.0):
    sys.path.insert(0, TOOLS); from mrmint_reel import render_video
    frames = []
    for i, (img, _) in enumerate(P.slides, 1):
        sc = 1250 / H; t = img.resize((int(W * sc), 1250), Image.LANCZOS)
        c = Image.new("RGB", (1080, 1920), BG); c.paste(t, ((1080 - t.width) // 2 - 30, 250))
        p = os.path.join(folder, f"reel_{i}.png"); c.save(p); frames.append(p)
    return render_video(frames, os.path.join(folder, "reel.mp4"), sec=sec)
# ===== Ende Material-Look =====

ID = "1723115"
P = Post(total=4, kicker_base="Material")
AB, LOE = os.path.join(HERE, "ab_hd.png"), os.path.join(HERE, "loesung_hd.png")
src = Image.open(os.path.join(HERE, "ab.png")).convert("RGB")
crops = {"_minus": (850, 330, 1585, 860), "_auf": (65, 1405, 1030, 1812)}
for k, c in crops.items(): src.crop(c).save(os.path.join(HERE, k + ".png"))
Image.open(os.path.join(HERE, "loesung.png")).convert("RGB").crop((70, 1420, 1125, 1830)).save(os.path.join(HERE, "_loes.png"))
LOES = os.path.join(HERE, "_loes.png")
MINUS, AUF = [os.path.join(HERE, k + ".png") for k in ("_minus", "_auf")]

m_cover(P, "Klammer auflösen", "Plus oder Minus davor?", AB, LOE,
        ["Regelkasten mit Beispielen", "17 Aufgaben, gestuft", "Klasse 7 und 8", "Mit Lösungen"], ID)
m_text(P, "Darum geht's", [
    "Regel: Plus davor, alles bleibt. Minus davor, alle Vorzeichen drehen sich um.",
    "Aufgabe 1: Zahlen markieren, Rechenzeichen einsetzen",
    "Aufgabe 2: ohne Klammer schreiben, dann rechnen",
    "Aufgabe 3: das Ganze mit Dezimalzahlen"], ID, shot=MINUS)
m_text(P, "So setzt du es ein", [
    "Direkt nach der Einführung zum Üben",
    "Die Hilfen nehmen von Aufgabe zu Aufgabe ab",
    "Mit dem Lösungsblatt kontrollieren die Schüler selbst",
    "Klappt auch als Hausaufgabe oder in der Vertretung"], ID, shot=AUF)
m_end(P, ID, solution=LOES)

P.save(HERE, prefix="kl")
if "--reel" in sys.argv: m_reel(P, HERE)
print("ok")
