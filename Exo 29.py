listnombre = [4,5,6,4,5,2,1,89,45,2,4]
list = set([]);
i =0
while i < len(listnombre):
    if listnombre[i] not in list :
        list.add(listnombre[i]);
        i=i+1;
    else :
        listnombre.remove(listnombre[i]);

print (listnombre);