"""MrMint "Mint 2.0" Slide-Baukasten (ab Nov 2026 Standard fuer alle Posts).

Prinzip: Infopost wie bei Nachrichtenmedien. Profi-Schrift (Inter), viel Weissraum,
ein Gedanke pro Slide, keine Baukasten-Deko. Alle Funktionen pruefen Ueberlauf und
brechen mit Fehler ab, statt kaputte Slides zu erzeugen.

Nutzung:
    import sys, os; sys.path.insert(0, "<repo>/tools")
    from mrmint_mint2 import *
    P = Post(total=9, kicker_base="KI im Lehreralltag")
    img, d, y = P.cover("Teil 2", "Headline ...", "Unterzeile ...")
    ...
    P.save("ordner")            # PNGs 1080x1350 + contact.png
    P.reel("ordner")            # reel.mp4 1080x1920 (Instagram)
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")

# ---------- Masse & Farben (nicht aendern ohne Absprache mit Davide) ----------
W, H = 1080, 1350
M = 80                      # Seitenrand links/rechts
TEXT_W = W - 2 * M
BOTTOM = H - 210            # Inhalt darf nicht tiefer (Logo/Handle-Zone)
DG = (16, 72, 57)           # Dunkelgruen: Cover + Schluss-Slide
MINT = (44, 168, 158)       # Akzent: Kicker, Balken, Nummern
INK = (18, 26, 24)          # Headlines/Text auf Weiss
GREY = (96, 106, 103)       # Fliesstext
LIGHT = (233, 245, 242)     # EINZIGE Flaeche: Panel / "richtig"-Beispiel
RED = (190, 62, 50)         # nur fuer "falsch", "Achtung", "Namen bleiben draussen"
WHITE = (255, 255, 255)
ON_DARK = (205, 230, 224)   # Fliesstext auf Dunkelgruen
LOGO_COL = (46, 117, 92)


def _font(name, size):
    p = os.path.join(FONTS, name)
    if not os.path.exists(p):
        p = os.path.join("/usr/share/fonts/opentype/inter", name)
    if not os.path.exists(p):
        raise FileNotFoundError(f"Schrift fehlt: {name}. Nie auf DejaVu ausweichen!")
    return ImageFont.truetype(p, size)


HEAD = lambda s: _font("InterDisplay-ExtraBold.otf", s)
DISP = lambda s, w="SemiBold": _font(f"InterDisplay-{w}.otf", s)
BODY = lambda s, w="Regular": _font(f"Inter-{w}.otf", s)


def _logo(color):
    p = os.path.join(HERE, "mrmint-logo.png")   # NEUES Logo (Gesicht + Icons + Schriftzug)
    a = np.array(Image.open(p).convert("RGBA"))
    a[..., :3] = color
    return Image.fromarray(a)


LOGO_GREEN = _logo(LOGO_COL)
LOGO_WHITE = _logo(WHITE)

FORBIDDEN = ["—", "–"]   # Gedankenstriche sind verboten
FLOSKELN = ["Kurz zusammengefasst", "Profi-Trick", "Ehrlich gesagt", "Game-Changer", "Gamechanger"]


class LayoutError(Exception):
    pass


def check_text(s):
    for ch in FORBIDDEN:
        if ch in s:
            raise LayoutError(f"Gedankenstrich in: {s!r}")
    for f in FLOSKELN:
        if f.lower() in s.lower():
            raise LayoutError(f"KI-Floskel '{f}' in: {s!r}")


def wrap(d, s, font, maxw):
    check_text(s)
    out, cur = [], ""
    for w in s.split():
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = w
    out.append(cur)
    for l in out:
        if d.textlength(l, font=font) > maxw:
            raise LayoutError(f"Wort zu breit: {l!r}")
    return out


class Post:
    def __init__(self, total, kicker_base=""):
        self.total = total
        self.kicker_base = kicker_base
        self.slides = []        # (img, dark)

    # ----- Rahmen -----
    def _frame(self, kicker, dark):
        no = len(self.slides) + 1
        img = Image.new("RGB", (W, H), DG if dark else WHITE)
        d = ImageDraw.Draw(img)
        check_text(kicker)
        d.text((M, 72), kicker.upper(), font=BODY(24, "SemiBold"), fill=MINT)
        d.text((W - M, 72), f"{no}/{self.total}", font=BODY(24, "Medium"), fill=WHITE if dark else INK, anchor="ra")
        lg = LOGO_WHITE if dark else LOGO_GREEN
        l = lg.resize((130, int(lg.height * 130 / lg.width)), Image.LANCZOS)
        img.paste(l, (M, H - l.height - 56), l)
        d.text((W - M, H - 80), "@mrmint18", font=BODY(24, "Medium"), fill=(170, 200, 192) if dark else GREY, anchor="ra")
        return img, d

    def _push(self, img, dark, y):
        if y > BOTTOM:
            raise LayoutError(f"Slide {len(self.slides) + 1}: Inhalt endet bei y={y}, erlaubt {BOTTOM}. Text kuerzen.")
        self.slides.append((img, dark))

    # ----- Slide-Typen -----
    def cover(self, kicker, headline, sub):
        img, d = self._frame(f"{self.kicker_base} · {kicker}" if self.kicker_base else kicker, True)
        y = self.text(d, 260, headline, HEAD(92), WHITE, 104, maxlines=4)
        d.rectangle([M, y + 40, M + 120, y + 48], fill=MINT)
        y = self.text(d, y + 90, sub, BODY(36), ON_DARK, 52, mw=TEXT_W - 40, maxlines=3)
        return img, d, y

    def page(self, kicker, headline, body=None):
        """Normale Inhaltsslide: Kicker, Headline (max 3 Zeilen), optional Fliesstext."""
        img, d = self._frame(kicker, False)
        y = self.text(d, 200, headline, HEAD(76), INK, 88, maxlines=3)
        if body:
            y = self.text(d, y + 36, body, BODY(34), GREY, 50, maxlines=4)
        return img, d, y

    def end(self, kicker, headline, sub, next_part=None):
        img, d = self._frame(kicker, True)
        y = self.text(d, 240, headline, HEAD(84), WHITE, 96, maxlines=3)
        y = self.text(d, y + 40, sub, BODY(36), ON_DARK, 52, maxlines=4)
        if next_part:
            y += 70
            d.line([(M, y), (W - M, y)], fill=(60, 110, 96), width=2)
            d.text((M, y + 36), "NÄCHSTER TEIL", font=BODY(24, "SemiBold"), fill=MINT)
            y = self.text(d, y + 80, next_part, DISP(46), WHITE, 58, maxlines=2)
        return img, d, y

    def done(self, img, d, y, dark=False):
        self._push(img, dark, y)

    # ----- Bausteine -----
    def text(self, d, y, s, font, fill, lh, mw=TEXT_W, x=M, maxlines=None):
        lines = wrap(d, s, font, mw)
        if maxlines and len(lines) > maxlines:
            raise LayoutError(f"{len(lines)} Zeilen statt max {maxlines}: {s!r}")
        for l in lines:
            d.text((x, y), l, font=font, fill=fill)
            y += lh
        return y

    def quote(self, d, y, s, size=40):
        """Zitat/Prompt mit Mint-Balken links. Kein Kasten."""
        f = BODY(size, "Medium")
        lines = wrap(d, s, f, TEXT_W - 44)
        h = len(lines) * (size + 18)
        d.rectangle([M, y, M + 8, y + h], fill=MINT)
        for i, l in enumerate(lines):
            d.text((M + 44, y + 2 + i * (size + 18)), l, font=f, fill=INK)
        return y + h

    def panel(self, d, y, label, s, size=34):
        """EINE helle Flaeche pro Slide, z. B. Einstellungsfeld oder Prompt."""
        f = BODY(size)
        lines = wrap(d, s, f, TEXT_W - 80)
        h = 76 + len(lines) * (size + 16) + 30
        d.rectangle([M, y, W - M, y + h], fill=LIGHT)
        d.text((M + 40, y + 30), label.upper(), font=BODY(22, "SemiBold"), fill=MINT)
        for i, l in enumerate(lines):
            d.text((M + 40, y + 76 + i * (size + 16)), l, font=f, fill=INK)
        return y + h

    def numbered(self, d, y, items, size=38):
        """Nummerierte Liste mit grossen Mint-Ziffern, ohne Kreise/Kaesten."""
        for i, it in enumerate(items, 1):
            d.text((M, y - 4), str(i), font=HEAD(size + 10), fill=MINT)
            y = self.text(d, y, it, BODY(size, "Medium"), INK, size + 14, mw=TEXT_W - 70, x=M + 70) + 24
        return y

    def compare(self, d, y, l_label, l_lines, r_label, r_lines, size=52):
        """Falsch/Richtig nebeneinander. Rechts helle Flaeche."""
        cw = TEXT_W // 2
        d.text((M, y), l_label, font=BODY(28, "SemiBold"), fill=RED)
        d.text((M + cw + 30, y), r_label, font=BODY(28, "SemiBold"), fill=MINT)
        y += 60
        rows = max(len(l_lines), len(r_lines))
        h = 40 + rows * (size + 24)
        d.rectangle([M + cw, y, W - M, y + h], fill=LIGHT)
        for i in range(rows):
            if i < len(l_lines):
                check_text(l_lines[i])
                d.text((M, y + 20 + i * (size + 24)), l_lines[i], font=DISP(size, "Medium"), fill=(150, 156, 154))
            if i < len(r_lines):
                check_text(r_lines[i])
                d.text((M + cw + 30, y + 20 + i * (size + 24)), r_lines[i], font=DISP(size, "SemiBold"), fill=INK)
        return y + h

    def warn(self, d, y, s, size=34):
        """Ein roter Hinweissatz (sparsam, max. 1 pro Slide)."""
        return self.text(d, y, s, BODY(size, "SemiBold"), RED, size + 16)

    # ----- Ausgabe -----
    def save(self, folder, prefix="slide"):
        if len(self.slides) != self.total:
            raise LayoutError(f"{len(self.slides)} Slides gebaut, total={self.total}")
        os.makedirs(folder, exist_ok=True)
        paths = []
        for i, (img, _) in enumerate(self.slides, 1):
            p = os.path.join(folder, f"{prefix}_{i}.png"); img.save(p); paths.append(p)
        sc = 0.3; w, h = int(W * sc), int(H * sc)
        rows = (len(paths) + 2) // 3
        sheet = Image.new("RGB", (3 * w + 64, rows * (h + 16) + 16), (225, 225, 223))
        for i, (img, _) in enumerate(self.slides):
            sheet.paste(img.resize((w, h), Image.LANCZOS), (16 + (i % 3) * (w + 16), 16 + (i // 3) * (h + 16)))
        sheet.save(os.path.join(folder, "contact.png"))
        return paths

    def reel(self, folder, sec=5.0):
        """1080x1920 Reel: Slide verkleinert in Safe Zone (y 250..1500), Rand in Slide-Farbe."""
        import sys
        sys.path.insert(0, HERE)
        from mrmint_reel import render_video
        frames = []
        for i, (img, dark) in enumerate(self.slides, 1):
            bg = DG if dark else WHITE
            sc = 1250 / H
            t = img.resize((int(W * sc), 1250), Image.LANCZOS)
            c = Image.new("RGB", (1080, 1920), bg)
            c.paste(t, ((1080 - t.width) // 2 - 30, 250))
            p = os.path.join(folder, f"reel_{i}.png"); c.save(p); frames.append(p)
        return render_video(frames, os.path.join(folder, "reel.mp4"), sec=sec)
