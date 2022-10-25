x=int(input("Podaj pierwsza liczbę: "))
y=int(input("Podaj drugą liczbę: "))
if y<x:
    x,y=y,x     #zamiana liczb
while x<=y:
    if x%2:
        x+=1
        continue
    print(x, end=' ')
    x+=1