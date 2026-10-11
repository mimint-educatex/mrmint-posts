"""MrMint Reel/TikTok Baukasten: 1080x1920 Slides + MP4.
Nutzung: import sys; sys.path.insert(0, "<repo>/tools"); from mrmint_reel import *
"""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
WHITE=(255,255,255); MINT=(44,168,158); DG=(20,80,63); GRAY=(74,74,74); LIGHT=(232,246,244)
F = "/usr/share/fonts/truetype/dejavu/"
sb = lambda s: ImageFont.truetype(F+"DejaVuSerif-Bold.ttf", s)   # Headlines
b  = lambda s: ImageFont.truetype(F+"DejaVuSans-Bold.ttf", s)
r  = lambda s: ImageFont.truetype(F+"DejaVuSans.ttf", s)
M = 80          # Seitenrand
TOP = 260       # Safe Zone oben (Reel/TikTok UI)
BOTTOM = 1500   # Inhalt nicht tiefer als hier (Caption/Buttons unten)
MAXW = W - 2*M - 120  # rechts Platz fuer Like/Share Buttons
LOGO = Image.open(os.path.join(os.path.dirname(__file__), "mrmint-logo.png")).convert("RGBA")

def base(subject="MATHE"):
    img = Image.new("RGB", (W, H), WHITE); d = ImageDraw.Draw(img)
    d.text((M, TOP), "MrMint", font=b(34), fill=DG)
    w = d.textlength(subject, font=b(22)) + 40
    d.rounded_rectangle([M, TOP+52, M+w, TOP+94], radius=21, fill=MINT)
    d.text((M+20, TOP+61), subject, font=b(22), fill=WHITE)
    lg = LOGO.resize((130, int(LOGO.height*130/LOGO.width)))
    img.paste(lg, (W-M-130-120, TOP-10), lg)
    return img, d

def wrap(d, text, font, mw=MAXW):
    out, cur = [], ""
    for w in text.split():
        t = (cur+" "+w).strip()
        if d.textlength(t, font=font) <= mw: cur = t
        else:
            if cur: out.append(cur)
            cur = w
    out.append(cur)
    for l in out:  # einzelnes Wort zu breit -> Fehler statt Ueberlauf
        if d.textlength(l, font=font) > W - 2*M:
            raise ValueError(f"Zu breit: '{l}', Schrift verkleinern")
    return out

def block(d, y, text, font, fill, lh, mw=MAXW):
    for l in wrap(d, text, font, mw):
        d.text((M, y), l, font=font, fill=fill); y += lh
    return y

def frac(d, cx, cy, n, m, size, col=MINT):
    f = b(size); w = max(d.textlength(n, font=f), d.textlength(m, font=f)) + 20
    d.text((cx, cy-10), n, font=f, fill=col, anchor="mb")
    d.line([(cx-w/2, cy), (cx+w/2, cy)], fill=col, width=max(4, size//20))
    d.text((cx, cy+10), m, font=f, fill=col, anchor="mt")

def render_video(pngs, out, sec=3.5, fade=0.5):
    """PNGs -> MP4 (H.264, 30fps, yuv420p, stiller AAC Track), weiche Ueberblendung."""
    n = len(pngs); D = sec + fade; total = sec*n + fade
    args = ["ffmpeg", "-y", "-loglevel", "error"]
    for p in pngs: args += ["-loop", "1", "-t", str(D), "-i", p]
    args += ["-f", "lavfi", "-t", str(total), "-i", "anullsrc=r=44100:cl=stereo"]
    chain, last = [], "[0]"
    for i in range(1, n):
        lab = f"[x{i}]"
        chain.append(f"{last}[{i}]xfade=transition=fade:duration={fade}:offset={sec*i}{lab}")
        last = lab
    chain.append(f"{last}format=yuv420p,fps=30[v]") if n > 1 else chain.append("[0]format=yuv420p,fps=30[v]")
    args += ["-filter_complex", ";".join(chain), "-map", "[v]", "-map", f"{n}:a",
             "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac",
             "-shortest", "-movflags", "+faststart", out]
    subprocess.run(args, check=True)
    return out

def contact_sheet(pngs, out, cols=3, scale=0.3):
    """Vorschau aller Slides in einem Bild fuer den Chat."""
    ims = [Image.open(p) for p in pngs]; w, h = int(W*scale), int(H*scale)
    rows = (len(ims)+cols-1)//cols
    sheet = Image.new("RGB", (cols*w+(cols+1)*20, rows*h+(rows+1)*20), (220,220,220))
    for i, im in enumerate(ims):
        sheet.paste(im.resize((w, h)), (20+(i%cols)*(w+20), 20+(i//cols)*(h+20)))
    sheet.save(out); return out
