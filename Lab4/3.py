zwierzeta=[]
x=int(input("Podaj ilość zwierząt: "))
while x>0:
    a=input("Podaj zwierzeta: ")
    zwierzeta.append(a)
    x-=1
zwierzeta.sort()
print(zwierzeta)
print(zwierzeta[0],zwierzeta[-1],zwierzeta[-2],zwierzeta[-3])
print("Długość listy: ",len(zwierzeta))