def find(lista, wartość):
    wynik = []
    a=0
    for i in lista:
        if i==wartość:
            wynik.append(a)
        a+=1
    return wynik


print(find([1,2,6,54,6,78,2,4,2],2))
