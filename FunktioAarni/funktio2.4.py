def luku(a):
    fibo = [0,1]
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
luku(15)
