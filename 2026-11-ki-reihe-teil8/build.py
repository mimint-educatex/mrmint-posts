import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=10, kicker_base="KI im Lehreralltag")

img, d, y = P.cover("Teil 8", "Eine Bestenliste für die ganze Klasse?",
                    "Lernspiele mit Speicherfunktion und Selbstlern-Lehrgänge, ohne Abo.")
P.sticker(img, y, "tipp"); P.done(img, d, y, dark=True)

img, d, y = P.page("Der Unterschied", "Level 1 und Level 2.",
                   "Spiele aus Teil 7 vergessen alles, sobald man sie schließt. Für mehr brauchst du zwei Helfer.")
y = P.numbered(d, y + 40, ["Level 1: läuft auf einem Gerät, nichts wird gespeichert", "Level 2: online für alle, Punkte und Fortschritt werden gespeichert"], size=36)
P.done(img, d, y)

img, d, y = P.page("Die Werkzeuge", "Zwei Helfer, beide mit kostenlosem Einstieg.",
                   "Du brauchst dafür kein Abo.")
y = P.numbered(d, y + 40, ["Netlify stellt dein Spiel online, mit eigenem Link für die Klasse", "Supabase ist die Datenbank für Punktestände und Fortschritt"], size=36)
y = P.text(d, y + 20, "Programmieren musst du trotzdem nicht. Die KI schreibt den Code und erklärt dir die Klicks.", BODY(32), GREY, 46)
P.done(img, d, y)

img, d, y = P.page("Ablauf", "So läuft es ab.")
y = P.numbered(d, y + 40, ["Die KI baut das Spiel wie in Teil 7", "Kostenloses Supabase-Projekt anlegen", "Öffentlichen Schlüssel an die KI geben, sie baut die Verbindung ein", "Spiel-Ordner bei Netlify hochladen", "Link an die Klasse"], size=34)
P.done(img, d, y)

img, d, y = P.page("Grenzen 1 von 2", "Kostenlos heißt mit Grenzen.")
y = P.numbered(d, y + 40, ["Supabase pausiert kostenlose Projekte bei zu wenig Aktivität in einer Woche. Du bekommst vorher eine Mail und startest es im Dashboard wieder.", "Netlify Free hat 300 Credits im Monat als hartes Limit. Sind sie weg, pausiert das Projekt."], size=32)
P.done(img, d, y)

img, d, y = P.page("Grenzen 2 von 2", "Sicherheit gehört dazu.")
y = P.numbered(d, y + 40, ["Nur den öffentlichen Schlüssel ins Spiel, nie den geheimen", "Nur Team- oder Spitznamen speichern", "Bei Fragen zum Datenschutz die Schulleitung einbeziehen"], size=36)
P.done(img, d, y)

img, d, y = P.page("Das nächste Level", "Selbstlern-Lehrgänge.",
                   "Mit derselben Technik baust du Lehrgänge: SuS arbeiten im eigenen Tempo, du siehst, wer wo steht.")
y = P.panel(d, y + 40, "Beispiele", "Messschieber ablesen, Multimeter, Brüche kürzen, Stromkreise. Gut für Vertretungsstunden, Nachzügler und Differenzierung.")
P.done(img, d, y)

img, d, y = P.page("Prompt", "Bausteine für den Lehrgang.")
y = P.numbered(d, y + 40, ["Lernziel: Was können SuS am Ende?", "Kapitel in kleinen Schritten", "Übungen nach jedem Kapitel, mit Feedback", "Fortschrittsbalken und freigeschaltete Level", "Abschlusstest mit Ergebnis-Code"], size=34)
P.done(img, d, y)

img, d, y = P.page("Einschätzung", "Lohnt sich das?",
                   "Plane für das erste Projekt etwas Zeit ein. Danach geht es deutlich schneller.")
y = P.numbered(d, y + 40, ["Wenn du es jedes Jahr einsetzt", "Für Klassen-Wettbewerbe", "Für Inhalte, die SuS oft wiederholen"], size=36)
y = P.text(d, y + 20, "Starte mit Level 1. Fehlt dir irgendwann die Bestenliste, ist das dein Zeichen für Level 2.", BODY(32), GREY, 46)
P.done(img, d, y)

img, d, y = P.end("KI im Lehreralltag · Teil 8", "Welcher Teil hat dir am meisten gebracht?",
                  "Das war die ganze Reihe. Schreib es in die Kommentare und speicher dir die Teile, die du noch umsetzen willst.")
P.done(img, d, y, dark=True)
P.save(HERE, prefix="teil8")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
