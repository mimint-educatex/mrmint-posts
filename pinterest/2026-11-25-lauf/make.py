import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
S = "src/"
P = [
 (S+"spiegel.pdf",[1,2,3],"PHYSIK · KLASSE 7/8","Spiegelbilder\nkonstruieren","Text, Fragen und Konstruktionsaufgabe",["4 Seiten","6 Fragen","mit Musterlösung"],"Spiegelbild und Trugbild","spiegel_a_mockup"),
 (S+"ascii.pdf",[1,2,3],"INFORMATIK · SEK I","ASCII-Code","Von Text zu ASCII zu Binärcode",["4 Seiten","4 Aufgaben","mit Lösung"],"Wie Computer Text speichern","ascii_a_mockup"),
 (None,[(S+"lin1.pdf",1),(S+"lin2.pdf",1),(S+"lin3.pdf",1)],"PHYSIK · KLASSE 7/8","Materialpaket\nSammellinse","Bildentstehung, Brennpunkt, Linsenkamera",["4 Materialien","Optik","Lehrermaterial"],"Die Sammellinse sicher verstehen","linsen_paket_a_mockup"),
 (S+"vorw.pdf",[1,2,4],"TECHNIK · ELEKTROTECHNIK","Vorwiderstand\nfür LEDs","Schrittweise berechnen, mit Tabelle",["4 Seiten","7 Aufgaben","mit Lösung"],"LEDs richtig dimensionieren","vorwiderstand_a_mockup"),
 (S+"gleich.pdf",[1,2,3],"MATHE · SEK I","Gleichungen\nlösen","Vom Einstieg bis zu Sachaufgaben",["3 Seiten","6 Blöcke","Basis + Standard"],"Schritt für Schritt zu x","gleichungen_a_mockup"),
 (None,[(S+"cod1.pdf",1),(S+"cod2.pdf",1),(S+"cod3.pdf",1)],"INFORMATIK · SEK I","Materialpaket\nCodes und Codierung","ASCII, Binärsystem, Codierung im Alltag",["4 Materialien","Arbeitsblätter","Sek I"],"Codes im Alltag verstehen","codes_paket_a_mockup"),
 (S+"seh.pdf",[1,2,3],"PHYSIK · KLASSE 7/8","Kurz- und\nWeitsichtigkeit","Auge, Linsen und Brillen",["3 Seiten","6 Fragen","mit Lösung"],"Warum Brillen scharf stellen","sehschwaechen_a_mockup"),
 (None,[(S+"zs1.pdf",1),(S+"zs2.pdf",1),(S+"zs3.pdf",1)],"MATHE · KLASSE 5","Materialpaket\nZahlenstrahl","2 Materialien mit Lösung und Lehrermaterial",["2 Materialien","mit Lösung","Klasse 5"],"Zahlenstrahl sicher zeichnen","zahlenstrahl_paket_a_mockup"),
 (S+"ki.pdf",[1,2,3],"INFORMATIK · SEK I","KI im Alltag\nverstehen","TikTok, Spotify und Co. erklärt",["5 Seiten","3 Niveaus","mit Lösung"],"Wie KI Entscheidungen trifft","ki_alltag_a_mockup"),
(S+"proz.pdf",[1,2,3],"MATHE · SEK I","Prozentwert\nberechnen","Dreisatz und Prozentstreifen",["4 Seiten","3 Aufgaben","mit Lösung"],"Prozentwert sicher berechnen","prozentwert_a_mockup"),
]
for pdf,pg,fach,t,u,ch,fuss,out in P:
    mockup(pdf,pg,fach,t,u,ch,fuss,f"out/{out}.jpg")
