listnombre = [4,5,6,4,5,2,1,89,45,2,4]
listPair =set([]);
listImpair=set([]);
for i in listnombre:
    if i%2 ==0:
        listPair.add(i);
    else:
        listImpair.add(i);
print(listImpair)
print(listPair)