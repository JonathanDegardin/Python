b=input("Veuillez saisir un message : ");
a=input("Veuillez saisir le caractère à chercher : ");
c=len(b);
nombre = 0
for i in range(0,c):
    if b[i] == str(a) :
        print("Le caractère", a, "se trouve à la position : ",i);
    nombre=0;
