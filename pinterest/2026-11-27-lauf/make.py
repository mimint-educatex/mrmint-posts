import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
S = "src/"
FL = S+"z_flaechen/"
DT = S+"z_dreitafel/"
RE = S+"z_relais/"
P = [
 (None,[(FL+"Umfang und Flächeninhalt Rechteck & Quadra_1766351/Eduki Umfang und Flächeninhalt Rechteck & Quadrat .pdf",1),(FL+"Dreieck Flächeninhalt und Umfang Zusammenf_1773644/Eduki Dreieck Flächeninhalt und Umfang Zusammenfas.pdf",1),(FL+"Trapez Flächeninhalt & Umfang Zusammenfass_1786395/Eduki Flächeninhalt & Umfang Trapez Zusammenfassun.pdf",1)],
  "MATHE · SEK I","Materialpaket\nFlächen und Umfang","Rechteck, Quadrat, Dreieck, Parallelogramm, Trapez",["4 Materialien","Formeln","Lernhilfen"],"Alle Flächenformeln im Blick","flaechen_paket_a_mockup"),
 (S+"schatten.pdf",[1,2,1],"PHYSIK · KLASSE 7/8","Kern- und\nHalbschatten","Text, Fragen und Konstruktion",["2 Seiten","5 Fragen","mit Lösung"],"Schatten konstruieren","schatten_a_mockup"),
 (S+"datenaustausch.pdf",[1,2,1],"INFORMATIK · SEK I","Sicherer\nDatenaustausch","Privatsphäre und Verschlüsselung",["2 Seiten","6 Aufgaben","mit Lösung"],"Von Caesar bis Ende-zu-Ende","datenaustausch_a_mockup"),
 (S+"transistor.pdf",[1,2,4],"TECHNIK · ELEKTROTECHNIK","Transistor und\nDunkelschaltung","Schaltzeichen, LDR und Schwellenspannung",["4 Seiten","7 Aufgaben","mit Lösung"],"Transistor als Schalter","transistor_a_mockup"),
 (S+"vergleich.pdf",[1,2,1],"MATHE · PROZENTRECHNUNG","Absoluter und\nrelativer Vergleich","Am Downloadbalken verstehen",["2 Seiten","4 Teilaufgaben","mit Lösung"],"Prozente anschaulich","vergleich_a_mockup"),
 (None,[(DT+"Dreitafelprojektion Einführung und Übung_2261254/Dreitafelprojektion_Einfuehrung_mit_Loesung_Eduki.pdf",1),(DT+"Schrägbild zeichnen (Kavalierperspektive) _2229342/Kavalierperspektive_Schraegbild_AB_Eduki.pdf",1),(DT+"Dreitafelprojektion Übungen zum Zeichnen_2261257/Dreitafelprojektion_Uebung_mit_Loesung_Eduki.pdf",1)],
  "TECHNIK · KLASSE 7-9","Materialpaket\nTechnisches Zeichnen","Dreitafelprojektion und Kavalierperspektive",["4 Materialien","mit Lösungen","Lehrermaterial"],"Technisch zeichnen lernen","dreitafel_paket_a_mockup"),
 (S+"unsichtbar.pdf",[1,2,3],"PHYSIK · OPTIK","Unsichtbares\nLicht","Infrarot und UV-Licht im Alltag",["3 Seiten","6 Fragen","mit Lösung"],"Wärmebild, UV und Co.","unsichtbar_a_mockup"),
 (S+"urheber.pdf",[1,2,3],"MEDIENBILDUNG · SEK I","Urheberrecht und\nCC-Lizenzen","Mit Fallbeispielen aus dem Alltag",["4 Seiten","8 Aufgaben","mit Lösung"],"Darf ich das Bild nutzen?","urheber_a_mockup"),
 (None,[(RE+"Schalter Taster - Öffner und Schließer - E_2105107/10 Schalter Taster Öffner  Schließer.pdf",1),(RE+"Das Relais als Schalter - Elektrotechnik_2105114/11 Das Relais.pdf",1),(RE+"Das Relais als Schalter - Elektrotechnik_2105114/11 Das Relais.pdf",3)],
  "TECHNIK · ELEKTROTECHNIK","Materialpaket\nSchalter und Relais","Öffner, Schließer, Taster und Relais",["2 Materialien","mit Lösungen","Steuerung"],"Steuerungstechnik einfach","relais_paket_a_mockup"),
 (S+"antiprop.pdf",[1,2,3],"MATHE · KLASSE 7","Antiproportionale\nZuordnungen","Einführung mit Tabellen und Sachaufgaben",["4 Seiten","4 Aufgaben","mit Lösung"],"Mehr Leute, weniger Zeit","antiprop_a_mockup"),
]
for pdf,pg,fach,t,u,ch,fuss,out in P:
    mockup(pdf,pg,fach,t,u,ch,fuss,f"out/{out}.jpg")
