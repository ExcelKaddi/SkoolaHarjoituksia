taulukko = ["Alma","Bill","Crubbe","Dirf","Embu"]
pituus = len(taulukko)
laskuri = 1
listanlaskuri = 0

while True:
    print(laskuri, taulukko[listanlaskuri])
    laskuri += 1
    listanlaskuri += 1
    if listanlaskuri>=pituus:
        break