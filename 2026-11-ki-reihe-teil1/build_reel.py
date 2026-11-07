import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_reel import render_video
from PIL import Image
os.chdir(os.path.dirname(os.path.abspath(__file__)))
# 1080x1350-Slides in 1080x1920 Reel-Rahmen (Safe Zone 250..1500)
outs = []
for i in range(1, 10):
    s = Image.open(f"teil1_{i}.png").convert("RGB")
    bg = s.getpixel((540, 5))
    sc = 1250 / 1350
    t = s.resize((int(1080 * sc), 1250), Image.LANCZOS)
    c = Image.new("RGB", (1080, 1920), bg)
    c.paste(t, ((1080 - t.width) // 2 - 40, 250))
    c.save(f"reel_{i}.png"); outs.append(f"reel_{i}.png")
render_video(outs, "reel.mp4", sec=5)
