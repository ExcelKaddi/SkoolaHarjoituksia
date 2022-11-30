foo = [2,3,4]
length = len(foo)
def val(value):
    v = value[0] + value[1] + value[2]
    va = v/length
    print(va)
val(foo)