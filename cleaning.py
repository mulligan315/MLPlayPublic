file = 'CleaningAssign.txt'

def return_set_from_string(range_string):
    ends=range_string.split('-')
    start=int(ends[0])
    end=int(ends[1])+1
    return set(range(start,end))

results=[]
counter = 0

with open(file,encoding='utf-8-sig') as clean_data:
    assign_list=list(clean_data)

for pairs in assign_list:
    pairs=pairs.removesuffix('\n')
    pairs_list=pairs.split(',')
    results.append(pairs_list)
    
#print(results)

for pairs in results:
    left=return_set_from_string(pairs[0])
    right=return_set_from_string(pairs[1])
    if left.issubset(right) or right.issubset(left):
        counter +=1
    
print(counter)