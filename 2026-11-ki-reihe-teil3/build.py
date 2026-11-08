import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=8, kicker_base="KI im Lehreralltag")

img, d, y = P.cover("Teil 3", "Ein Chat für alles? Darum wird es chaotisch.",
                    "Mit Projekten bekommt jedes Fach einen eigenen Ordner, den die KI kennt.")
P.sticker(img, y, "tipp"); P.done(img, d, y, dark=True)

img, d, y = P.page("Grundlagen", "Was ist ein Projekt?",
                   "Ein eigener Bereich in deiner KI. Alles, was dort liegt, kennt jeder Chat in diesem Projekt. Bei ChatGPT und Claude heißt das genau so.")
y = P.numbered(d, y + 60, ["Anweisungen: Regeln, die immer gelten", "Dateien: Bildungsplan, Vorlagen, Raster", "Chats: alle Gespräche zum Thema"])
P.done(img, d, y)

img, d, y = P.page("Aufteilung", "Ein Projekt pro Fach und Klasse.",
                   "Dazu ein paar Projekte für Aufgaben, die quer durchgehen.")
y = P.panel(d, y + 50, "Beispiel", "Mathe Klasse 8, Technik Klasse 9, Klassenarbeiten, Klassenleitung")
y = P.text(d, y + 50, "Lieber fünf gepflegte Projekte als zwanzig halbe. Fang mit deinem Hauptfach an.", BODY(34), GREY, 50)
P.done(img, d, y)

img, d, y = P.page("Baustein 1", "Die Anweisungen sind das Herzstück.",
                   "Hier steht, was in diesem Projekt immer gilt. Zum Beispiel:")
y = P.quote(d, y + 50, "Physik Klasse 9, mittleres Niveau. Aufgaben in drei Stufen. Formeln immer mit Einheiten, Lösungen mit Rechenweg auf einer extra Seite.")
P.done(img, d, y)

img, d, y = P.page("Baustein 2", "Wenige Dateien, aber die richtigen.",
                   "Zu viel Material widerspricht sich irgendwann. Das lohnt sich:")
y = P.numbered(d, y + 50, ["Bildungsplan-Auszug zum Fach", "Stoffverteilungsplan", "zwei bis drei deiner Vorlagen"])
y = P.warn(d, y + 30, "Keine Schülerlisten, Noten oder Gutachten.")
P.done(img, d, y)

img, d, y = P.page("Im Alltag", "Neuer Chat, sofort im Bild.",
                   "Du schreibst nur noch, was du heute brauchst. Den Rest kennt die KI aus dem Projekt.")
y = P.quote(d, y + 50, "„AB zum Ohmschen Gesetz für eine Doppelstunde.“", size=44)
P.done(img, d, y)

img, d, y = P.page("Typische Fehler", "Das bremst Projekte aus.")
y = P.numbered(d, y + 50, ["Für jede Kleinigkeit ein eigenes Projekt", "Dreißig Dateien, die sich widersprechen", "Anweisungen vom September, die im Mai nicht mehr passen"])
y = P.text(d, y + 30, "Einmal im Monat fünf Minuten aufräumen reicht.", BODY(34, "SemiBold"), INK, 50)
P.done(img, d, y)

img, d, y = P.end("KI im Lehreralltag · Teil 3", "Wie teilst du deine Projekte auf?",
                  "Speicher dir den Post für die nächste Freistunde.",
                  next_part="Dein Styleguide für Arbeitsblätter und Folien")
P.done(img, d, y, dark=True)
P.save(HERE, prefix="teil3")
if "--reel" in sys.argv: P.reel(HERE)
print("ok")
