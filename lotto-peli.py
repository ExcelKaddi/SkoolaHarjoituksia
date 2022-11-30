import random
def error():
    print("Error, Yritä uusiksi")
def lotto(amount,limit):
    lista = []
    lista2 = []
    oikeinmenneet = []
    #Generoi satunnaiset numerot
    for i in range(amount):
        satuinnaisluku = random.randint(1,limit)
        while True:
            if satuinnaisluku in lista:
                satuinnaisluku = random.randint(1,limit)
            if satuinnaisluku not in lista:
                lista.append(satuinnaisluku)
                break
    #Ottaa arvaukset inputilla
    for i in range(amount):
        while True:
            try:
                print("Arvaa lottonumero [",i+1,"/",len(lista),"]")
                e1 = int(input(""))
                if e1>limit:
                    error()
                else:
                    lista2.append(e1)
                    break
            except ValueError:
                error()
    #Katsoo oikeinolevat arvaukset
    for i in range(amount):
        if lista[i] in lista2:
            oikeinmenneet.append(lista[i])
    #Lopputulos > Voitto/Tappio 
    if len(oikeinmenneet)==amount:
        print("Voitit numeroilla",lista2)
    if len(oikeinmenneet)<amount:
        print("Hävisit")
        print("Sait",len(oikeinmenneet),"oikein")
        print("Oikeat voittonumerot olivat",lista2)

while True:
    lotto(7,41)
    print("Haluatko kokeilla uusiksi? Y/N")
    lopetus = input("")
    if lopetus=="N" or lopetus=="n":
        break