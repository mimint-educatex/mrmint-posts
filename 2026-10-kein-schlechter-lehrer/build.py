import sys, os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "tools"))
from mrmint_reel import *
os.chdir(os.path.dirname(os.path.abspath(__file__)))
TAG="SCHULALLTAG"
def pre(d,y=520):
    d.text((M,y),"Du bist kein schlechter Lehrer, wenn ...",font=r(40),fill=GRAY); return y+90
def card(d,y,text,col=LIGHT):
    lines=wrap(d,text,r(42),MAXW-80); h=len(lines)*56+50
    d.rounded_rectangle([M,y,W-M-120,y+h],radius=28,fill=col)
    yy=y+25
    for l in lines: d.text((M+40,yy),l,font=r(42),fill=DG); yy+=56
    return y+h+30
def phone(d,cx,cy,s=1.0):
    w,h=int(150*s),int(270*s)
    d.rounded_rectangle([cx-w//2,cy-h//2,cx+w//2,cy+h//2],radius=int(28*s),outline=DG,width=10)
    d.rounded_rectangle([cx-25,cy-h//2+18,cx+25,cy-h//2+28],radius=5,fill=DG)
    for k in (1,2):
        R=w//2+35*k
        d.arc([cx-R,cy-R,cx+R,cy+R],start=-28,end=28,fill=MINT,width=8)
        d.arc([cx-R,cy-R,cx+R,cy+R],start=152,end=208,fill=MINT,width=8)
# 1 Hook
img,d=base(TAG)
y=block(d,560,"Du bist kein",sb(96),DG,116)
y=block(d,y,"schlechter Lehrer,",sb(96),DG,116)
y=block(d,y,"wenn ...",sb(96),MINT,116)
y=block(d,y+60,"... es bei dir nicht so läuft wie bei Lehrer-Influencern.",r(46),GRAY,64)
img.save("r1.png")
# 2 Was man online sieht
img,d=base(TAG)
y=block(d,500,"Was ich online oft lese:",sb(58),DG,80)+40
for t in ["„Bei mir dürfen sie aufs Klo, ohne zu fragen.“","„Wer müde ist, darf schlafen. Wir reden danach.“","„Handys verbieten? Nein, Umgang beibringen!“"]:
    y=card(d,y,t)
y=block(d,y+30,"Klingt toll. Würde ich auch gern so machen.",b(44),MINT,60)
img.save("r2.png")
# 3 Klo
img,d=base(TAG)
y=pre(d)
y=block(d,y,"deine Schüler nicht ohne zu fragen aufs Klo dürfen.",sb(66),DG,82)+40
d.text((M,y),"fast 200",font=b(150),fill=MINT); y+=180
y=block(d,y,"dokumentierte Toilettengänge in einem Schuljahr haben einzelne Schüler bei uns. Nur im Unterricht gezählt.",r(44),GRAY,60)+30
y=block(d,y,"Oft geht es dabei nicht ums Klo, sondern ums Vapen oder um TikTok.",b(44),DG,60)
img.save("r3.png")
# 4 Handy
img,d=base(TAG)
y=pre(d)
y=block(d,y,"das Handy bei dir im Unterricht Pause hat.",sb(66),DG,82)+50
phone(d,W//2-60,y+150); y+=360
y=block(d,y,"Viele Jugendliche kommen in der Freizeit kaum vom Handy los.",r(44),GRAY,60)+20
y=block(d,y,"Zu Hause achtet oft niemand darauf, weil anderes gerade wichtiger ist.",b(44),DG,60)
img.save("r4.png")
# 5 Schule als Ort
img,d=base(TAG)
y=block(d,520,"Schule darf ein Ort sein,",sb(70),DG,86)
y=block(d,y,"an dem es nicht ständig am Hosenbein vibriert.",sb(70),MINT,86)+60
y=card(d,y,"Handy gezielt für den Unterricht nutzen: ja.")
y=card(d,y,"Dauernd erreichbar und aus der Konzentration gerissen: nein.")
img.save("r5.png")
# 6 Merksatz
img,d=base(TAG)
y=block(d,520,"Eine Methode ist nur so gut wie die Klasse, für die sie gemacht ist.",sb(66),DG,82)+50
y=block(d,y,"Was an einer Schule klappt, muss an deiner nicht klappen. Das ist kein Versagen. Das ist Kontext.",r(44),GRAY,62)+60
d.line([(M,y),(M+200,y)],fill=MINT,width=6); y+=40
y=block(d,y,"Unterrichtsmaterial für Mathe, Physik, Technik und IT: auf eduki unter MrMint",r(36),MINT,50)
img.save("r6.png")
contact_sheet([f"r{i}.png" for i in range(1,7)],"/tmp/claude-0/-home-claude-mrmint-posts/7adc0e5c-6540-519e-a6e8-367b31d968bf/scratchpad/sheet.png")
