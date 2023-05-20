file = 'rucksackdata.txt'

with open(file,encoding='utf-8-sig') as ruck_data:
    ruck_list=list(ruck_data)

results=[]
score=0
counter=0
group=[]
    
for line in ruck_list:
    modded_line = set(line.removesuffix('\n'))
    counter+=1
    group.append(modded_line)
    if counter==3:
        set1=group[0].intersection(group[1])
        set2=group[2].intersection(set1)
        results.append(list(set2))
        counter=0
        group=[]

for letter in results:
    ascii_val=ord(letter[0])
    if ascii_val<97:
        ascii_val=ascii_val-64+26
        
    else:
        ascii_val=ascii_val-96
        
    score+=ascii_val    
print(score)  