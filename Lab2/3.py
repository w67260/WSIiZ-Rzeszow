print("1)dodawanie, 2)odejmowanie, 3)mnożenie, 4)dzielenie, 5)potęgowanie")
operacja=int(input("Wybierz numer operacji: "))

x=float(input("Podaj pierwszą liczbę: "))
y=float(input("Podaj drugą liczbę: "))

if operacja==1:
    wynik=x+y
elif operacja==2:
    wynik=x-y
elif operacja==3:
    wynik=x*y
elif operacja==4:
    if y==0:
        print("Nie można dzielić przez 0")
        exit()
    else:
        wynik=x/y
elif operacja==5:
    wynik=x**y
else:
    print("Niepoprawna operacja")
    exit()

print("Wynik:",wynik)