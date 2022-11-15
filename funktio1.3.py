laskuri = 0
lista = [3,3,3,4,2,20,3,3,3,1,2]
x = len(lista)

while True:
    if laskuri==x:
        break
    if lista[laskuri] % 2:
        turha = 0
    else:
        print(lista[laskuri])
    laskuri+=1
