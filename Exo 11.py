b=input("Veuillez saisir un nombre : ");
a = 1;
while a<=int(b):
    if int(b)%a ==0:
        print(a,"est un diviseur de",b);
        a=a+1;
    else:
        a=a+1;

