def nombreOccurences(list, a):
    occ = 0
    for element in list:
        if element == a:
            occ = occ + 1
    return occ
list = [4, 2, 2, 2, 12, 12, 2, 5, 3, 2]
print("Le nombre d'occurrences de 2 dans la liste est : ", nombreOccurences(list, 2))