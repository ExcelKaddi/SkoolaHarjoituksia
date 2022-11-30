iät = [20,15,16,18,21,5]
laskuri = 0
while True:
    if iät[laskuri]>=18:
        print("täysi-ikäinen")
    if iät[laskuri]<18:
        print("ala-ikäinen")
    laskuri += 1
    if laskuri>=6:
        break