import sys; sys.path.insert(0, ".")
from pin_lib import mockup
mockup(None, ["src6/cover_et.png", ("src6/tr.pdf", 1), ("src6/rp.pdf", 1)], "MATERIALPAKET · TECHNIK 9/10",
       "Elektrotechnik\n15 ABs", "Vom Stromkreis bis zum Transistor",
       ["mit Lösungen", "AFB I bis III", "aufbauend"], "Die komplette Unterrichtsreihe", "out/paket_elektrotechnik_a_mockup.jpg")
mockup(None, ["src6/cover_opt.png", ("src6/mond.pdf", 1), ("src6/sch.pdf", 1)], "MATERIALPAKET · PHYSIK 7/8",
       "Optik komplett\n20 ABs", "Von Licht und Schatten bis zu Linsen",
       ["mit Lösungen", "Schatten", "Linsen"], "Die komplette Einheit", "out/paket_optik_a_mockup.jpg")
