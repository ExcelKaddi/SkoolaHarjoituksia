foo = ["2","3","4","5","5"]
bar = [10,123,421,3] 
lista = []
def listat(lista1,lista2):
    laskuri = 0
    toinen = -1
    while True:
        if laskuri<len(bar):
            x = str(lista1[laskuri])+lista2[laskuri]
            lista.append(x)
            laskuri+=1
        if laskuri==len(bar):
            toinen += 1
            x = str(lista1[toinen])+lista2[laskuri]
            lista.append(x)
            if toinen==len(bar)-1:
                break
listat(bar, foo)
print(lista)
