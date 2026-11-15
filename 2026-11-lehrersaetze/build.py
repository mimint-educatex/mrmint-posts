import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=8, kicker_base="Lehreralltag")
img, d, y = P.cover("Übersetzt", "Sätze, die nur Lehrkräfte sagen", "Und was wirklich gemeint ist.")
P.sticker(img, y, "inspiration"); P.done(img, d, y, dark=True)

def big(kicker, headline, label, body):
    img, d = P._frame(kicker, False)
    y = P.text(d, 380, headline, HEAD(104), INK, 116, maxlines=3)
    d.rectangle([M, y + 50, M + 120, y + 58], fill=MINT)
    d.text((M, y + 110), label, font=BODY(30, "SemiBold"), fill=MINT)
    y = P.text(d, y + 165, body, BODY(50, "Medium"), GREY, 68, maxlines=4)
    P.done(img, d, y)
items = [
 ("„Ich warte.“", "Gemeint ist: Ich stehe hier, bis es leise ist. Ich habe die ganze Stunde Zeit."),
 ("„Das war keine Frage.“", "Gemeint ist: Die Diskussion ist beendet. Setz dich bitte."),
 ("„Wir machen das kurz zusammen.“", "Gemeint ist: Das dauert mindestens eine Viertelstunde."),
 ("„Ich schicke euch das über iServ.“", "Gemeint ist: Ich hoffe, ich finde die Datei heute Abend wieder."),
 ("„Ihr könnt gerne leise arbeiten.“", "Gemeint ist: Das war keine Einladung."),
 ("„Das kommt in der Arbeit dran.“", "Gemeint ist: Jetzt schreibt plötzlich die ganze Klasse mit."),
]
for i, (h, b) in enumerate(items, 1):
    big(f"Satz {i} von 6", h, "GEMEINT IST", b.replace("Gemeint ist: ", ""))
img, d, y = P.end("Lehreralltag · Übersetzt", "Welcher Satz fehlt hier?", "Schreib ihn in die Kommentare und schick den Post an eine Kollegin.")
P.done(img, d, y, dark=True)
P.save(HERE, prefix="ls")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
