import random
x = int(input("1 vai 0: " ))
rand = random.uniform(0,1)
if rand>0.5 and x==1:
    print("Voitit")
if rand<0.5 and x==1:
    print("Hävisit")
if rand<0.5 and x==0:
    print("Voitit")
if rand>0.5 and x==0:
    print("Hävisit")
print("Numero oli", rand)