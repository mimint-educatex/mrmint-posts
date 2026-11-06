import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
mockup("src5/ba.pdf", [1, 2, 3], "MATHE · KLASSE 6/7", "Brüche\naddieren",
       "und subtrahieren · Übung und Wiederholung",
       ["3 Seiten", "Merkkästen", "mit Lösungen"], "Auch für Vertretungsstunden", "out/brueche_as_a_mockup.jpg")
mockup("src5/gl.pdf", [1, 2, 3], "MATHE · KLASSE 7/8", "Gleichungen\nlösen",
       "Einfach erklärt bis zu Sachaufgaben",
       ["Erklärkästen", "Sachaufgaben", "mit Lösungen"], "Schritt für Schritt", "out/gleichungen_a_mockup.jpg")
mockup("src5/pz.pdf", [1, 3, 5], "MATHE · KLASSE 7/8", "Proportionale\nZuordnungen",
       "Einführung und Festigung am Wochenmarkt",
       ["9 Seiten", "mit Tipps", "mit Lösungen"], "Inkl. Expertenaufgaben", "out/prop_zuordnungen_a_mockup.jpg")
