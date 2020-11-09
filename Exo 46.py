def motsCommuns(a, b):
    a2 = a.split()
    b2 = b.split()
    communs = []
    for mot in a2:
        if mot in b2:
            communs.append(mot)
    return communs
a = "Python est un langage de programmation"
b = "Python est orienté objet"
print(motsCommuns(a,b))
