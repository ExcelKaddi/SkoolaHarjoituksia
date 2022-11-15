def luku(a, b, c, d, e):
    laskuri = 0
    jono = [a, b, c, d, e]
    pituus = len(jono)
    pituus-=1
    while True:
        x = jono[laskuri]
        laskuri+=1
        lasku = x + jono[laskuri]
        print(lasku)
        if pituus==laskuri:
            break
luku(10, 1, 20, 1, 1)
