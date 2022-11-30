import random

arvo = 1
laskuri = 1
while True:
    print(arvo)
    x = random.randint(1,6)
    arvo += x
    laskuri += 1
    if arvo>=100:
        print("100")
        break
print("Lukua kasvatettiin",laskuri+1,"kertaa")