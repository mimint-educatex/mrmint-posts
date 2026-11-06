import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup, nutzen, einblick
P = "src/lh.pdf"; FACH = "TECHNIK · KLASSE 9/10"
mockup(P, [1, 18, 45], FACH, "micro:bit\nprogrammieren", "Lernheft für Einsteiger · MakeCode",
       ["54 Seiten", "mit Lösungen", "3 Projekte"], "Sofort einsetzbar", "out/microbit_a_mockup.jpg")
nutzen(P, FACH, "Die erste\nmicro:bit-Stunde?", "Fertig geplant.", (1, (130, 270, 480, 530)),
       ["Von der LED bis zum Sensor", "12 Aufgaben und 3 Projekte", "Gestufte Tipps zu jeder Aufgabe", "Ohne Installation im Browser"],
       "54 Seiten Lernheft", "out/microbit_b_nutzen.jpg")
einblick(P, [9, 10, 11], ["Auftrag", "Tipps", "Lösung"], FACH, "micro:bit\nAufgaben", "Jede Aufgabe in drei Stufen",
         ["Selbstständig", "Differenziert", "54 Seiten"], "Ideal für Freiarbeit", "out/microbit_c_einblick.jpg")
