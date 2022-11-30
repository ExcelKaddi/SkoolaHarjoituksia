foo = [2,3,4,5]
bar = [15,100]
lista = []
toinen = []
kolmas = []
neljäs = []
vikalista = []

def listat(lista1,lista2):
    laskin = 0
    while True:
        laskuri = 0
        if laskuri>=0:
            if laskin==0:
                x = lista1[laskin]
                a = lista2[laskuri]
                lista.append(x)
                lista.append(a)
                laskuri += 1
                laskin += 1
            if laskin==3:
                x = lista1[laskin-1]
                a = lista2[laskuri]
                kolmas.append(x)
                kolmas.append(a)
                laskin += 1 
                if laskin==4:
                    x = lista1[laskin-1]
                    a = lista2[laskuri+1]
                    neljäs.append(x)
                    neljäs.append(a)
        if laskuri==1:
            x = lista1[laskin]
            a = lista2[laskuri]
            toinen.append(x)
            toinen.append(a)
            laskin += 2 
        if laskin==4:
            break
                
listat(foo, bar)
vikalista.append(lista)
vikalista.append(toinen)
vikalista.append(kolmas)
vikalista.append(neljäs)
print(vikalista)
