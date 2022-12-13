import random
def gra():
    x=random.randint(0,20)
    y=0
    while True:
        y+=1
        liczba=int(input("Podaj liczbę: "))
        if liczba==x:
            print(f"Gratulacje! Liczba prób: {y}")
            return
        elif liczba>x:
            print("Wylosowana liczba jest mniejsza")
        else:
            print("Wylosowana liczba jest większa")

gra()