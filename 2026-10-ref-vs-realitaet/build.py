import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "tools"))
from mrmint_reel import *

TAG = "REFERENDARIAT"
FOOT = 1430  # Footer innerhalb der Safe Zone


def frame(part, n, total=6, chevron=True):
    img, d = base(TAG)
    # zweite Pille "TEIL x/2" wie bei der Lehrprobe-Serie
    x0 = M + d.textlength(TAG, font=b(22)) + 40 + 14
    t = f"TEIL {part}/2"
    w = d.textlength(t, font=b(22)) + 40
    d.rounded_rectangle([x0, TOP+52, x0+w, TOP+94], radius=21, fill=LIGHT)
    d.text((x0+20, TOP+61), t, font=b(22), fill=DG)
    # Footer
    d.text((M, FOOT), "@mrmint18", font=r(30), fill=MINT)
    pn = f"{n}/{total}"
    d.text((W-M-120-d.textlength(pn, font=b(30)), FOOT), pn, font=b(30), fill=MINT)
    if chevron and n < total:
        cx, cy = W-M-150, FOOT-70
        for k in (0, 22):
            d.line([(cx+k-14, cy-18), (cx+k+4, cy), (cx+k-14, cy+18)], fill=MINT, width=6)
    return img, d


def stat(d, y, num, text, nc, tc):
    f = b(170); nw = d.textlength(num, font=f)
    d.text((M, y), num, font=f, fill=nc)
    x = M + nw + 36; mw = W-M-120-x
    lines = wrap(d, text, b(44), mw)
    yy = y + 105 - len(lines)*29
    for l in lines:
        d.text((x, yy), l, font=b(44), fill=tc); yy += 58


def accent(d, y):
    d.line([(M, y), (M+140, y)], fill=MINT, width=10)
    return y + 50


def card(d, y, head, text, fill=LIGHT, hc=MINT, tc=DG):
    lines = wrap(d, text, r(40), MAXW-80)
    h = 40 + 52 + len(lines)*54 + 30
    d.rounded_rectangle([M, y, W-M-120, y+h], radius=28, fill=fill)
    d.text((M+40, y+34), head, font=b(36), fill=hc)
    yy = y + 34 + 62
    for l in lines:
        d.text((M+40, yy), l, font=r(40), fill=tc); yy += 54
    return y + h + 28


def chip_rows(d, y, items, font=b(36)):
    x = M
    for it in items:
        w = d.textlength(it, font=font) + 56
        if x + w > W-M-120:
            x = M; y += 92
        d.rounded_rectangle([x, y, x+w, y+72], radius=36, fill=LIGHT)
        d.text((x+28, y+16), it, font=font, fill=DG)
        x += w + 18
    return y + 92


def eduki(d, y):
    return block(d, y, "Unterrichtsmaterial für Mathe, Physik, Technik und IT: auf eduki unter MrMint", r(32), GRAY, 44)


def spotlight(d, cx, top, bottom):
    # Scheinwerferkegel auf eine Bühne
    d.polygon([(cx-30, top), (cx+30, top), (cx+230, bottom), (cx-230, bottom)], fill=LIGHT)
    d.rounded_rectangle([cx-50, top-40, cx+50, top+10], radius=14, fill=DG)
    d.ellipse([cx-230, bottom-40, cx+230, bottom+40], fill=MINT)
    for sx in (-120, 0, 120):  # kleine Sterne als "Show"
        sy = top + 140 + (40 if sx else 0)
        d.regular_polygon((cx+sx, sy, 18), 4, rotation=45, fill=MINT)


def iceberg(d, y0):
    water = y0 + 170
    # Spitze ueber Wasser
    d.polygon([(330, water), (420, y0+20), (470, y0+60), (560, water)], fill=WHITE, outline=DG, width=6)
    d.text((620, y0+70), "Unterricht", font=b(44), fill=DG)
    d.ellipse([588, y0+92, 604, y0+108], fill=DG)
    # Wasserlinie
    d.rectangle([0, water, W, FOOT-40], fill=LIGHT)
    for x in range(0, W, 90):
        d.arc([x, water-14, x+90, water+14], start=180, end=360, fill=MINT, width=5)
    # Teil unter Wasser
    d.polygon([(330, water), (560, water), (760, water+230), (710, water+500),
               (440, water+580), (180, water+420), (220, water+170)], fill=MINT)
    items = ["Korrekturen", "Konferenzen", "Elterngespräche", "Aufsichten", "Organisation"]
    yy = water + 70
    for it in items:
        tw = d.textlength(it, font=b(38))
        d.text((465-tw/2, yy), it, font=b(38), fill=WHITE); yy += 82
    return water + 660


def scale(d, cy):
    cx = 500
    d.line([(cx, cy-30), (cx, cy+260)], fill=DG, width=10)
    d.rounded_rectangle([cx-110, cy+250, cx+110, cy+280], radius=12, fill=DG)
    lx, ly, rx, ry = cx-300, cy+60, cx+300, cy-60   # links schwer, rechts leicht
    d.line([(lx, ly), (rx, ry)], fill=DG, width=10)
    d.ellipse([cx-18, cy-18, cx+18, cy+18], fill=MINT)
    for (x, y, lab, col, big) in [(lx, ly, "Beziehung", MINT, True), (rx, ry, "Methode", GRAY, False)]:
        d.line([(x, y), (x-70, y+110)], fill=DG, width=4)
        d.line([(x, y), (x+70, y+110)], fill=DG, width=4)
        d.chord([x-110, y+60, x+110, y+170], start=0, end=180, fill=col)
        tw = d.textlength(lab, font=b(32))
        d.text((x-tw/2, y+180), lab, font=b(32), fill=col)
    return cy + 300


def teil1(out):
    os.makedirs(out, exist_ok=True)
    # 1 Hook
    img, d = frame(1, 1)
    y = block(d, 470, "Niemand hat mir im Ref gesagt,", sb(78), DG, 96)
    y = block(d, y, "dass Unterrichten nur der kleinste Teil meines Jobs wird.", sb(78), MINT, 96)
    y = accent(d, y+40)
    block(d, y, "Teil 1: Was das Ref dir nicht zeigt.", b(44), GRAY, 60)
    img.save(f"{out}/r1.png")
    # 2 Showstunde
    img, d = frame(1, 2)
    spotlight(d, 470, 470, 760)
    y = block(d, 860, "Die Lehrprobe heißt nicht umsonst Showstunde.", sb(64), DG, 80)
    y = block(d, y+30, "Das Ref zeigt Unterricht unter Idealbedingungen. Den echten Beruf zeigt es nicht.", r(42), GRAY, 58)
    img.save(f"{out}/r2.png")
    # 3 Vergleich
    img, d = frame(1, 3)
    y = block(d, 450, "Im Ref:", sb(64), GRAY, 80)
    stat(d, y, "1", "Stunde, 90 Minuten Planung", GRAY, GRAY)
    y += 240
    d.line([(M, y), (W-M-120, y)], fill=LIGHT, width=6); y += 40
    y = block(d, y, "Im Job:", sb(64), DG, 80)
    stat(d, y, "27", "Stunden pro Woche", MINT, DG)
    y += 240
    block(d, y, "Die 90 Minuten pro Stunde sind dann einfach weg.", r(42), GRAY, 58)
    img.save(f"{out}/r3.png")
    # 4 Eisberg
    img, d = frame(1, 4)
    y = block(d, 420, "Die bittere Wahrheit:", sb(58), DG, 74)
    y = block(d, y, "Unterricht ist nur die Spitze.", sb(58), MINT, 74)
    iceberg(d, y+10)
    img.save(f"{out}/r4.png")
    # 5 Klassenleitung
    img, d = frame(1, 5)
    y = block(d, 450, "Und mit Klassenleitung?", sb(70), DG, 86)
    y = block(d, y+10, "Kommt das alles noch dazu:", r(42), GRAY, 58) + 40
    y = chip_rows(d, y, ["Elternabende", "Zeugnisse", "Konflikte klären", "Ausflüge", "Absprachen", "Entschuldigungen", "Elternmails"])
    y = accent(d, y+40)
    block(d, y, "Und nichts davon hast du im Ref geübt.", b(46), DG, 62)
    img.save(f"{out}/r5.png")
    # 6 Cliffhanger
    img, d = frame(1, 6)
    y = block(d, 450, "Und was heißt das jetzt für deinen Unterricht?", sb(70), DG, 86)
    y = block(d, y+30, "Teil 2: Warum weniger Perfektion okay ist.", b(46), MINT, 62)
    y = block(d, y+50, "Was hat dich nach dem Ref am meisten überrascht? Schreib es in die Kommentare.", r(42), GRAY, 58)
    y = accent(d, y+50)
    eduki(d, y)
    img.save(f"{out}/r6.png")


def teil2(out):
    os.makedirs(out, exist_ok=True)
    # 1 Hook
    img, d = frame(2, 1)
    y = block(d, 470, "Du sitzt abends da und denkst:", sb(74), DG, 92)
    y = block(d, y+20, "„Im Ref war mein Unterricht besser.“", sb(74), MINT, 92)
    y = accent(d, y+40)
    block(d, y, "Lies weiter.", b(52), GRAY, 66)
    img.save(f"{out}/r1.png")
    # 2 Ehrlich
    img, d = frame(2, 2)
    y = block(d, 470, "Ehrlich gesagt: Vielleicht war er das sogar.", sb(70), DG, 86)
    y = block(d, y+40, "Im Ref hattest du Zeit für jedes Detail. Jetzt hast du 27 Stunden und alles, was unter der Wasserlinie liegt.", r(44), GRAY, 60)
    y = accent(d, y+50)
    block(d, y, "Aber das ist nicht die ganze Wahrheit.", b(46), DG, 62)
    img.save(f"{out}/r2.png")
    # 3 Kern (hervorgehoben)
    img, d = frame(2, 3, chevron=False)
    d.rounded_rectangle([M-20, 440, W-M-100, 1390], radius=40, fill=MINT)
    y = 520
    for l in wrap(d, "Du bist kein schlechter Lehrer, nur weil du keine Showstunden mehr hältst.", sb(74), MAXW-60):
        d.text((M+30, y), l, font=sb(74), fill=WHITE); y += 92
    y += 50
    d.line([(M+30, y), (M+170, y)], fill=WHITE, width=10); y += 50
    for l in wrap(d, "Du machst einfach einen anderen Job als im Ref.", b(46), MAXW-60):
        d.text((M+30, y), l, font=b(46), fill=WHITE); y += 62
    img.save(f"{out}/r3.png")
    # 4 Was zaehlt
    img, d = frame(2, 4)
    y = block(d, 440, "Was wirklich zählt:", sb(70), DG, 86)
    y = scale(d, y+130)
    block(d, y+40, "Beziehung und Klassenführung schlagen jede perfekte Methode.", b(46), DG, 62)
    img.save(f"{out}/r4.png")
    # 5 Tipps
    img, d = frame(2, 5, chevron=False)
    y = block(d, 430, "Weniger Zeit, kein schlechtes Gewissen:", sb(60), DG, 76) + 30
    y = card(d, y, "1. Bewährtes wiederverwenden", "Das ist nicht faul, das ist nachhaltig.")
    y = card(d, y, "2. Im Kollegium teilen", "Ein gutes Arbeitsblatt muss nicht jeder neu erfinden.")
    y = card(d, y, "3. Solide statt Show", "Nicht jede Stunde muss ein Highlight sein.")
    img.save(f"{out}/r5.png")
    # 6 Abschluss
    img, d = frame(2, 6)
    y = block(d, 470, "Hör auf, dich mit deinem Ref-Ich zu vergleichen.", sb(76), DG, 94)
    y = accent(d, y+40)
    y = block(d, y, "Was hat dir im 1. Dienstjahr geholfen, das schlechte Gewissen loszuwerden?", r(42), GRAY, 58)
    y = block(d, y+40, "Schreib es in die Kommentare.", b(42), MINT, 58)
    eduki(d, y+60)
    img.save(f"{out}/r6.png")


if __name__ == "__main__":
    t1, t2 = os.path.join(HERE, "teil1"), os.path.join(HERE, "teil2")
    teil1(t1); teil2(t2)
    sp = sys.argv[1] if len(sys.argv) > 1 else HERE
    contact_sheet([f"{t1}/r{i}.png" for i in range(1, 7)], f"{sp}/sheet1.png")
    contact_sheet([f"{t2}/r{i}.png" for i in range(1, 7)], f"{sp}/sheet2.png")
