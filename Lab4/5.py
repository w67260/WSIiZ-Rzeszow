import random as r
punkty=[round(r.uniform(0,51),2) for i in range(15)]
print(punkty)

print("Najmniejsza wartość: ",min(punkty))
print("Największa wartość: ",max(punkty))

x=float(input("Podaj liczbę do wyszukania: "))
if x in punkty:
    print(punkty.index(x))
else:
    print("Liczby nie ma w tej liście")

srednia=sum(punkty)/len(punkty)
print("Średnia to: ",round(srednia,2))

ponizej=[]
for i in punkty:
    if i<srednia:
        ponizej.append(i)
print("Poniżej - długość:", len(ponizej), ponizej)

powyzej=[i for i in punkty if i>srednia]
print("Powyżej - długość:", len(powyzej), powyzej)