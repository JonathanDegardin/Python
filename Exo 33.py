a=input("Saisissez votre message : ");
b= len(a)
for i in range(0,b):
    if i == 0 or i%2 == 0 :
        print(a[i]);