"""MrMint Pinterest-Pins: 3 Layouts im 2:3-Format (1000x1500).

mockup   : Kopfband mit Titel, Cover vorn + 2 Innenseiten gefächert, 3 Fakten-Chips
nutzen   : große Aussage, Ausschnitt aus dem Material, Checkliste mit 4 Punkten
einblick : Titel, 3 Seiten nebeneinander mit Beschriftung (z. B. Auftrag/Tipps/Lösung)
"""
import os
import fitz
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
MOCHIY = os.path.join(HERE, "MochiyPopOne-Regular.ttf")
LOGO = os.path.join(HERE, "mrmint-logo.png")
POP = "/usr/share/fonts/truetype/google-fonts/Poppins-{}.ttf"
PETROL, DARK, BG, WHITE, MINT = "#2CA89E", "#14503F", "#EEF6F5", "#FFFFFF", "#BFE6E2"
W, H = 1000, 1500


def F(path, size):
    return ImageFont.truetype(path, size)


def pop(style, size):
    return F(POP.format(style), size)


def page_img(pdf, pno, width, clip=None):
    """Seite pno (1-basiert) rendern; clip = (x0,y0,x1,y1) in PDF-Punkten."""
    pg = fitz.open(pdf)[pno - 1]
    rect = fitz.Rect(*clip) if clip else pg.rect
    z = width / rect.width
    pix = pg.get_pixmap(matrix=fitz.Matrix(z, z), clip=rect)
    return Image.frombytes("RGB", (pix.width, pix.height), pix.samples)


def card(img, border=3, shadow=18):
    w, h = img.size
    out = Image.new("RGBA", (w + shadow * 2, h + shadow * 2), (0, 0, 0, 0))
    sh = Image.new("RGBA", out.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([shadow, shadow + 8, w + shadow, h + shadow + 8], fill=(0, 0, 0, 90))
    out.alpha_composite(sh.filter(ImageFilter.GaussianBlur(shadow / 2)))
    fr = img.convert("RGBA")
    ImageDraw.Draw(fr).rectangle([0, 0, w - 1, h - 1], outline="#222222", width=border)
    out.alpha_composite(fr, (shadow, shadow))
    return out


def fit(d, text, path, max_w, start, min_size=40):
    s = start
    while s > min_size:
        f = F(path, s)
        if max(d.textlength(l, font=f) for l in text.split("\n")) <= max_w:
            return f
        s -= 4
    return F(path, min_size)


def label(d, text, x=60, y=48, fill=DARK):
    f = pop("Bold", 30)
    d.rounded_rectangle([x, y, x + d.textlength(text, font=f) + 44, y + 52], radius=26, fill=fill)
    d.text((x + 22, y + 6), text, font=f, fill=WHITE)


def chips(d, items, y=1240):
    f = pop("Bold", 34)
    widths = [d.textlength(t, font=f) + 80 for t in items]
    gap = (W - 120 - sum(widths)) / max(len(items) - 1, 1)
    x = 60
    for t, w in zip(items, widths):
        d.rounded_rectangle([x, y, x + w, y + 64], radius=32, fill=WHITE, outline=PETROL, width=4)
        d.ellipse([x + 18, y + 20, x + 42, y + 44], fill=PETROL)
        d.text((x + 56, y + 10), t, font=f, fill=DARK)
        x += w + gap


def footer(im, d, line1, line2="Unterrichtsmaterial von MrMint auf eduki"):
    d.rectangle([0, 1340, W, H], fill=DARK)
    logo = Image.open(LOGO).convert("RGBA")
    logo.thumbnail((165, 134))
    bg = Image.new("RGBA", (logo.width + 16, logo.height + 16), WHITE)
    m = Image.new("L", bg.size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, bg.width, bg.height], radius=20, fill=255)
    bg.alpha_composite(logo, (8, 8))
    im.paste(bg, (50, 1352), m)
    d.text((262, 1368), line1, font=pop("Bold", 40), fill=WHITE)
    d.text((262, 1422), line2, font=pop("Medium", 30), fill=MINT)


def save(im, out):
    im.convert("RGB").save(out, quality=92)
    return out


def mockup(pdf, pages, fach, titel, untertitel, fakten, fuss, out):
    im = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 430], fill=PETROL)
    label(d, fach)
    tf = fit(d, titel, MOCHIY, W - 120, 120)
    d.multiline_text((60, 130), titel, font=tf, fill=WHITE, spacing=10)
    tb = d.multiline_textbbox((60, 130), titel, font=tf, spacing=10)
    d.text((62, tb[3] + 22), untertitel, font=pop("Bold", 38), fill=DARK)
    for pno, a, (x, y) in zip(pages[1:], [8, -7], [(470, 540), (40, 560)]):
        c = card(page_img(pdf, pno, 420)).rotate(a, expand=True, resample=Image.BICUBIC)
        im.alpha_composite(c, (x, y))
    fr = card(page_img(pdf, pages[0], 520))
    im.alpha_composite(fr, ((W - fr.width) // 2, 505))
    chips(d, fakten)
    footer(im, d, fuss)
    return save(im, out)


def nutzen(pdf, fach, frage, antwort, bild, punkte, fuss, out):
    """bild = (seite, clip) Ausschnitt; punkte = 4 kurze Zeilen."""
    im = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 570], fill=DARK)
    label(d, fach, fill=PETROL)
    tf = fit(d, frage, MOCHIY, W - 120, 104)
    d.multiline_text((60, 135), frage, font=tf, fill=WHITE, spacing=8)
    tb = d.multiline_textbbox((60, 135), frage, font=tf, spacing=8)
    af = fit(d, antwort, MOCHIY, W - 160, 92)
    aw = d.textlength(antwort, font=af)
    ab = d.textbbox((0, 0), antwort, font=af)
    y = tb[3] + 30
    d.rounded_rectangle([50, y - 6, 50 + aw + 40, y + ab[3] + 22], radius=24, fill=PETROL)
    d.text((70, y), antwort, font=af, fill=WHITE)
    pno, clip = bild
    img = page_img(pdf, pno, 600, clip)
    if img.height > 330:
        img = img.resize((int(img.width * 330 / img.height), 330))
    c = card(img, border=0)
    im.alpha_composite(c, ((W - c.width) // 2, 600))
    f = pop("Bold", 38)
    y = 640 + c.height
    for p in punkte:
        d.ellipse([70, y + 8, 110, y + 48], fill=PETROL)
        d.line([(80, y + 28), (88, y + 37), (101, y + 19)], fill=WHITE, width=6)
        d.text((134, y + 1), p, font=f, fill=DARK)
        y += 82
    footer(im, d, fuss)
    return save(im, out)


def einblick(pdf, pages, beschriftung, fach, titel, untertitel, fakten, fuss, out):
    im = Image.new("RGBA", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, 430], fill=PETROL)
    label(d, fach)
    tf = fit(d, titel, MOCHIY, W - 120, 110)
    d.multiline_text((60, 130), titel, font=tf, fill=WHITE, spacing=10)
    tb = d.multiline_textbbox((60, 130), titel, font=tf, spacing=10)
    d.text((62, tb[3] + 22), untertitel, font=pop("Bold", 38), fill=DARK)
    pw = 280
    xs = [36, 356, 676]
    for pno, x, lab, a in zip(pages, xs, beschriftung, [-3, 0, 3]):
        c = card(page_img(pdf, pno, pw), shadow=14).rotate(a, expand=True, resample=Image.BICUBIC)
        im.alpha_composite(c, (x - 8, 650))
        f = pop("Bold", 36)
        tw = d.textlength(lab, font=f)
        cx = x + 14 + pw // 2
        d.rounded_rectangle([cx - tw / 2 - 24, 580, cx + tw / 2 + 24, 636], radius=28, fill=DARK)
        d.text((cx - tw / 2, 585), lab, font=f, fill=WHITE)
    chips(d, fakten)
    footer(im, d, fuss)
    return save(im, out)
