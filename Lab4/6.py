lista=list(range(10))
print(lista)
lista[:0]=lista[-3:]
del lista[-3:]
print(lista)