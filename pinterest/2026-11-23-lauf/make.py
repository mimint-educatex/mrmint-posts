import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
P = [
 ("teil_paket",[1,2,3],"MATHE · SEK I","Materialpaket\nTeilbarkeitsregeln","7 Materialien mit Lösungen und Abschlusstest",["7 Materialien","mit Lösungen","Test"],"Teilbarkeit sicher üben","teilbarkeit_paket_a_mockup"),
 ("linfkt_paket",[1,2,3],"MATHE · SEK I","Materialpaket\nLineare Funktionen","Wiederholung mit Lösungen",["2 Materialien","Wiederholung","mit Lösungen"],"Lineare Funktionen sicher üben","linfkt_paket_a_mockup"),
 ("teiler",[1,2,3],"MATHE · SEK I","Teiler und\nVielfache","Übung mit Lösung",["3 Seiten","Aufgaben","mit Lösung"],"Der Einstieg in die Teilbarkeit","teiler_a_mockup"),
 ("licht",[1,2,3],"PHYSIK · KLASSE 7/8","Zerlegung des\nweißen Lichts","Prisma, Spektrum und Regenbogen",["3 Seiten","6 Fragen","mit Musterlösung"],"Warum das Prisma Farben trennt","licht_a_mockup"),
 ("loch",[1,2],"PHYSIK · KLASSE 7/8","Lochkamera","Infotext und sechs Fragen",["2 Seiten","6 Fragen","mit Abbildung"],"Wie das Bild auf dem Kopf entsteht","lochkamera_a_mockup"),
 ("farbmischung",[1,2,3],"PHYSIK · KLASSE 7/8","Additive\nFarbmischung","RGB-Licht, Tabelle und Lückentext",["3 Seiten","6 Fragen","mit Lösung"],"Rot, Grün und Blau mischen","farbmischung_a_mockup"),
 ("eva",[1,2,3],"INFORMATIK · SEK I","EVA-Prinzip","Eingabe, Verarbeitung, Ausgabe",["3 Seiten","5 Fragen","mit Lösung"],"Wie Computer Daten verarbeiten","eva_a_mockup"),
 ("bohr",[1,2],"TECHNIK · KLASSE 7/8","Standbohr-\nmaschine","Arbeitsschritte in die richtige Reihenfolge bringen",["2 Seiten","13 Schritte","mit Lösung"],"Sicher bohren lernen","bohrmaschine_a_mockup"),
 ("ohm",[1,2,3],"TECHNIK · KLASSE 7/8","Ohmsches\nGesetz","Widerstände berechnen mit dem Formeldreieck",["4 Seiten","5 Aufgaben","mit Lösung"],"U, R und I sicher berechnen","ohm_a_mockup"),
]
for k,pg,fach,t,u,ch,fuss,out in P:
    mockup(f"src/{k}.pdf",pg,fach,t,u,ch,fuss,f"out/{out}.jpg")
