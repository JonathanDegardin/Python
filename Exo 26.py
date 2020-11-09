a = input("Saisissez votre message : ").split(" ");
b  = len(a);
for i in range(0,b):
    if a[i].startswith("a"):
        print(a[i]);
