def dodawanie(x,y):
    suma=x+y
    return suma

def odejmowanie(x,y):
    roznica=x-y
    return roznica

def mnozenie(x,y):
    iloczyn=x*y
    return iloczyn

def dzielenie(x,y):
    if y!=0:
        iloraz=x/y
        return iloraz
    else:
        return "Nie dziel przez 0"

kalk={'+':dodawanie,'-':odejmowanie,'*':mnozenie,'/':dzielenie}
x=int(input("Podaj x: "))
y=int(input("Podaj y: "))
dzialanie=input("Podaj działanie(+,-,*,/): ")

print(kalk[dzialanie](x,y))