def potęga(liczby,potęgi):
    wynik=[]
    if len(liczby)==len(potęgi):
        for i in range(len(liczby)):
            wynik.append(liczby[i]**potęgi[i])
    return wynik

print(potęga([2,4,5,6],[1,0,2,2]))