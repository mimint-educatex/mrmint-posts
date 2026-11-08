import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=8, kicker_base="KI im Lehreralltag")

img, d, y = P.cover("Teil 4", "Jedes KI-Arbeitsblatt sieht anders aus?",
                    "Mit einem Styleguide bekommst du jedes Mal dein Layout.")
P.sticker(img, y, "tipp"); P.done(img, d, y, dark=True)

img, d, y = P.page("Der Begriff", "Was ist ein Styleguide?",
                   "Eine Übersicht mit deinen Gestaltungsregeln: Farben, Schriften, Größen und der feste Aufbau deiner Materialien.")
y = P.text(d, y + 50, "Firmen nennen das Corporate Design, in Canva heißt es Brand Kit. Ohne Styleguide erfindet die KI jedes Mal ein neues Design.", BODY(34, "Medium"), INK, 50)
P.done(img, d, y)

img, d, y = P.page("Baustein 1", "Wenige Farben, jede mit Aufgabe.",
                   "Gib sie als Farbcode an, dann trifft die KI genau deinen Ton.")
y = P.panel(d, y + 50, "Beispiel", "Mint #2CA89E für Nummern und Rahmen. Dunkelgrün #14503F für Überschriften. Gelb #F2B233 nur für Merkkästen.")
P.done(img, d, y)

img, d, y = P.page("Baustein 2", "Maximal zwei Schriften.",
                   "Eine für Überschriften, eine für den Text. Und feste Größen, damit jedes AB gleich wirkt.")
y = P.quote(d, y + 50, "Überschrift 16 pt fett, Text 12 pt, Aufgabennummern fett.")
P.done(img, d, y)

img, d, y = P.page("Baustein 3", "Fester Aufbau fürs Arbeitsblatt.")
y = P.numbered(d, y + 50, ["Kopfzeile mit Name, Datum, Klasse", "Titel mit Thema und Fach", "Infotext oder Merkkasten", "Aufgaben mit Nummer", "Platz zum Schreiben"])
P.done(img, d, y)

img, d, y = P.page("Baustein 4", "Auch Folien bekommen feste Bausteine.")
y = P.numbered(d, y + 50, ["Einstieg mit Bild, Geschichte oder These", "Arbeitsauftrag immer im gleichen Design, mit Name des ABs", "Sicherung mit einer Verständnisfrage"])
P.done(img, d, y)

img, d, y = P.page("Abkürzung", "Lass die KI deinen Styleguide ableiten.")
y = P.quote(d, y + 50, "„Leite aus diesen drei Arbeitsblättern einen Styleguide ab: Farben, Schriften, Aufbau, wiederkehrende Elemente.“")
y = P.text(d, y + 50, "Danach prüfen, ergänzen und als Datei ins Projekt legen.", BODY(34), GREY, 50)
P.done(img, d, y)

img, d, y = P.end("KI im Lehreralltag · Teil 4", "Hast du schon einen Styleguide?",
                  "Speicher dir den Post, dann hast du die Bausteine parat.",
                  next_part="Skills: Abläufe auf Knopfdruck")
P.done(img, d, y, dark=True)
P.save(HERE, prefix="teil4")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
