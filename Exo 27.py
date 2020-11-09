a = input("Saisissez votre message : ").split(" ");
b=len(a);
c=0;
motmax = "";
for i in range(0,b):
    if len(a[i])>c:
        c=len(a[i]);
        motmax = a[i];
print("le mot le plus long de votre chaine est ",motmax);
