def funkcja(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
    return kwargs

print(funkcja(imie="Konrad",nazwisko="Mrugała",wiek=20))