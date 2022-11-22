values=[10,20,30]
keys=["ten","twenty","thirty"]

d=dict(zip(keys, values))
print(d)
#print(list(zip(keys,values)))
d={}
for i in range(len(values)):
    d[keys[i]]=values[i]
print(d)


d2=dict(thirty=30,forty=40,fifty=50)
print(d2)


d.update(d2)
print(d)