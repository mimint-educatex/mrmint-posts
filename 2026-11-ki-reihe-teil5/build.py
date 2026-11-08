import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=8, kicker_base="KI im Lehreralltag")

img, d, y = P.cover("Teil 5", "Du erklärst der KI jede Woche dasselbe?",
                    "Mit Skills speicherst du einen Ablauf einmal und rufst ihn danach auf Knopfdruck ab.")
P.sticker(img, y, "tipp"); P.done(img, d, y, dark=True)

img, d, y = P.page("Grundlagen", "Was ist ein Skill?",
                   "Eine gespeicherte Anleitung für eine Aufgabe, die du immer wieder machst, mit Schritten, Regeln und Vorlagen. Die KI holt sie sich, sobald sie passt.")
y = P.panel(d, y + 40, "Projekt oder Skill?", "Ein Projekt sagt, WORUM es geht: Fach, Klasse, Material. Ein Skill sagt, WIE etwas gemacht wird: Schritte und Qualität.")
y = P.text(d, y + 40, "Bei Claude heißt das Skills. ChatGPT und Gemini haben Ähnliches, je nach Tarif.", BODY(30), GREY, 44)
P.done(img, d, y)

img, d, y = P.page("Faustregel", "Beim dritten Mal wird daraus ein Skill.")
y = P.numbered(d, y + 50, ["Die Aufgabe kommt regelmäßig", "Sie läuft immer in ähnlichen Schritten", "Du korrigierst immer dieselben Dinge"])
y = P.text(d, y + 30, "Einmalige Aufgaben und schnelle Fragen brauchen keinen Skill.", BODY(34), GREY, 50)
P.done(img, d, y)

img, d, y = P.page("Beispiele 1 von 2", "Skills, die sich für Lehrkräfte lohnen.")
y = P.numbered(d, y + 50, ["Klassenarbeit: Anforderungsbereiche, Punkte, Erwartungshorizont", "Arbeitsblatt im eigenen Layout, mit Lösungsblatt", "Folien zum AB: Einstieg, Arbeitsauftrag, Sicherung"])
P.done(img, d, y)

img, d, y = P.page("Beispiele 2 von 2", "Noch mehr Ideen.")
y = P.numbered(d, y + 50, ["Themenliste zur Klassenarbeit für SuS und Eltern", "Elternbrief mit festem Aufbau", "Lernspiel aus deinen Aufgaben", "Wochenplan mit Terminen und To-dos"])
P.done(img, d, y)

img, d, y = P.page("Aufbau", "Was in einen guten Skill gehört.",
                   "Im Kern ist ein Skill eine gut geschriebene Anleitung:")
y = P.numbered(d, y + 40, ["Ziel: Was soll am Ende herauskommen?", "Schritte in fester Reihenfolge", "Qualitätsregeln, die immer gelten", "Vorlagen und Beispiele", "Typische Fehler, die vermieden werden"], size=36)
P.done(img, d, y)

img, d, y = P.page("Erstellen", "Skill erstellen ohne Technik.",
                   "Der beste Moment ist direkt nach einem Chat, der richtig gut lief.")
y = P.quote(d, y + 50, "„Mach aus dem, was wir gerade gemacht haben, einen Skill. Übernimm alle meine Korrekturen als Regeln.“", size=38)
y = P.text(d, y + 40, "Später reicht: „Übernimm das in den Skill.“ So wird er mit jeder Nutzung besser.", BODY(34), GREY, 50)
P.done(img, d, y)

img, d, y = P.end("KI im Lehreralltag · Teil 5", "Welchen Ablauf erklärst du der KI ständig neu?",
                  "Speicher dir den Post, dann hast du die Bausteine beim nächsten Skill parat.",
                  next_part="KI als Organizer für Termine, Mails und To-dos")
P.done(img, d, y, dark=True)
P.save(HERE, prefix="teil5")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
