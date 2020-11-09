import itertools
listNombre = [1,2,3,4]
permutations = itertools.permutations(listNombre)
allList = list(permutations)
print ("Voici toutes les possibilités de listes issu de permutation", allList)