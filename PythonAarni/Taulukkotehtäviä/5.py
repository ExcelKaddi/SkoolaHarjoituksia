foo = [2,3,4,5,2,5,2,1,5,6,6,3,232,32,12,42,2,3,4,5,2,5,2,1,5,6,6,3,232,32,12,42,2,3,4,5,2,5,2,1,5,6,6,3,232,32,12,42,2,3,4,5,2,5,2,1,5,6,6,3,232,32,12,42]
lenght = len(foo)
def val(value):
    laskuri = 0
    for i in range(lenght):
        if laskuri<lenght:
            print(value[laskuri])
            laskuri+=3
val(foo)