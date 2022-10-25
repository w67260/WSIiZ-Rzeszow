n=int(input("Podaj liczbę studentów: "))
i=1
while i<=n:
    suma=0
    punkty=int(input(f"Podaj punkty dla studenta {i}: "))
    suma+=punkty
    i+=1
srednia=suma/n
print(f"Średnia punktów to: {srednia}")