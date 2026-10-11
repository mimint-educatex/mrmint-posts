from PIL import Image, ImageDraw, ImageFont
import math
W,H=1080,1920
WHITE=(255,255,255);MINT=(44,168,158);DG=(20,80,63);GRAY=(74,74,74);LIGHT=(232,246,244)
F="/usr/share/fonts/truetype/dejavu/"
sb=lambda s:ImageFont.truetype(F+"DejaVuSerif-Bold.ttf",s)
b=lambda s:ImageFont.truetype(F+"DejaVuSans-Bold.ttf",s)
r=lambda s:ImageFont.truetype(F+"DejaVuSans.ttf",s)
M=80;N=6
LOGO=Image.open("/root/.claude/skills/synced/7b6f9acb-f888-464a-9a84-8ff2842a54b8_427bbd9f-23d7-480a-9007-ea84013b29d5/mrmint-instagram-post/assets/mrmint-logo.png").convert("RGBA")
TOP=260  # Reel-Safe-Zone oben
def base(no):
    img=Image.new("RGB",(W,H),WHITE);d=ImageDraw.Draw(img)
    d.text((M,TOP),"MrMint",font=b(34),fill=DG)
    t="MATHE";w=d.textlength(t,font=b(22))+40
    d.rounded_rectangle([M,TOP+52,M+w,TOP+94],radius=21,fill=MINT);d.text((M+20,TOP+61),t,font=b(22),fill=WHITE)
    lg=LOGO.resize((130,int(LOGO.height*130/LOGO.width)));img.paste(lg,(W-M-130-120,TOP-10),lg)
    return img,d
def wrap(d,text,font,mw):
    out=[];cur=""
    for w in text.split():
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=mw: cur=t
        else: out.append(cur);cur=w
    out.append(cur);return out
def block(d,y,text,font,fill,lh,mw=W-2*M-120):
    for l in wrap(d,text,font,mw): d.text((M,y),l,font=font,fill=fill);y+=lh
    return y
def frac(d,cx,cy,n,m,size,col):
    f=b(size);w=max(d.textlength(n,font=f),d.textlength(m,font=f))+20
    d.text((cx,cy-10),n,font=f,fill=col,anchor="mb");d.line([(cx-w/2,cy),(cx+w/2,cy)],fill=col,width=7)
    d.text((cx,cy+10),m,font=f,fill=col,anchor="mt")
# 1 Titel
img,d=base(1)
y=block(d,560,"Vier Grundvorstellungen",sb(80),DG,96)
y=block(d,y,"zum Bruch",sb(80),MINT,96)
y=block(d,y+50,"Wer nur rechnet, ohne sie zu kennen, scheitert spätestens beim Vergleichen und Ordnen.",r(44),GRAY,60)
frac(d,W//2,y+220,"3","4",140,MINT)
img.save("r1.png")
# 2 Teil eines Ganzen
img,d=base(2)
d.text((M,480),"1",font=sb(130),fill=MINT)
y=block(d,640,"Teil eines Ganzen",sb(76),DG,92)
y=block(d,y+20,"Ein Ganzes in 4 gleich große Teile zerlegen, 3 davon nehmen.",r(44),GRAY,60)
cx,cy,R=W//2,y+330,250
for i in range(4):
    a0=-90+i*90;a1=a0+90
    d.pieslice([cx-R,cy-R,cx+R,cy+R],a0,a1,fill=MINT if i<3 else LIGHT,outline=WHITE,width=8)
d.ellipse([cx-R,cy-R,cx+R,cy+R],outline=DG,width=6)
frac(d,W//2,cy+R+150,"3","4",100,DG)
img.save("r2.png")
# 3 Anteil einer Menge
img,d=base(3)
d.text((M,480),"2",font=sb(130),fill=MINT)
y=block(d,640,"Anteil einer Menge",sb(76),DG,92)
y=block(d,y+20,"3/4 von 12 Schülern: 12 in 4 Gruppen teilen, 3 Gruppen nehmen.",r(44),GRAY,60)
y0=y+80;r0=44;gap=130
for g in range(4):
    gx=M+60+g*230
    d.rounded_rectangle([gx-20,y0-20,gx+180,y0+400],radius=24,fill=LIGHT if g<3 else (245,245,245),outline=MINT if g<3 else (210,210,210),width=4)
    for k in range(3):
        d.ellipse([gx+80-r0,y0+40+k*gap-r0+20,gx+80+r0,y0+40+k*gap+r0+20],fill=MINT if g<3 else (200,200,200))
d.text((W//2,y0+500),"9 von 12 Schülern",font=b(52),fill=DG,anchor="mm")
img.save("r3.png")
# 4 Ergebnis einer Division
img,d=base(4)
d.text((M,480),"3",font=sb(130),fill=MINT)
y=block(d,640,"Ergebnis einer Division",sb(76),DG,92)
y=block(d,y+20,"3 Pizzen gerecht auf 4 Kinder verteilen. Jedes Kind bekommt 3/4 Pizza.",r(44),GRAY,60)
yc=y+260
d.text((W//2-150,yc),"3 : 4  =",font=b(110),fill=DG,anchor="mm")
frac(d,W//2+200,yc,"3","4",110,MINT)
block(d,yc+220,"Diese Vorstellung trägt später bis zu Dezimalzahlen und Prozent.",b(44),DG,60)
img.save("r4.png")
# 5 Zahl auf dem Zahlenstrahl
img,d=base(5)
d.text((M,480),"4",font=sb(130),fill=MINT)
y=block(d,640,"Eine Zahl auf dem Zahlenstrahl",sb(76),DG,92)
y=block(d,y+20,"3/4 ist eine eigene Zahl zwischen 0 und 1, nicht nur ein Stück Pizza.",r(44),GRAY,60)
ly=y+260;x0,x1=M+40,W-M-40
d.line([(x0,ly),(x1,ly)],fill=DG,width=8)
for i in range(5):
    x=x0+(x1-x0)*i/4;d.line([(x,ly-30),(x,ly+30)],fill=DG,width=6)
d.text((x0,ly+70),"0",font=b(56),fill=DG,anchor="mm");d.text((x1,ly+70),"1",font=b(56),fill=DG,anchor="mm")
xp=x0+(x1-x0)*3/4
d.ellipse([xp-30,ly-30,xp+30,ly+30],fill=MINT)
frac(d,xp,ly-170,"3","4",90,MINT)
block(d,ly+180,"Damit können Kinder Brüche vergleichen und ordnen.",b(44),DG,60)
img.save("r5.png")
# 6 CTA
img,d=base(6)
y=block(d,600,"Erst Vorstellung,",sb(88),DG,104)
y=block(d,y,"dann Rechenregel.",sb(88),MINT,104)
y=block(d,y+50,"Übungsblätter zum Bruchrechnen mit Lösungen findest du auf eduki unter MrMint.",r(46),GRAY,64)
block(d,y+60,"Speichern für die nächste Bruch-Einheit!",b(48),DG,64)
img.save("r6.png")
