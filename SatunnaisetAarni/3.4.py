import random
lista = ["miisu","kisu","joni","jäpi","jonne","eemil","jaakko","janne","moona","mari"]
lista2 = ["miisu","kisu","joni","jäpi","jonne","eemil","jaakko","janne","moona","mari"]
laskin = 0
while True:
    x = random.randint(0,len(lista)-1)
    lista.append(lista[x])
    print(lista[laskin])
    laskin+=1
    if lista[x] in lista2:
        lista2.remove(lista[x])
    if len(lista2)==0:
        print("Kaikki on toistettu kerran")
        break