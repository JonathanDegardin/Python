Voyelles = ['a','e','i','o','u','y'];
b=input("Choisissez votre message : ");
a = len(b);
compte = 0;
for i in range(0,a):
    if b[i] in Voyelles:
        compte = compte +1;
print("Le message contient",compte,"voyelles");
