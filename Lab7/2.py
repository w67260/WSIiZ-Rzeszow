import numpy as np
macierz=np.random.randint(low=0,high=100,size=(5,5))
print(macierz)

print("Wartość max: ",macierz.max())
print("Wartość min: ",macierz.min())

print("Max wiersz:",macierz.max(axis=1))
print("Max kolumna:",macierz.max(axis=0))
print("Min wiersz:",macierz.min(axis=1))
print("Min kolumna:",macierz.min(axis=0))