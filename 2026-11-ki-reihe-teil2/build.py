import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_mint2 import *
HERE = os.path.dirname(os.path.abspath(__file__))
P = Post(total=9, kicker_base="KI im Lehreralltag")

# 1 Cover
img, d, y = P.cover("Teil 2", "Warum klingt die KI nie nach deinem Unterricht?",
                    "Vier Dinge, die ich der KI mitgebe, damit das Material zu meiner Klasse passt.")
P.done(img, d, y, dark=True)

# 2 Problem
img, d, y = P.page("Das Problem", "Die KI kennt Schule. Aber nicht deine.",
                   "Ohne Infos rät sie: irgendein Niveau, irgendein Aufbau, irgendein Bundesland. Raus kommt Durchschnitt.")
d.text((M, y + 60), "Was sie wirklich braucht:", font=BODY(34, "SemiBold"), fill=INK)
y = P.numbered(d, y + 130, ["Infos über dich", "den passenden Bildungsplan", "eine Beschreibung deiner Klasse", "dein eigenes AB als Vorbild"])
P.done(img, d, y)

# 3 Ueber dich
img, d, y = P.page("Zutat 1 von 4", "Sag ihr einmal, wer du bist.",
                   "In den Einstellungen gibt es ein Feld für persönliche Anweisungen. Was dort steht, gilt in jedem Chat.")
y = P.panel(d, y + 50, "Persönliche Anweisungen",
            "Ich unterrichte Mathe und Technik an einer Realschule in Baden-Württemberg, Klasse 5 bis 10. Arbeitsaufträge bitte in Du-Form und in kurzen Sätzen. Antworte knapp.")
P.done(img, d, y)

# 4 Bildungsplan
img, d, y = P.page("Zutat 2 von 4", "„Nach Bildungsplan“ reicht nicht.",
                   "Die KI weiß nicht, welcher Abschnitt gemeint ist. Lade ihn hoch, dann kennt sie Kompetenzen und Operatoren.")
y = P.numbered(d, y + 60, ["Bildungsplan-Auszug als PDF", "dein Stoffverteilungsplan", "eine Operatorenliste"])
P.done(img, d, y)

# 5 Klasse
img, d, y = P.page("Zutat 3 von 4", "Beschreib die Klasse. Nicht die Kinder.",
                   "Das Niveau entscheidet, ob ein AB funktioniert. Zum Beispiel so:")
y = P.quote(d, y + 50, "Klasse 8, sehr gemischt, viele Kinder mit Deutsch als Zweitsprache. Kurze Sätze, maximal zwei Infos pro Aufgabe.")
y = P.warn(d, y + 60, "Namen und Noten bleiben draußen.")
P.done(img, d, y)

# 6 Eigenes AB
img, d, y = P.page("Zutat 4 von 4", "Dein bestes AB ist die beste Anleitung.",
                   "Aufbau, Niveau und Ton erkennt die KI daran besser als an jeder Beschreibung. Lade es hoch und schreib dazu:")
y = P.quote(d, y + 50, "„Orientiere dich an Aufbau und Niveau dieses ABs. Die Inhalte bitte nicht übernehmen.“")
P.done(img, d, y)

# 7 Interview
img, d, y = P.page("Tipp", "Lass dich von der KI interviewen.")
y = P.quote(d, y + 50, "„Stell mir 10 Fragen zu meinem Unterricht, bevor du loslegst.“", size=44)
y = P.text(d, y + 60, "Sie fragt genau das ab, was ihr fehlt. Deine Antworten sind danach das perfekte Briefing, das du immer wieder nutzen kannst.", BODY(34), GREY, 50)
P.done(img, d, y)

# 8 KI-Muster
img, d, y = P.page("Achtung", "Die KI baut Aufgaben gern immer gleich.")
y = P.compare(d, y + 60, "Typisch KI", ["x + 5 = 12", "x + 3 = 9", "x + 7 = 15"],
              "Besser gemischt", ["12 = x + 5", "3x = 9", "15 − x = 8"])
y = P.text(d, y + 50, "Gleich gebaute Aufgaben trainieren ein Muster, nicht das Thema. Bitte die KI ausdrücklich, Aufbau, Zahlen und Reihenfolge zu mischen.", BODY(34), GREY, 50)
P.done(img, d, y)

# 9 Schluss
img, d, y = P.end("KI im Lehreralltag · Teil 2", "Welche Zutat fehlt dir noch?",
                  "Speicher dir den Post, dann hast du die vier Zutaten beim nächsten Prompt parat.",
                  next_part="Projekte: dein Fach-Ordner für die KI")
P.done(img, d, y, dark=True)

P.save(HERE, prefix="teil2")
if "--reel" in sys.argv:
    P.reel(HERE)
print("ok")
