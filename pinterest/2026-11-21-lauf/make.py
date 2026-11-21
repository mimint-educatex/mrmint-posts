import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
P = [
 ("lichtbrechung",[1,2,3],"PHYSIK · KLASSE 7/8","Lichtbrechung","Brechungsregeln und Totalreflexion",["3 Seiten","6 Fragen","mit Musterlösung"],"Brechung am Lot verstehen","lichtbrechung_a_mockup"),
 ("mond",[1,2],"PHYSIK · KLASSE 7/8","Die\nMondphasen","Lückentext mit Bild zu allen Phasen",["2 Seiten","Lückentext","mit Lösung"],"Neumond bis Vollmond verstehen","mondphasen_a_mockup"),
 ("clientserver",[1,2],"INFORMATIK · SEK I","Client-Server-\nPrinzip","Infotext und vier Aufgaben",["2 Seiten","4 Aufgaben","mit Lösung"],"Anfrage und Antwort, Pull und Push","clientserver_a_mockup"),
 ("terme_paket",[1,2,3],"MATHE · KLASSE 6/7","Materialpaket\nTerme vereinfachen","Differenziert mit Lösungen",["5 Materialien","differenziert","mit Lösungen"],"Alle Termarten in einem Paket","terme_paket_a_mockup"),
 ("bruch_paket",[1,2,3],"MATHE · SEK I","Materialpaket\nBruchrechnung","Wiederholung und Vertretungsmaterial",["4 Materialien","Wiederholung","Übungen"],"Brüche sicher beherrschen","bruch_paket_a_mockup"),
]
for k,pg,fach,t,u,ch,fuss,out in P:
    mockup(f"src/{k}.pdf",pg,fach,t,u,ch,fuss,f"out/{out}.jpg")
mockup("src/netz_paket.pdf",[1,2,3],"INFORMATIK · SEK I","Materialpaket\nNetzwerke","Vom Client-Server-Prinzip bis zum WLAN",["4 Materialien","Netzwerke","Übungen"],"Netzwerke einfach verstehen","out/netzwerke_paket_a_mockup.jpg")
