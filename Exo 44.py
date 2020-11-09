def nombreMajOuMin(a):
    nombreMaj = 0
    nombreMin = 0
    for lettre in a:
        if (lettre.isupper()):
            nombreMaj = nombreMaj + 1
        else:
            if lettre.islower():
                nombreMin = nombreMin + 1
    return (nombreMaj, nombreMin)
a = "TeeEeESt"
print("Le nombre de majuscules est : ", nombreMajOuMin(a)[0])
print("Le nombre de minuscules est : ", nombreMajOuMin(a)[1])

