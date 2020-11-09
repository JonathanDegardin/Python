a = int(input("Veuillez saisir un nombre :  "))
# On utilise un compteur j
j = 0
for i in range(0,a):
    if(i**2 == a):
        j = j +1
if(j > 0):
    print("L'entier  ", a , " est un carré parfait")
else:
    print("l'entier ", a , " n'est pas est un carré parfait")

