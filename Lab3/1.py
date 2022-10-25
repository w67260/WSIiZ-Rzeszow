x=int(input("Podaj pierwsza liczbę: "))
y=int(input("Podaj drugą liczbę: "))
if y<x:
    x,y=y,x     #zamiana liczb
while x<y:
    print(x)
    x+=1