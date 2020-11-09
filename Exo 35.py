a=input("Saisissez votre texte : ").split();
list=set([])
for i in a :
    if i not in list:
        list.add(i);
        print("La fréquence d'apparition de",i,"est" ,a.count(i));