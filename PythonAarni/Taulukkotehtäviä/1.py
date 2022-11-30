foo = [2,3,7,5]

def val(value):
    if len(foo)==3:
        v = value[0] + value[1] + value[2]
    if len(foo)==4:
        v = value[0] + value[1] + value[2] + value[3]
    print(v)
val(foo)