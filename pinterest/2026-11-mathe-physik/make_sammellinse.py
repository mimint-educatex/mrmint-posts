import sys; sys.path.insert(0, "../../tools")
from pin_lib import mockup
mockup("src3/Sammellinse_Bildentstehung_ohne_Name.pdf", [3, 1, 4], "PHYSIK · KLASSE 7/8", "Sammellinse\nBildentstehung",
       "Bildkonstruktion mit drei Lichtstrahlen",
       ["4 Seiten", "mit Lösungen", "Optik"], "Zum Einführen und Üben", "out/sammellinse_a_mockup.jpg")
