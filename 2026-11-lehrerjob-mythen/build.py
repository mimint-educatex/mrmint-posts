import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=8, kicker_base="Lehrer-Mythen")
img, d, y = P.cover("Check", "Lehrer haben ja nachmittags frei", "Fünf Sätze, die wir ständig hören, und was dahintersteckt.")
P.sticker(img, y, "inspiration"); P.done(img, d, y, dark=True)

def big(kicker, headline, label, body):
    img, d = P._frame(kicker, False)
    y = P.text(d, 380, headline, HEAD(104), INK, 116, maxlines=3)
    d.rectangle([M, y + 50, M + 120, y + 58], fill=MINT)
    d.text((M, y + 110), label, font=BODY(30, "SemiBold"), fill=MINT)
    y = P.text(d, y + 165, body, BODY(50, "Medium"), GREY, 68, maxlines=4)
    P.done(img, d, y)
items = [
 ("„Lehrer haben nachmittags frei.“", "Realität: Nach dem Unterricht beginnen Vorbereitung, Korrekturen, Elterngespräche und Konferenzen."),
 ("„Lehrer haben ständig Ferien.“", "Realität: Unterrichtsfrei heißt nicht arbeitsfrei. Zeugnisse, Korrekturen und Vorbereitung laufen oft weiter."),
 ("„Lehrer müssen doch nur reden.“", "Realität: Vor jeder Stunde stehen Planung und Material, danach die Auswertung. Sichtbar sind nur die 45 Minuten."),
 ("„Mit Kindern arbeiten ist doch entspannt.“", "Realität: Bis zu 30 Kinder, 30 Tagesformen, und alle sollen gleichzeitig etwas lernen."),
 ("„Lehrer haben einen sicheren Job.“", "Realität: Stimmt zum Teil. Verbeamtung gibt Sicherheit, dafür gibt es kein Streikrecht."),
]
for i, (h, b) in enumerate(items, 1):
    big(f"Mythos {i} von 5", h, "REALITÄT", b.replace("Realität: ", ""))
img, d, y = P.page("Fazit", "")
y = P.text(d, 360, "Der Job hat Vorteile, aber er ist kein Halbtagsjob.", HEAD(88), INK, 100, maxlines=4)
y = P.numbered(d, y + 70, ["Sichtbar ist nur der Unterricht", "Unterrichtsfrei heißt nicht arbeitsfrei", "Sicherheit gibt es, Feierabend ist Auslegungssache"], size=44)
P.done(img, d, y)
img, d, y = P.end("Lehrer-Mythen · Check", "Welchen Satz hörst du am häufigsten?", "Kommentier ihn und schick den Post an jemanden, der es nicht glaubt.")
P.done(img, d, y, dark=True)
P.save(HERE, prefix="lm")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
