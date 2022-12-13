def znaki(s):
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
        # if i in d.keys():
        #     d[i]+=1
        # else:
        #     d[i]=1
    return d

wynik=znaki("znaki napisu")
print(wynik)

for k in sorted(wynik):
    print(f"{k}:{wynik[k]}")