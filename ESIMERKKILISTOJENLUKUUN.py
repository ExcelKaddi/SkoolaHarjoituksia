foo = [23,34,"Kissa"]

for f in foo:
    print(f)

for f in range(len(foo)):
    print(foo[f])

laskuri = 0
while laskuri < len(foo):
    print(foo[laskuri])
    laskuri += 1