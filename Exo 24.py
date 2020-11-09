a = input("Saisir votre mot : ");
v=0;
for i in range(len(a)//2):
    if a[i] != a[-i-1]:
        v=v+1;
if v > 0:
    print(a,"n'est pas un palindrome");
else:
    print(a,"est un palindrome");