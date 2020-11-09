b=input("Veuillez saisir un message : ");
a=len(b);
list = set({});
nombre = 0
for i in b:
    if i not in list :
        list.add(i);
        print("Le caractère", i, "apparait", b.count(i), "fois");
    nombre=0;
