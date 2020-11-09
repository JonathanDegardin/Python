def nombreDivisibles(list,a):
    b = 0
    for i in list:
        if( i%a == 0):
            b = b + 1
    return b
list = [22,12,35,78,1,3]
a = 3
print("Le nombre d'élément de la liste qui sont divisible par ",a, " est : ",nombreDivisibles(list,a))