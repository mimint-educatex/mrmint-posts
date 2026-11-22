import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=8, kicker_base="Lehreralltag")

img, d, y = P.cover("Entlastung", "Korrigieren ohne Rotstift-Marathon", "Fünf Wege, Zeit zu sparen. Ohne schlechtes Gewissen.")
P.sticker(img, y, "tipp"); P.done(img, d, y, dark=True)

def big(kicker, headline, body, hs=96, bs=46, lh=64, maxl=6):
    img, d = P._frame(kicker, False)
    y = P.text(d, 330, headline, HEAD(hs), INK, hs + 12, maxlines=3)
    d.rectangle([M, y + 40, M + 120, y + 48], fill=MINT)
    y = P.text(d, y + 100, body, BODY(bs, "Medium"), GREY, lh, maxlines=maxl)
    return img, d, y

img, d, y = big("Weg 1 von 5", "Selbstkontrolle statt Abgabe",
    "Die Lösungen liegen am Pult oder digital bereit. Die Kinder kontrollieren selbst und markieren, was nicht stimmt. Du schaust nur dort hin.", hs=88)
P.done(img, d, y)

img, d, y = big("Weg 2 von 5", "Stichprobe statt Vollkontrolle",
    "Lege vorher fest: Heute schaue ich nur Aufgabe 4 und 7 an. Das reicht, um zu sehen, wer es kann und wer nicht.", hs=88)
P.done(img, d, y)

img, d = P._frame("Weg 3 von 5", False)
y = P.text(d, 250, "Randzeichen statt Lösung", HEAD(88), INK, 100, maxlines=3) + 60
y = P.quote(d, y, "(−3) − (−2) = −5", size=56) + 30
y = P.quote(d, y, "Am Rand: V", size=44) + 60
y = P.text(d, y, "Das V am Rand heißt: Vorzeichen prüfen. Den Fehler findet das Kind selbst. Mit einem Kürzel pro Fehlerart reichen wenige Zeichen fürs ganze Heft.", BODY(40, "Medium"), GREY, 58, maxlines=5)
P.done(img, d, y)

img, d, y = big("Weg 4 von 5", "Eine Rückmeldung pro Heft",
    "Statt Kommentaren an jedem Rand ein Satz am Ende: ein Stern, ein Wunsch. Der ist schnell geschrieben und schnell gelesen.", hs=88)
P.done(img, d, y)

img, d, y = big("Weg 5 von 5", "Klassenfehler einmal besprechen",
    "Beim Durchsehen die drei häufigsten Fehler notieren und an der Tafel klären. Einmal erklärt statt fünfundzwanzig Mal an den Rand geschrieben.", hs=84)
P.done(img, d, y)

img, d = P._frame("Wann das passt", False)
y = P.text(d, 250, "Nicht jede Aufgabe braucht den Rotstift", HEAD(80), INK, 92, maxlines=3) + 50
y = P.panel(d, y, "Gilt für", "Hausaufgaben, Wochenpläne und Übungsphasen. Bei Klassenarbeiten gibt deine Schule den Rahmen vor.", size=38)
P.done(img, d, y)

img, d, y = P.end("Lehreralltag", "Welcher Weg spart dir am meisten Zeit?", "Schreib es in die Kommentare und schick den Post an jemanden mit Heftstapel.")
P.done(img, d, y, dark=True)

P.save(HERE, prefix="kor")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
