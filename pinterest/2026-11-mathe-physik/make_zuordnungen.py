import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
mockup("src2/zu.pdf", [1, 7, 13], "MATHE · KLASSE 7/8", "Zuordnungen\nüben",
       "proportional und antiproportional",
       ["2 Niveaus", "mit Tipps", "mit Lösungen"], "Inkl. Expertenaufgaben", "out/zuordnungen_a_mockup.jpg")
