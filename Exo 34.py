notes = [12 , 4 , 14 , 11 , 18 , 13 , 7, 10 , 5 , 9 , 15 , 8 , 14 , 16];
a=len(notes);
auDessus=[];
for i in range(0,a):
    if notes[i] > 10:
        auDessus.append(notes[i])
print (auDessus);
