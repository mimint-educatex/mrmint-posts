import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
P = [
 ("klammer",[1,2],"MATHE · KLASSE 7/8","Klammern\nauflösen","mit Plus oder Minus davor",["2 Seiten","Schritt für Schritt","mit Lösungen"],"Vorzeichenregeln sicher üben","klammer_a_mockup"),
 ("zylinder",[1,2,3],"MATHE · KLASSE 8/9","Volumen\nZylinder","Formel in Gruppenarbeit erarbeiten",["3 Seiten","Gruppenarbeit","mit Lösungen"],"Mit Rollen für die Gruppe","zylinder_a_mockup"),
 ("saegen",[1,2,3],"TECHNIK · KLASSE 8/9","Metall\nsägen","Handbügelsäge und Zahnteilung",["3 Seiten","mit Lösungen","Selbsteinschätzung"],"Theorie für den Technikunterricht","metall_saegen_a_mockup"),
 ("holz",[1,2,5],"TECHNIK · KLASSE 7/8","Holzverbindungen","Dübeln, Schrauben, Nageln, Leimen",["6 Seiten","Differenzierung","mit Lösungen"],"Verbindungen im Vergleich","holzverbindungen_a_mockup"),
 ("gewinde",[1,2,3],"TECHNIK · KLASSE 7/8","Gewinde\nschneiden","Theorie-AB mit Kernlochtabelle",["3 Seiten","mit Lösung","Selbsteinschätzung"],"Vom Kernloch zum Gewinde","gewindeschneiden_a_mockup"),
 ("legostein",[1],"TECHNIK · KLASSE 7/8","Messschieber\nÜbungen","Messen am Legostein",["1 Seite","5 Messaufgaben","mit Lösung"],"Ablesen und Messen üben","messschieber_a_mockup"),
 ("terme",[1,2],"MATHE · KLASSE 6/7","Terme und\nVariablen","Einführung mit Aufgaben",["2 Seiten","mit Lösungen","Selbsteinschätzung"],"Der Einstieg in die Algebra","terme_a_mockup"),
 ("vierecke",[1,2,3],"MATHE · KLASSE 6/7","Vierecke\nbenennen","Vierecke erkennen und unterscheiden",["4 Seiten","mit Lösungen","Geometrie"],"Vierecksarten sicher erkennen","vierecke_a_mockup"),
 ("multimeter",[1,2,3],"TECHNIK · KLASSE 7/8","Messen mit dem\nMultimeter","Anleitung für Schülerinnen und Schüler",["3 Seiten","mit Lösungen","Widerstand messen"],"Mit Anleitung und Aufgaben","multimeter_a_mockup"),
 ("widerstand",[1,2],"TECHNIK · KLASSE 7/8","Widerstand\nmessen","Reihen- und Parallelschaltung an der Messplatte",["2 Seiten","mit Lösungen","Formeln herleiten"],"Messen, vergleichen, herleiten","widerstand_a_mockup"),
 ("lagebez",[1,2,3],"MATHE · KLASSE 8/9","Lagebeziehungen\nvon Geraden","Lineare Funktionen: parallel oder senkrecht",["3 Seiten","mit Lösungen","parallel / senkrecht"],"Mit Steigungen entscheiden","lagebeziehungen_a_mockup"),
 ("kommunikation",[1,2],"INFORMATIK · KLASSE 5/6","Digital\nkommunizieren","Infotext und Fragen zum Text",["2 Seiten","6 Fragen","mit Lösungen"],"Kommunikation im Netz verstehen","kommunikation_a_mockup"),
 ("biegen",[1,2],"TECHNIK · KLASSE 7/8","Kunststoffe\nbiegen","Verfahren im Vergleich",["2 Seiten","Infotext","mit Lösungen"],"Heizdraht, Heißluft und mehr","kunststoff_biegen_a_mockup"),
 ("kunststoff",[1,2,3],"TECHNIK · KLASSE 7/8","Herstellung von\nKunststoff","Von Erdöl zum Kunststoff",["3 Seiten","Infotext","mit Lösungen"],"Vom Rohstoff zum Produkt","kunststoff_herstellung_a_mockup"),
]
for k,pg,fach,t,u,ch,fuss,out in P:
    mockup(f"src/{k}.pdf",pg,fach,t,u,ch,fuss,f"out/{out}.jpg")
