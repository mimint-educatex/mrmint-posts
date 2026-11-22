import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=8, kicker_base="Unterricht")

img, d, y = P.cover("Einordnung", "Frontalunterricht ist besser als sein Ruf.", "Stimmt das? Eine Einordnung mit Studien.")
P.sticker(img, y, "tipp"); P.done(img, d, y, dark=True)

def big(kicker, headline, body, hs=88, bs=44, lh=62, maxl=7):
    img, d = P._frame(kicker, False)
    y = P.text(d, 300, headline, HEAD(hs), INK, hs + 12, maxlines=3)
    d.rectangle([M, y + 40, M + 120, y + 48], fill=MINT)
    y = P.text(d, y + 100, body, BODY(bs, "Medium"), GREY, lh, maxlines=maxl)
    return img, d, y

img, d, y = big("Das spricht dafür", "Anfänger brauchen Anleitung",
    "Wer in einem Thema neu ist, lernt neuen Stoff mit klarer Führung meist besser als mit minimaler Hilfe: erst zeigen, dann üben, mit Rückmeldung. So argumentieren Kirschner, Sweller und Clark (2006).")
P.done(img, d, y)

img, d = P._frame("Wichtig vorab", False)
y = P.text(d, 250, "Gemeint ist kein Dauervortrag", HEAD(80), INK, 92, maxlines=3) + 40
d.text((M, y), "rund 0,6", font=HEAD(120), fill=MINT)
y = P.text(d, y + 150, "Effektstärke für Direct Instruction bei Hattie. Dazu gehören Lernziele, Beispiele, geführtes Üben und Verständnischecks.", BODY(38, "Medium"), INK, 54, maxlines=4) + 30
y = P.text(d, y, "Reines Zuhören gehört nicht dazu.", BODY(34), GREY, 50)
P.done(img, d, y)

img, d, y = big("Der Haken", "Wer viel weiß, braucht weniger Führung",
    "Kalyuga nennt das Expertise Reversal Effect: Hilfen, die Anfängern nützen, können Fortgeschrittene bremsen. Wer Termumformungen sicher kann, braucht keine Schritt-für-Schritt-Vorgabe mehr.", hs=80, bs=42, lh=60)
P.done(img, d, y)

img, d, y = big("Nicht alle sehen das so", "Die Debatte ist offen",
    "Hmelo-Silver und Kollegen (2007) halten dagegen: Gut angeleitete Projektarbeit ist etwas anderes als reines Entdecken. Und Gespräche, in denen Kinder viel begründen, hängen mit mehr Lernzuwachs zusammen. Sie brauchen aber Monate Übung.", hs=84, bs=40, lh=58)
P.done(img, d, y)

img, d = P._frame("Woran es hängt", False)
y = P.text(d, 300, "Es kommt darauf an", HEAD(84), INK, 96, maxlines=2) + 50
y = P.numbered(d, y, [
    "Wie viel Vorwissen die Klasse hat",
    "Ob neuer Stoff oder Übung dran ist",
    "Wie lang die gelenkte Phase dauert",
    "Ob die Kinder dabei mitdenken oder nur zuhören"], size=42)
P.done(img, d, y)

img, d = P._frame("Auflösung", False)
y = P.text(d, 300, "Stimmt die Überschrift?", HEAD(88), INK, 100, maxlines=2) + 50
y = P.panel(d, y, "Teils", "Für neuen Stoff sind gelenkte Phasen oft stark. Als Dauermodus tragen sie nicht.", size=42)
P.done(img, d, y)

img, d, y = P.end("Unterricht", "Wo setzt du bewusst auf gelenkte Phasen?", "Und wo lieber nicht? Schreib es in die Kommentare und schick den Post an eine Kollegin.")
P.done(img, d, y, dark=True)

P.save(HERE, prefix="fu")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
