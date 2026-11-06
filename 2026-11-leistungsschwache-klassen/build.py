import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_reel import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))
TAG = "SCHULALLTAG"
N = 7

def num(d, i):
    t = f"{i}/{N}"
    d.text((W-M-120, BOTTOM+20), t, font=b(30), fill=MINT, anchor="ra")

def pill(d, y, text, col=MINT, fg=WHITE, size=26):
    w = d.textlength(text, font=b(size)) + 44
    d.rounded_rectangle([M, y, M+w, y+size+28], radius=(size+28)//2, fill=col)
    d.text((M+22, y+14), text, font=b(size), fill=fg)
    return y + size + 28 + 30

def card(d, y, text, col=LIGHT, fg=DG, size=40, lh=54, bold=False):
    f = b(size) if bold else r(size)
    lines = wrap(d, text, f, MAXW-80); h = len(lines)*lh + 50
    d.rounded_rectangle([M, y, W-M-120, y+h], radius=28, fill=col)
    yy = y + 25
    for l in lines: d.text((M+40, yy), l, font=f, fill=fg); yy += lh
    return y + h + 28

def method(i, nr, name, problem, aber):
    img, d = base(TAG)
    y = pill(d, 470, f"METHODE {nr}")
    y = block(d, y, name, sb(66), DG, 80) + 30
    y = block(d, y, problem, r(44), GRAY, 60) + 40
    y = card(d, y, aber)
    num(d, i); img.save(f"r{i}.png")

# 1 Hook
img, d = base(TAG)
d.text((M, 450), "Aus meiner Erfahrung:", font=r(42), fill=GRAY)
y = block(d, 530, "3 Methoden,", sb(92), DG, 110)
y = block(d, y, "die in leistungs-", sb(70), DG, 90, mw=W-2*M)
y = block(d, y, "schwächeren Klassen", sb(70), DG, 90, mw=W-2*M)
y = block(d, y, "oft scheitern.", sb(92), MINT, 110)
y = block(d, y+50, "Nicht, weil die Methoden schlecht sind. Und nicht, weil du schlecht bist.", r(46), GRAY, 64)
num(d, 1); img.save("r1.png")

# 2 Stationenlernen
method(2, 1, "Stationenlernen mit freier Wahl",
       "Viele verlieren den Überblick, bleiben an der leichtesten Station hängen oder warten einfach ab.",
       "Kann klappen: mit Laufzettel, fester Reihenfolge und vielen Wochen Übung.")

# 3 Gruppenarbeit
method(3, 2, "Gruppenarbeit ohne feste Rollen",
       "Einer arbeitet, drei schauen zu. Oder alle reden, nur nicht über die Aufgabe.",
       "Kann klappen: mit Rollen wie Zeitwächter oder Schreiber, klarem Produkt und kleinen Gruppen. Muss aber lange eingeübt werden.")

# 4 Entdeckendes Lernen
method(4, 3, "„Finde die Regel selbst heraus“",
       "Wenn Grundlagen fehlen, wird Entdecken schnell zu Frust. Die Forschung zeigt:",
       "Wer wenig Vorwissen hat, lernt neuen Stoff mit klarer Anleitung meist besser als durch offenes Entdecken.")

# 5 Zwei Optionen
img, d = base(TAG)
y = pill(d, 470, "MEINE MEINUNG", col=DG)
y = block(d, y, "Nimmt die Klasse offene Lernwege nicht an, hast du 2 Optionen:", sb(58), DG, 74) + 40
y = card(d, y, "A: Lange einüben. Routinen Schritt für Schritt aufbauen und dranbleiben.")
y = card(d, y, "B: Dich anpassen. Mehr Struktur, mehr gelenkte Phasen. Dafür mehr Zeit für individuelle Förderung.")
y = block(d, y+20, "Beides ist legitim.", b(46), MINT, 60)
num(d, 5); img.save("r5.png")

# 6 Beziehung
img, d = base(TAG)
y = block(d, 500, "Was am meisten zählt:", r(48), GRAY, 66) + 10
d.text((M, y), "Beziehung.", font=sb(110), fill=MINT); y += 170
y = block(d, y, "Die Lehrer-Schüler-Beziehung gehört laut Hattie zu den stärksten Einflüssen auf den Lernerfolg.", r(42), GRAY, 58) + 40
for t in ["Namen kennen und nutzen", "Interesse an ihnen zeigen, nicht nur an Noten", "Verlässlich sein, auch bei Konsequenzen", "Kleine Erfolge sehen und sagen"]:
    d.ellipse([M, y+14, M+22, y+36], fill=MINT)
    for l in wrap(d, t, b(40), MAXW-50):
        d.text((M+45, y), l, font=b(40), fill=DG); y += 54
    y += 16
num(d, 6); img.save("r6.png")

# 7 Merksatz
img, d = base(TAG)
y = block(d, 520, "Erst Beziehung,", sb(84), DG, 104)
y = block(d, y, "dann Methode.", sb(84), MINT, 104) + 50
y = block(d, y, "Die beste Methode bringt wenig, wenn die Klasse dir nicht vertraut. Mit Vertrauen funktioniert dann oft auch mehr Offenheit.", r(44), GRAY, 62) + 60
d.line([(M, y), (M+200, y)], fill=MINT, width=6); y += 40
y = block(d, y, "Mein Unterrichtsmaterial für Mathe, Physik, Technik und IT findest du auf eduki unter MrMint.", r(36), MINT, 50)
num(d, 7); img.save("r7.png")

contact_sheet([f"r{i}.png" for i in range(1, N+1)], "/tmp/sheet.png", cols=4)
