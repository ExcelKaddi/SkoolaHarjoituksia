def functio(a, b, c, d, e):
    laskuri = 0
    while True:
        lista = [a, b, c, d, e]
        pituus = len(lista)
        if lista[laskuri] % 2:
            print(lista[laskuri])
        if laskuri==pituus-1:
            break
        laskuri+=1
functio(8, 4, 7, 3, 5)
