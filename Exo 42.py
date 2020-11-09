def insertEtoile(a):
    b = "";
    c= len(a);
    for i in range(0,c):
        b= b+ a[i]+ "*" ;
    return b;
a = "Test";
print(insertEtoile(a));