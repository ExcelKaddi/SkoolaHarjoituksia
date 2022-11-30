import random

luku = 0
laskuri = 1
while True:
    print(luku)
    x1 = random.randint(1,2)
    x = random.randint(1,6)
    if x1==1:
        luku-=x
    if x1==2:
        luku+=x
    if luku<=-10:
        print(luku)
        print("Pelaaja 1 voitti")
        break
    if luku>=10:
        print(luku)
        print("Pelaaja 2 voitti")
        break
