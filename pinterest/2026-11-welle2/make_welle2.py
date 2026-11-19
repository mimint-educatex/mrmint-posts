import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
P = [
 ("reflexion",[1,2],"PHYSIK · KLASSE 7/8","Reflexion\ndes Lichts","Strahlenverlauf am Spiegel zeichnen",["2 Seiten","3 Aufgaben","Zeichenübungen"],"Reflexionsgesetz anwenden","reflexion_a_mockup"),
 ("caesar",[1,2],"INFORMATIK · KLASSE 7","Caesar-\nVerschlüsselung","Ver- und Entschlüsseln üben",["2 Seiten","mit Lösung","Expertenaufgabe"],"Codes knacken im Informatikunterricht","caesar_a_mockup"),
 ("otto",[1,2,4],"TECHNIK · KLASSE 9","Ottomotor","Viertakt- und Zweitaktmotor erklärt",["4 Seiten","6 Fragen","mit Musterlösung"],"Infotext, Fragen und Beschriftung","ottomotor_a_mockup"),
 ("prozent_paket",[1,2,3],"MATHE · KLASSE 7","Materialpaket\nProzentrechnen","Mit Prozentstreifen und Dreisatz",["7 Materialien","Dreisatz","Prozentstreifen"],"Alle drei Größen sicher berechnen","prozent_paket_a_mockup"),
 ("binom_paket",[1,2,3],"MATHE · KLASSE 8/9","Materialpaket\nBinomische Formeln","Einführung, Übung und Faktorisieren",["5 Materialien","Einführung","Übung"],"Alle drei Formeln in einem Paket","binom_paket_a_mockup"),
]
for k,pg,fach,t,u,ch,fuss,out in P:
    mockup(f"src/{k}.pdf",pg,fach,t,u,ch,fuss,f"out/{out}.jpg")
