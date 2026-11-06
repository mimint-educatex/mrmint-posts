import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
mockup("src4/bg.pdf", [1, 2], "MATHE · KLASSE 8/9", "Bruchgleichungen\nlösen",
       "Einfache Einführung mit Beispielen",
       ["2 Seiten", "Merkkästen", "mit Lösungen"], "Lösungen mit Rechenweg", "out/bruchgleichungen_a_mockup.jpg")
mockup("src4/md.pdf", [1, 2], "MATHE · KLASSE 6/7", "Brüche\nmultiplizieren",
       "und dividieren · Übung und Wiederholung",
       ["2 Seiten", "Merkkästen", "mit Lösungen"], "Ideal zum Wiederholen", "out/brueche_md_a_mockup.jpg")
