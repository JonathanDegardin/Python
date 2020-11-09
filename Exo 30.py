listnombre = [4,5,6,4,5,2,1,89,45,2,4]
list = set([]);
listnombre2 = [42,12,5,78,89]
v=0;
for i in listnombre:
    for j in listnombre2:
        if i not in list:
            if i == j :
                print("Les deux listes possèdent la valeur",i);
                v=v+1
                list.add(i);
if v==0:
    print("Les deux listes ne contiennent aucune valeure en commun");