import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=9, kicker_base="KI im Lehreralltag")

img, d, y = P.cover("Teil 7", "Ein Lernspiel in fünf Minuten. Ohne Programmieren.",
                    "Die KI baut dir ein Quiz oder Memory für deine Klasse.")
P.sticker(img, y, "tipp"); P.done(img, d, y, dark=True)

img, d, y = P.page("Grundlagen", "Wie geht das ohne Programmieren?",
                   "Die KI schreibt das Spiel als kleine Webseite. Sie läuft im Browser: auf dem iPad, am Beamer oder am Handy.")
y = P.numbered(d, y + 40, ["Claude: Artifacts", "Gemini: Canvas", "ChatGPT: Code mit Vorschau im Chat"], size=36)
y = P.text(d, y + 20, "Du siehst das Spiel sofort und kannst es direkt testen.", BODY(34), GREY, 50)
P.done(img, d, y)

img, d, y = P.page("Ideen", "Diese Spiele klappen auf Anhieb.")
y = P.numbered(d, y + 50, ["Quiz mit Punkten", "Memory", "Zuordnen und Lückentext", "Glücksrad und Zeit-Challenge"])
y = P.text(d, y + 30, "Je einfacher die Spielidee, desto besser das Ergebnis. Fang mit einem Quiz an.", BODY(34), GREY, 50)
P.done(img, d, y)

img, d, y = P.page("Prompt", "Die fünf Bausteine für den Spiel-Prompt.")
y = P.numbered(d, y + 40, ["Spieltyp: Quiz, Memory, Zuordnen", "Inhalt: deine Aufgaben, Thema, Niveau", "Zielgruppe: Klasse und Sprache", "Gerät: iPad, Beamer oder Handy", "Regeln: Punkte, Timer, Feedback"], size=36)
P.done(img, d, y)

img, d, y = P.page("Zum Kopieren", "Ein Beispiel-Prompt.")
y = P.panel(d, y + 40, "Prompt", "Erstelle ein Quiz als Webseite für Klasse 6 zum Thema Brüche. 15 Fragen in 3 Levels, steigend schwer. Große Buttons fürs iPad. 10 Punkte pro richtige Antwort, bei Fehlern den Lösungsweg zeigen. Fragen zufällig mischen. Am Ende Punktestand und Button „Nochmal spielen“. Keine Namenseingabe.", size=32)
P.done(img, d, y)

img, d, y = P.page("Qualität", "Darauf musst du achten.")
y = P.numbered(d, y + 50, ["Aufgaben selbst liefern oder genau prüfen", "Große Buttons und Schrift fürs Tablet", "Fragen zufällig mischen lassen", "Lösungsweg bei Fehlern anzeigen"], size=36)
y = P.warn(d, y + 20, "Keine Namen oder Logins der SuS.")
P.done(img, d, y)

img, d, y = P.page("Feinschliff", "Nachbessern im Chat.",
                   "Spiel das Ergebnis einmal selbst durch. Dann:")
y = P.numbered(d, y + 40, ["„Mach die Buttons größer.“", "„Füge einen 30-Sekunden-Timer hinzu.“", "„Level 3 ist zu leicht, mach es kniffliger.“"], size=36)
P.done(img, d, y)

img, d, y = P.page("Verteilen", "So kommt das Spiel zu deiner Klasse.")
y = P.numbered(d, y + 50, ["Als Link teilen, wenn dein Tool das anbietet", "Oder als HTML-Datei speichern und über deine Lernplattform verteilen, zum Beispiel iServ", "SuS öffnen die Datei im Browser"], size=36)
y = P.text(d, y + 20, "Am Beamer geht auch ein Klassen-Duell: zwei Teams, abwechselnd antworten.", BODY(32), GREY, 46)
P.done(img, d, y)

img, d, y = P.end("KI im Lehreralltag · Teil 7", "Welches Spiel baust du als Erstes?",
                  "Speicher dir den Post, dann hast du den Prompt beim nächsten Mal parat.",
                  next_part="Lernspiele mit Bestenliste und Lehrgänge")
P.done(img, d, y, dark=True)
P.save(HERE, prefix="teil7")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
