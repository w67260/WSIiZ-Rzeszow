imiona=['Kasia','Tomek','Jan','Ola','Jerzy','Marek','Piotr','Zuzia','Bartek','Jacek']
print(imiona)

x=imiona[4]
imiona[4]=imiona[0]
imiona[0]=x
print(imiona)

imiona[5]='Konrad'
print(imiona)

del imiona[6]
print(imiona)

imiona.insert(0,"Konrad")
imiona.insert(1,"Gabriela")
imiona.insert(2,"Nikola")
print(imiona)

x=input("Podaj imię do usunięcia: ")
imiona.remove(x)
print(imiona)

