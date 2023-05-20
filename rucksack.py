file = 'rucksackdata.txt'

with open(file,encoding='utf-8-sig') as ruck_data:
    ruck_list=list(ruck_data)

results=[]
score=0
    
for line in ruck_list:
    modded_line = line.removesuffix('\n')
    length=int(len(modded_line)/2)
    line_left=modded_line[:length]
    line_right=modded_line[length:]
    left=set(line_left)
    right=set(line_right)
    print(line_left,line_right)
    results.append(list(left.intersection(right)))
    
for letter in results:
    ascii_val=ord(letter[0])
    if ascii_val<97:
        ascii_val=ascii_val-64+26
        
    else:
        ascii_val=ascii_val-96
        
    score+=ascii_val    
print(score)
