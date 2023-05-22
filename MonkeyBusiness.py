file='MonkeyParameters.txt'
monkey_specs=[]
monkeys=[]
name=0
items=1
operation=2
divisor=3
ifTrue=4
ifFalse=5
inspections=6

with open(file, encoding='utf-8-sig') as monkey_data:
    for line in monkey_data:
        monkey_specs.append(line.removesuffix('\n'))

for line in monkey_specs:
    
    if line.startswith('Monkey'):
        monkey=list()    
        num=line.split(' ')
        monkey.append(num[1].removesuffix(':'))
        
    elif line.startswith('  Start'):
        item_temp=line.removeprefix('  Starting items: ').split(', ')
        item_list=[]
        for item in item_temp:
            item_list.append(int(item))
        monkey.append(item_list)
    elif line.startswith('  Oper'):
        oper=line.removeprefix('  Operation: new = old ')
        monkey.append(oper)
    elif line.startswith('  Test'):
        test=int(line.removeprefix('  Test: divisible by '))
        monkey.append(test)
    elif line.startswith('    If true'):
        true=int(line.removeprefix('    If true: throw to monkey '))
        monkey.append(true)
    elif line.startswith('    If false'):
        false=int(line.removeprefix('    If false: throw to monkey '))
        monkey.append(false)
        monkey.append(0)
        monkeys.append(monkey)
        
for x in range(0,20):
    for monk in monkeys:
        for item in monk[items]:
            operand, calc_num = monk[operation].split(' ')
            if calc_num=='old':
                calc_num=item
            else:
                calc_num=int(calc_num)
            match operand:
                case '*':
                    worry_level=item*calc_num
                case '+':
                    worry_level=item+calc_num
            small_worry=worry_level//3
            if small_worry % monk[divisor]==0:
                monkeys[monk[ifTrue]][items].append(small_worry)
            else:
                monkeys[monk[ifFalse]][items].append(small_worry)
            monk[inspections]+=1
        monk[items]=[]

print(monkeys)
activity=[]
for monk in monkeys:
    activity.append(monk[inspections])
activity.sort(reverse=True)
print(activity[0]*activity[1])