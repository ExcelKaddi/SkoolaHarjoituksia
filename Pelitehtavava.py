#Pelitehtavava 17.11.2022
#Tee oliopohjainen peli.
#Paahenkilo kulkee 10x10 kentalla, aluksi hanella on 100 energiaa.
#Kentta on kaksiulotteinen taulukko.
#Kulkeminen tapahtuu nuoli- tai wasd nappaimilla.
#kentalla on 10 hyttysta (hyttysolioita) satunnaisissa paikoissa.
#Jos pelaaja menee samaan ruutuun kuin hyttynen, hanen energiansa vahenee 20.
#Pelissa on aarre satunnaisessa ruudussa.
#Jos pelaaja menee aarre-ruutuun, han voittaa.
#Peliluuppi voidaan toteuttaa "while-input"-rakenteella, Pygamea tai hiirta ei tarvita

#A) Toteuta ja testaa peli.

#B) Paranna pelia, niin, etta se on oikeasti pelattava, eika voitto ole vain satunnainen.
import random
import time

rN0 = random.randint(1, 10)
rN1 = random.randint(1, 10)
rN2 = random.randint(1, 10)
rN3 = random.randint(1, 10)
rN4 = random.randint(1, 10)
rN15 = random.randint(1, 10)
rN16 = random.randint(1, 10)
rN17 = random.randint(1, 10)
rN18 = random.randint(1, 10)
rN19 = random.randint(1, 10)
randomx = [rN0, rN1, rN2, rN3, rN4, rN15, rN16, rN17, rN18, rN19]
rN5 = random.randint(1, 10)
rN6 = random.randint(1, 10)
rN7 = random.randint(1, 10)
rN8 = random.randint(1, 10)
rN9 = random.randint(1, 10)
rN10 = random.randint(1, 10)
rN11 = random.randint(1, 10)
rN12 = random.randint(1, 10)
rN13 = random.randint(1, 10)
rN14 = random.randint(1, 10)
randomy = [rN5, rN6, rN7, rN8, rN9, rN10, rN11, rN12, rN13, rN14]

#Voitto

apos = random.randint(1,10)
vpos = random.randint(1,10)

#Pelaajan X,Y
a = 1
v = 1
e = 100
def energia():
    global e
    e-=20
def liike():
    global a
    a+=1
def liike2():
    global v
    v-=1
def liike3():
    global v
    v+=1
def liike4():
    global a
    a-=1

#Aloitus
while True:

    x = input("Minne haluat liikkua: ")
    time.sleep(0.2)
    if x=="W":
        if a>1:
            print("Pelaaja liikkui ylös.")
            liike4()
        if a==1:
            print("Seinä tuli vastaan.")
    if x=="A":
        if v>1:
            print("Pelaaja liikkui vasemmalle.")
            liike2()
        if v==1:
            print("Seinä tuli vastaan.")
    if x=="D":
        if v<10:
            print("Pelaaja liikkui oikealle.")
            liike3()
        if v==10:
            print("Seinä tuli vastaan.")
    if x=="S":
        if a<10:
            print("Pelaaja liikkui alas.")
            liike()
        if a==10:
            print("Seinä tuli vastaan.")
    if a==apos and v==vpos:
        time.sleep(0.2)
        input("Löysit palkinnon ja voitit")
        exit()
    if a==randomx[0] and v==randomy[0] or a==randomx[1] and v==randomy[1] or a==randomx[2] and v==randomy[2] or a==randomx[3] and v==randomy[3] or a==randomx[4] and v==randomy[4] or a==randomx[5] and v==randomy[5] or a==randomx[6] and v==randomy[6] or a==randomx[7] and v==randomy[7] or a==randomx[8] and v==randomy[8] or a==randomx[9] and v==randomy[9]:
        energia()
        time.sleep(0.2)
        print("Osuit viholliseen!")
        print("Nyt sinun energiamääräsi on vain", e)

        if e==0:
            input("Hävisit pelin")
            exit()
    time.sleep(0.2)
    print("Sijaintisi on, y=",a,"x =",v)
    