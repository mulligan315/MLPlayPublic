from pprint import pprint as pp

file = "Calories.txt"

with open(file) as calories_input:
    calories=list(calories_input)

elves=[]
elf=[]
max_calories = 0

for line in calories:
    if line != '\n':
        elf.append(line)
    else:
        elves.append(elf)
        elf=[]
        
elves.append(elf)
for elf in elves:
    total_calories=0
    for item in elf:
        total_calories+=int(item)
    max_calories=max(total_calories,max_calories)
    
print(max_calories)
        