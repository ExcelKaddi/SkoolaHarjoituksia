import random
lista = [0,"kissa",5,"koira"]
while True:
    x1 = random.randint(0,len(lista)-1)
    del lista[x1]
    if len(lista)==1:
        print(lista[0])
        break