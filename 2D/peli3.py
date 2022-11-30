import pgzrun,math
import time
import random

#Viholliset
hank2 = Actor('hank')
hank2.x = 0
hank2.y = 10
skyler = Actor('skyler')
skyler.x = 0
skyler.y = 10

#BreakingBad Logo
logo = Actor('logo')
logo.x = 450
logo.y = 120

#Mike
hahmo = Actor('mike')
hahmo.x = 450
hahmo.y = 120

#3 Eri krystallit
alien = Actor('alien')
alien.x = 0
alien.y = 10
alien2 = Actor('alien')
alien2.x = 0
alien2.y = 500
alien3 = Actor('alien2')
alien2.x = 0
alien2.y = 200

#Taustakuva
background = Actor('background')
#tuco
tuco = Actor('todd')
tuco.x = 20
tuco.y = 700

#gusfring
gus = Actor('gus')
gus.x = 20
gus.y = 700

#veri
veri = Actor('damage')
veri.x = 500
veri.y = 700

#Waltteri
kk = Actor('kaiku')
kk.x = random.randint(450,550)
kk.y = 500

#STAMINA LOAD
load = Actor('stamina')
load.x = 245
load.y = 130

#ENDMENU
endwalt = Actor('207')
endwalt.x = 500
endwalt.y = 500

#Valuet
sekuntikello = 0
pisteet = 0 
veri.angle = 0
elämät = 100

#Koko
WIDTH = 950
HEIGHT =900
stamina = 100

#Onko Waltteri elossa
kk.kuolema = False
def kuolematrue():
    kk.kuolema = True

#Pisteet
def points():
    global pisteet
    pisteet += 10

#Gus antaa staminaa
def points_gus():
    global stamina
    if stamina<100:
        stamina+=1

#STAMINAreset
def staminareset():
    global stamina
    stamina=100

#TIMERreset
def timereset():
    global sekuntikello
    sekuntikello=0
    Aika()

#POINTreset
def pistereset():
    global pisteet
    pisteet = 0 
#HPreset
def hpreset():
    global elämät
    elämät = 100

#Animaatio + SlowMotion(FPS)
def verianimaaatio():
    if kk.kuolema==False:
        veri.angle += 0.3
        veri.draw()

#Mike 60S VAIKENNUS
def mike():
    hahmo.draw()

def tuco2():
    tuco.draw()
#Ajastin
def Aika():
    global sekuntikello
    if kk.kuolema==False:
        sekuntikello += 1
        timer()
def timer():
    clock.schedule(Aika, 1.0)        
#RUN-STAMINA
def jaksaminen():
    global stamina
    stamina -= 1
    if stamina<=0:
        stamina = 0
#HP MÄÄRÄ
def miinus():
    global elämät
    elämät -= 1
    if elämät == 0:
        kuolematrue()
        elämät += 100
#Piirtämisen aloitus ja Musiikki
timer()
def draw():
    #Jos Waltteri ei ole kuollut
    if kk.kuolema==False:
        screen.clear()
        music.play('theme')
        music.set_volume(0.2)
#Hahmojen Piirto 
        background.draw()
        alien.draw()
        alien2.draw()
        alien3.draw()
        hank2.draw()
        logo.draw()
        skyler.draw()
        kk.draw()
        gus.draw()
        alien.angle += 0.3
        alien2.angle -= 0.3
        alien3.angle += 0.15
#Yläkulma Teksti
        screen.draw.text("LIIKE: WASD TAI NUOLINÄPPÄIMET", (560,10), fontsize=32)																							
        screen.draw.text("JUOKSEMINEN: SHIFT + LIIKE", (560,35), fontsize=32)
        screen.draw.text("60 SEC = HPRESET", (560,60), fontsize=32)
#Päivittyvät tekstit   
        screen.draw.text(f"PISTEET: " + str(pisteet), (10, 40), fontsize=50)
        screen.draw.text(f"AIKA HENGISSÄ: " + str(sekuntikello), (10, 5), fontsize=50)
        screen.draw.text(f"HP: " + str(elämät), (10, 75), fontsize=50)
        screen.draw.text(f"STAMINA: "+ str(stamina), (10, 110), fontsize=50)
#Vaikeutus + Osuminen
        if sekuntikello>=60:
            mike()
        if sekuntikello>=120:
            tuco2()
#HP RESET AT 60S
        if sekuntikello==60 or sekuntikello==120 or sekuntikello==180 or sekuntikello==240 or sekuntikello==300:
            hpreset()
#Viholliseen osuminen  + Veri      
        if skyler.colliderect(kk) or hank2.colliderect(kk) or hahmo.colliderect(kk) and sekuntikello>=60 or tuco.colliderect(kk) and sekuntikello>=120:
            miinus()
            verianimaaatio()
#Krystalliiin osuminen 
        if alien.colliderect(kk):
            points()            
            alien.x = random.randint(-20, 780)
            alien.y = random.randint(-20, 780)
        if alien2.colliderect(kk):
            points()
            alien2.x = random.randint(-20, 780)
            alien2.y = random.randint(-20, 780)
        if alien3.colliderect(kk):
            points()
            alien3.x = random.randint(-20, 780)
            alien3.y = random.randint(-20, 780)
#GusFringiin osuminen + Staminan Lisäys 
        if gus.colliderect(kk):    
            points_gus()              
            if stamina<100:
                load.draw()
    #Jos WALTER WHITE Kuolee
    if kk.kuolema==True:
        lasku = sekuntikello/60
        minuuteiksi = round(lasku, 2)
        #MENU
        screen.clear()
        background.draw()
        endwalt.draw() 
        screen.draw.text(f"TULOKSESI", (400, 350), fontsize=50)
        screen.draw.text(f"PISTEET: "+ str(pisteet), (240, 400), fontsize=100)
        screen.draw.text("TEKIJÄ: -KAIKU- ", (415, 580), fontsize=32)
        screen.draw.text("RESTART -SPACE- ", (415, 620), fontsize=32)
        if keyboard[keys.SPACE]:
            kk.kuolema = False
            #AloitusPaikanResets
            kk.x = random.randint(450,550)
            kk.y = random.randint(450,550)
            #StatsResets
            staminareset()
            timereset()
            pistereset()
        if sekuntikello>=60:
            screen.draw.text(f"SELVISIT: " + str(minuuteiksi) + " MIN", (240, 480), fontsize=100)
        if sekuntikello<=60:
            screen.draw.text(f"SELVISIT: "+ str(sekuntikello) + " SEC", (240, 480), fontsize=100)
            
  
def update():

#krystallit 
    alien.x -= 4
    alien.y -= 4
    alien.x %= WIDTH
    alien.y %= HEIGHT
    alien2.x -= -2
    alien2.y -= -2
    alien2.x %= WIDTH
    alien2.y %= HEIGHT
    alien3.x -= 7
    alien3.y -= 3
    alien3.x %= WIDTH
    alien3.y %= HEIGHT
    hahmo.x -= 7
    hahmo.y -= 3
    hahmo.x %= WIDTH
    hahmo.y %= HEIGHT

#tappavat-viholliset
    hank2.x -= -7
    hank2.y -= -4
    hank2.x %= WIDTH
    hank2.y %= HEIGHT
    skyler.x -= -4
    skyler.y -= -10
    skyler.x %= WIDTH
    skyler.y %= HEIGHT
    tuco.x -= 5
    tuco.y -= 10
    tuco.x %= WIDTH
    tuco.y %= HEIGHT

#waltteri valkoinen
    kk.y %= HEIGHT
    kk.x %= WIDTH

#gusfring
    gus.x -= 3
    gus.y -= 3
    gus.x %= WIDTH
    gus.y %= HEIGHT 

#Kävely WASD ja NUOLINÄPPÄIN
    if keyboard[keys.W] or keyboard[keys.UP]:
        kk.y -= 5
    if keyboard[keys.S] or keyboard[keys.DOWN]:
        kk.y += 5
    if keyboard[keys.A] or keyboard[keys.LEFT]:
        kk.x -= 5
    if keyboard[keys.D] or keyboard[keys.RIGHT]:
        kk.x += 5

#Juokseminen WASD + SHIFT AND NUOLINÄPPÄIN + SHIFT 
    if stamina>0 and keyboard[keys.LSHIFT] and keyboard[keys.W] or stamina>0 and keyboard[keys.LSHIFT] and keyboard[keys.UP]:
        kk.y -= 7
        jaksaminen()
    if stamina>0 and keyboard[keys.LSHIFT] and keyboard[keys.S] or stamina>0 and keyboard[keys.LSHIFT] and keyboard[keys.DOWN]:
        kk.y += 7
        jaksaminen()
    if stamina>0 and keyboard[keys.LSHIFT] and keyboard[keys.A] or stamina>0 and keyboard[keys.LSHIFT] and keyboard[keys.LEFT]:
        kk.x -= 7
        jaksaminen()
    if stamina>0 and keyboard[keys.LSHIFT] and keyboard[keys.D] or stamina>0 and keyboard[keys.LSHIFT] and keyboard[keys.RIGHT]:
        kk.x += 7
        jaksaminen()
pgzrun.go()