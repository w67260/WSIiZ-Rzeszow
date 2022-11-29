def funkcja(imie, wiek=20):
    '''
    Funkcja wypisuje na ekranie imię oraz wiek.
    :param imie:
    :param wiek:
    :return:
    '''
    print(imie,wiek)

funkcja("Konrad","Mrugała")
funkcja("Konrad", 20)
funkcja(wiek=20, imie="Konrad")

print(funkcja.__doc__)
print(help(funkcja))

funkcja("Konrad")