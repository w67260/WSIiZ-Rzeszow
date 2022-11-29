def funkcja(*args):
    max=args[0]
    for i in args[1:]:
        if i>max:
            max=i
    return max

print(funkcja(-1,21,23,4,32,-15,0,57,9))
####################################################
def funkcja(*args):
    if len(args)==0:
        return
    max=args[0]
    for i in args[1:]:
        if i>max:
            max=i
    return max
####################################################
def funkcja(num1,*args):
    max=num1
    for i in args:
        if i>max:
            max=i
    return max

print(funkcja(1))