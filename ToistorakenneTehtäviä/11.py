list = ["1",2,4, "Alma",10, 20, [12,23], "Bill","Crubbe",5,"Dirf","Embu"]
laskuri = 0

while True:
    x = isinstance(list[laskuri],str)
    if x==False:
        print("Se on numero!")
    if x==True:
        print("Se on sana!")
    laskuri += 1
    if len(list)==laskuri:
        break