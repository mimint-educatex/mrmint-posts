import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_reel import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))
TAG = "REFERENDARIAT"
RIGHT = W - M - 120  # rechte Inhaltskante

def card(d, y, text, col=LIGHT, font=None, fill=DG, lh=56):
    font = font or r(42)
    lines = wrap(d, text, font, MAXW - 80); h = len(lines)*lh + 50
    d.rounded_rectangle([M, y, RIGHT, y+h], radius=28, fill=col)
    yy = y + 25
    for l in lines: d.text((M+40, yy), l, font=font, fill=fill); yy += lh
    return y + h + 28

def minus_badge(d, y, text="1 Jahr weniger"):
    f = b(44); w = d.textlength(text, font=f) + 70
    d.rounded_rectangle([M, y, M+w, y+80], radius=40, fill=MINT)
    d.text((M+35, y+40), text, font=f, fill=WHITE, anchor="lm")
    return y + 110

def year_boxes(d, y, n_mint, labels=("Jahr 1", "Jahr 2", "Jahr 3")):
    gap = 24; bw = (RIGHT - M - 2*gap) / 3
    for i, lab in enumerate(labels):
        x0 = M + i*(bw+gap)
        if i < n_mint:
            d.rounded_rectangle([x0, y, x0+bw, y+130], radius=22, fill=MINT)
            d.text((x0+bw/2, y+65), lab, font=b(40), fill=WHITE, anchor="mm")
        else:
            d.rounded_rectangle([x0, y, x0+bw, y+130], radius=22, outline=MINT, width=6)
            d.text((x0+bw/2, y+65), lab, font=b(40), fill=MINT, anchor="mm")
    return y + 160

slides = []
def save(img, n):
    p = f"r{n}.png"; img.save(p); slides.append(p)

# 1 Hook
img, d = base(TAG)
y = block(d, 540, "Nur 1 Jahr", sb(104), DG, 124)
y = block(d, y, "Probezeit", sb(104), DG, 124)
y = block(d, y, "statt 3?", sb(104), MINT, 124)
y = block(d, y+60, "So verkürzt du deine Probezeit. Und so wird aus deinen Noten deine Leistungszahl.", r(46), GRAY, 64)
y = block(d, y+40, "Gilt für Baden-Württemberg.", b(40), MINT, 56)
save(img, 1)

# 2 Grundlagen
img, d = base(TAG)
y = block(d, 470, "Erst mal: Was ist die Probezeit?", sb(70), DG, 86) + 30
y = block(d, y, "Sie startet nach dem Ref, sobald du Beamter auf Probe wirst. Danach kommt die Verbeamtung auf Lebenszeit.", r(44), GRAY, 60) + 50
y = year_boxes(d, y, 3)
y = block(d, y+10, "Normal: 3 Jahre.", b(48), DG, 66)
y = block(d, y, "Minimum: 1 Jahr.", b(48), MINT, 66) + 20
y = block(d, y, "Dazwischen entscheiden zwei Hebel.", r(44), GRAY, 60)
save(img, 2)

# 3 Hebel 1
img, d = base(TAG)
d.text((M, 470), "Hebel 1", font=b(44), fill=MINT)
y = block(d, 530, "Deine Ref-Note", sb(84), DG, 100) + 20
y = minus_badge(d, y) + 10
y = block(d, y, "Bedingung: Note der Laufbahnprüfung (2. Staatsexamen) zwischen", r(44), GRAY, 60) + 10
d.text((M, y), "1,0 und 1,44", font=b(110), fill=MINT); y += 150
y = block(d, y, "Diese Note steht schon fest, wenn du an deiner Schule anfängst.", b(44), DG, 60)
save(img, 3)

# 4 Hebel 2
img, d = base(TAG)
d.text((M, 440), "Hebel 2", font=b(44), fill=MINT)
y = block(d, 500, "Deine Beurteilungen in der Probezeit", sb(68), DG, 82) + 20
y = minus_badge(d, y) + 10
y = block(d, y, "Die Schulleitung beurteilt dich zweimal. Beide Noten müssen 1,5 oder besser sein.", r(44), GRAY, 60) + 30
y = card(d, y, "1. Beurteilung: meist nach ca. 9 Monaten, auch ohne Besuch möglich.")
y = card(d, y, "2. Beurteilung: immer mit Unterrichtsbesuch.")
save(img, 4)

# 5 Kombination
img, d = base(TAG)
y = block(d, 450, "Was heißt das für dich?", sb(70), DG, 86) + 30
rows = [("Beide Hebel erfüllt", "1 Jahr", MINT), ("Ein Hebel erfüllt", "2 Jahre", MINT), ("Keiner erfüllt", "3 Jahre", DG)]
for lab, val, col in rows:
    d.rounded_rectangle([M, y, RIGHT, y+124], radius=26, fill=LIGHT)
    d.text((M+40, y+62), lab, font=r(44), fill=DG, anchor="lm")
    d.text((RIGHT-40, y+62), val, font=b(52), fill=col, anchor="rm")
    y += 150
y = block(d, y+10, "Gut zu wissen: Ist die 1. Beurteilung 1,5 oder besser, wird die 2. früher angesetzt.", r(42), GRAY, 58) + 20
y = block(d, y, "Ein Recht darauf gibt es nicht. Das Regierungspräsidium entscheidet.", b(42), DG, 58)
save(img, 5)

# 6 Anrechnungen
img, d = base(TAG)
y = block(d, 470, "Was noch zählt", sb(76), DG, 92) + 20
y = block(d, y, "Haben diese Zeiten deinen Weg ins Lehramt verzögert, können sie angerechnet werden:", r(42), GRAY, 58) + 30
for t in ["Wehrdienst, Zivildienst, FSJ, FÖJ, BFD", "Elternzeit oder Pflege von Angehörigen", "Eigener Unterricht in deinen Fächern, z. B. Vertretungsvertrag"]:
    y = card(d, y, t, font=r(40), lh=52)
y = block(d, y+10, "Höchstens 2 Jahre. Das RP prüft jeden Fall.", b(42), MINT, 58)
save(img, 6)

# 7 Leistungszahl Formel
img, d = base(TAG)
y = block(d, 470, "Und die Leistungszahl?", sb(72), DG, 88) + 20
y = block(d, y, "Nach dieser Zahl wird die Rangliste für die Einstellung gebildet.", r(44), GRAY, 60) + 40
for fac, lab in [("10 ×", "Bachelornote"), ("+ 10 ×", "Masternote"), ("+ 20 ×", "Ref-Note")]:
    d.text((M, y), fac, font=b(70), fill=MINT)
    d.text((M+310, y+12), lab, font=b(56), fill=DG)
    y += 105
y = block(d, y+30, "Kleiner ist besser.", b(52), MINT, 70)
y = block(d, y, "Bestwert: 40", b(52), MINT, 70) + 30
y = block(d, y, "Mit altem Staatsexamen: 20 × Note des ersten plus 20 × Note des zweiten Staatsexamens.", r(40), GRAY, 56)
save(img, 7)

# 8 Beispiel
img, d = base(TAG)
y = block(d, 470, "Ein Beispiel", sb(76), DG, 92) + 40
for lab, calc, res in [("Bachelor 2,0", "10 × 2,0", "20"), ("Master 1,6", "10 × 1,6", "16"), ("Ref 1,8", "20 × 1,8", "36")]:
    d.text((M, y), lab, font=r(46), fill=GRAY)
    d.text((M+360, y), calc, font=r(46), fill=GRAY)
    d.text((RIGHT, y), res, font=b(52), fill=DG, anchor="ra")
    y += 90
d.line([(M, y+5), (RIGHT, y+5)], fill=MINT, width=6); y += 30
d.text((M, y), "Leistungszahl", font=b(52), fill=DG)
d.text((RIGHT, y-20), "72", font=b(96), fill=MINT, anchor="ra"); y += 130
y = card(d, y, "Die Ref-Note zählt so viel wie Bachelor und Master zusammen.")
y = block(d, y, "Wartezeit und Vertretungsverträge ändern die Zahl nicht.", b(42), DG, 58)
save(img, 8)

# 9 Merksatz
img, d = base(TAG)
y = block(d, 520, "Die Ref-Note zählt doppelt:", sb(72), DG, 88)
y = block(d, y, "für deinen Listenplatz und für deine Probezeit.", sb(72), MINT, 88) + 50
y = block(d, y, "Alle Angaben für Baden-Württemberg, Stand 2026. Im Einzelfall beim Regierungspräsidium nachfragen.", r(40), GRAY, 56) + 50
d.line([(M, y), (M+200, y)], fill=MINT, width=6); y += 40
y = block(d, y, "Unterrichtsmaterial für Mathe, Physik, Technik und IT: auf eduki unter MrMint", r(36), MINT, 50)
save(img, 9)

for p in slides:
    im = Image.open(p); px = im.load()
    # Inhalt unterhalb BOTTOM pruefen
    low = [yy for yy in range(BOTTOM, H) for xx in range(0, W, 8) if px[xx, yy] != WHITE]
    print(p, "UEBERLAUF ab y=%d" % low[0] if low else "ok")
contact_sheet(slides, sys.argv[1] if len(sys.argv) > 1 else "sheet.png")
