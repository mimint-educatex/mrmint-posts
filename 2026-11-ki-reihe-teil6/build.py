import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=8, kicker_base="KI im Lehreralltag")

img, d, y = P.cover("Teil 6", "Deine KI kann mehr als Arbeitsblätter.",
                    "Als Organizer behält sie Termine, Mails und To-dos im Blick.")
P.sticker(img, y, "tipp"); P.done(img, d, y, dark=True)

img, d, y = P.page("Grundlagen", "Verbinde die KI mit deinen Apps.",
                   "Viele KIs lassen sich mit Kalender und Mail verbinden. Je nach Tool heißt das Connector oder App.")
y = P.panel(d, y + 50, "Wichtig", "Die KI macht Vorschläge. Prüf jeden Vorschlag, bevor etwas eingetragen oder gesendet wird.")
P.done(img, d, y)

img, d, y = P.page("Anwendung 1", "Termine in Sekunden eintragen.",
                   "Terminplan der Schule als Foto oder PDF hochladen und die KI übernehmen lassen.")
y = P.quote(d, y + 50, "„Trag alle Klassenarbeits-Termine aus diesem Plan in meinen Kalender ein, mit Erinnerung eine Woche vorher.“", size=38)
y = P.text(d, y + 40, "Konferenzen, Elternabende und Notenfristen laufen genauso.", BODY(34), GREY, 50)
P.done(img, d, y)

img, d, y = P.page("Anwendung 2", "Mails schneller abarbeiten.",
                   "Lange Verläufe zusammenfassen und Antworten vorformulieren lassen.")
y = P.numbered(d, y + 40, ["„Was muss ich diese Woche noch beantworten?“", "„Fass den Verlauf zur Klassenfahrt in drei Punkten zusammen.“", "„Schreib eine freundliche, klare Antwort an die Eltern.“"], size=34)
P.done(img, d, y)

img, d, y = P.page("Anwendung 3", "To-dos, die sich selbst anlegen.",
                   "Aus einem Termin leitet die KI ab, was du vorher erledigen musst.")
y = P.panel(d, y + 50, "Beispiel", "Termin: Klassenarbeit Mathe 8a. Daraus werden zwei To-dos: KA erstellen, eine Woche vorher. KA korrigieren, eine Woche danach.")
P.done(img, d, y)

img, d, y = P.page("Routine", "Dein Montags-Briefing.",
                   "Fünf Minuten am Montagmorgen, und du weißt, was die Woche bringt.")
y = P.quote(d, y + 50, "„Was steht diese Woche an? Liste Termine, Fristen und offene To-dos. Was sollte ich heute zuerst erledigen?“", size=38)
y = P.text(d, y + 40, "Noch bequemer als Skill, wie in Teil 5.", BODY(34), GREY, 50)
P.done(img, d, y)

img, d, y = P.page("Grenzen", "Klare Grenzen setzen.")
y = P.numbered(d, y + 50, ["Nichts ohne deine Freigabe senden lassen", "Dienstliches und Privates trennen", "Vorgaben deiner Schule zu Apps beachten"])
y = P.warn(d, y + 30, "Noten und Schülerdaten gehören in kein privates KI-Konto.")
P.done(img, d, y)

img, d, y = P.end("KI im Lehreralltag · Teil 6", "Was soll deine KI dir abnehmen?",
                  "Speicher dir den Post, dann planst du die nächste Woche leichter.",
                  next_part="Lernspiele per Prompt")
P.done(img, d, y, dark=True)
P.save(HERE, prefix="teil6")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
