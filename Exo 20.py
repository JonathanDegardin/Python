a = input("Veuillez saisir un message : ");
b=len(a)
premier = a[0];
dernier = a[b-1];
a = a[1:b-1];
a2 = dernier + a +premier;
print(a2);
