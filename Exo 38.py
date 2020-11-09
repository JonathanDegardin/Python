a = "Python est un langage de programmation".split();
b = len(a)
premier = a[0]
dernier = a[b-1]
a.pop(b-1)
a.pop(0)
final = " ".join(a)
a = dernier + " " + final + " " + premier
print(a)