sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

for key in sample_dict.keys():
    print(f'{key:<10} = {sample_dict[key]:>10}')

for k,v in sample_dict.items():
    print(f'{k:<10} = {v:>10}')
#######################################
list=["name","surname","city"]
d={}
for key in list:
    if key in sample_dict:
        d[key]=sample_dict[key]
print(d)
#######################################
for key in list:
    x=sample_dict.pop(key, "Błąd")
    print(x)
#######################################
#for i in sample_dict.values():
#    if i=="Jones":
#        print("true")
#        break
#    else:
#        print("false")

if "Jones" in sample_dict.values():
    print("True")
else:
    print("false")