def luku(a, b, c, d, e):
    lista = [a, b, c, d, e]
    lista.sort()
    print("Suurin numero on", lista[-1])
    print("Pienin numero on", lista[0])
    keskiarvo = a + b + c + d + e
    lasku = keskiarvo/5
    print("Keskiarvo on", lasku)
luku(-253, 2531, 523, 2, 5)
