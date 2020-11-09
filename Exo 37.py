a = " Python est un langage de programmation de haut niveau".split()
b = " Python est un langage interprété".split()
motsCommuns=set([])
for i in a:
    if(i in b):
        motsCommuns.add(i)
print("La liste des mots communs à a et b est : ",motsCommuns)