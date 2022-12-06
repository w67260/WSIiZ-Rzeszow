import numpy as np
'''l=[]
for i in range(7,-1,-1):
    x=2**i
    l.append(x)
print(l)'''
l=[2**i for i in range(7,-1,-1)]
print(l)

wagi=np.array(l)
print(wagi)

liczba_bin=np.random.randint(low=0,high=2,size=8)
print(liczba_bin)

wynik=liczba_bin*wagi
print(wynik)

liczba_dzies=wynik.sum()
print(liczba_dzies)