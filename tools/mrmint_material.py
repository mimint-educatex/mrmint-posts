"""MrMint Material-Helfer fuer Material-Posts (AB/KA-Screenshots) im Mint-2.0-Stil.

Ergaenzt mrmint_mint2.py um alles, was man fuer echte Material-Screenshots braucht:
Zuschnitt per Weissraum-Analyse, Wasserzeichen (Pflicht, IP-Schutz), Rahmen mit Schatten
und gestapelte Seiten fuer das Cover. Ersetzt die alten Helfer aus dem Skill-Ordner
(scripts/build_slides_template.py), die nicht mehr verwendet werden.

Nutzung:
    from mrmint_mint2 import *
    from mrmint_material import *
    crop = content_box("seite-1.png")                       # nie nach Augenmass croppen
    paste_framed_image(img, "seite-1.png", (80, y, 1000, 1100), crop=crop)
    card = make_card("seite-1.png", crop, 520); stack_card(img, card, (540, 760), -4)
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

from mrmint_mint2 import BODY, MINT, WHITE

__all__ = ["content_box", "add_shadow", "add_watermark", "paste_framed_image",
           "make_card", "stack_card"]


def content_box(path, pad=24, threshold=245, min_ink=0.002):
    """Zuschnitt-Grenzen (left, top, right, bottom) per Helligkeitsanalyse.

    Zeilen/Spalten gelten als leer, wenn weniger als min_ink ihrer Pixel dunkler als
    threshold sind. So werden weisse Seitenraender entfernt, ohne Inhalt abzuschneiden.
    """
    g = np.asarray(Image.open(path).convert("L"))
    ink = g < threshold
    rows = np.where(ink.mean(axis=1) > min_ink)[0]
    cols = np.where(ink.mean(axis=0) > min_ink)[0]
    if len(rows) == 0 or len(cols) == 0:
        raise ValueError(f"Kein Inhalt gefunden in {path} (Seite leer?)")
    h, w = g.shape
    return (max(0, int(cols[0]) - pad), max(0, int(rows[0]) - pad),
            min(w, int(cols[-1]) + 1 + pad), min(h, int(rows[-1]) + 1 + pad))


def add_shadow(img, box, blur=18, offset=10, opacity=70):
    left, top, right, bottom = box
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(
        [left + offset, top + offset, right + offset, bottom + offset],
        radius=14, fill=(20, 40, 35, opacity))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    base = img.convert("RGBA")
    base.alpha_composite(layer)
    img.paste(base.convert("RGB"))


def add_watermark(img, box, text="MrMint", font_size=30, spacing_x=200, spacing_y=85,
                  angle=-28, opacity=65):
    """Diagonales Wasserzeichen ueber den Bereich box. Pflicht auf jedem Material-Screenshot."""
    left, top, right, bottom = box
    w, h = right - left, bottom - top
    diag = int((w ** 2 + h ** 2) ** 0.5) + 120
    wm = Image.new("RGBA", (diag, diag), (0, 0, 0, 0))
    wd = ImageDraw.Draw(wm)
    font = BODY(font_size, "Bold")
    for row, ty in enumerate(range(0, diag, spacing_y)):
        shift = (spacing_x // 2) if row % 2 else 0
        for tx in range(-spacing_x, diag, spacing_x):
            wd.text((tx + shift, ty), text, font=font, fill=(120, 120, 120, opacity))
    wm = wm.rotate(angle, resample=Image.BICUBIC)
    cx, cy = wm.width // 2, wm.height // 2
    wm = wm.crop((cx - w // 2, cy - h // 2, cx - w // 2 + w, cy - h // 2 + h))
    region = img.crop(box).convert("RGBA")
    img.paste(Image.alpha_composite(region, wm).convert("RGB"), box)


def paste_framed_image(img, path, box, crop=None):
    """Screenshot in box einpassen: Schatten, Wasserzeichen, duenner Mint-Rahmen.

    crop=None schneidet automatisch per content_box() zu.
    Gibt die tatsaechlich belegte Flaeche (left, top, right, bottom) zurueck.
    """
    left, top, right, bottom = box
    max_w, max_h = right - left, bottom - top
    shot = Image.open(path).convert("RGB").crop(crop or content_box(path))
    scale = min(max_w / shot.width, max_h / shot.height)
    size = (int(shot.width * scale), int(shot.height * scale))
    shot = shot.resize(size, Image.LANCZOS)
    px, py = left + (max_w - size[0]) // 2, top + (max_h - size[1]) // 2
    frame = (px - 2, py - 2, px + size[0] + 2, py + size[1] + 2)
    add_shadow(img, frame)
    img.paste(shot, (px, py))
    add_watermark(img, (px, py, px + size[0], py + size[1]))
    ImageDraw.Draw(img).rounded_rectangle(frame, radius=6, outline=MINT, width=3)
    return frame


def make_card(path, crop, target_w):
    """Seite als Karte (mit Wasserzeichen und Mint-Rand) fuer gestapelte Cover."""
    shot = Image.open(path).convert("RGB").crop(crop or content_box(path))
    shot = shot.resize((target_w, int(shot.height * target_w / shot.width)), Image.LANCZOS)
    add_watermark(shot, (0, 0, shot.width, shot.height))
    card = Image.new("RGB", (shot.width + 12, shot.height + 12), MINT)
    card.paste(shot, (6, 6))
    return card


def stack_card(img, card, center, rotation):
    """Karte leicht gedreht mit Schatten auf img setzen (mehrfach aufrufen fuer einen Stapel)."""
    rot = card.convert("RGBA").rotate(rotation, expand=True, resample=Image.BICUBIC)
    x, y = center[0] - rot.width // 2, center[1] - rot.height // 2
    shadow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    shadow.paste(Image.new("RGBA", rot.size, (20, 40, 35, 85)), (x + 12, y + 12), rot.split()[-1])
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))
    base = img.convert("RGBA")
    base.alpha_composite(shadow)
    base.alpha_composite(rot, (x, y))
    img.paste(base.convert("RGB"))
