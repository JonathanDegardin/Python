b=input("Veuillez saisir un nombre : ");
v = 0;
for i in range(1,int(b)+1):
    if int(b)%i ==0:
        v=v+1;
if v>2:
    print("Votre nombre n'est pas premier");
else:
    print("Votre nombre est premier");