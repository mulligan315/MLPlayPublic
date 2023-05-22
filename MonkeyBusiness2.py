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

def low_prime_array(num):
    primes=[2,3,5,7,11,13,17,19,23]
    prime_remainders_dict=dict()
    for prime in primes:
        prime_remainders_dict[prime]=num % prime
    return prime_remainders_dict

    
def update_primes(squared,operand,amount,remainders):
    for prime in remainders:
        value=remainders[prime]
        if squared==True:
            remainder=value*value
        elif operand=='*':
            remainder=value*amount
        elif operand=='+':
            remainder=value+amount
        new_remainder = remainder % prime
        remainders[prime] = new_remainder
    return remainders
    

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
            remainders=low_prime_array(int(item))
            item_list.append(remainders)
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
for monk in monkeys:
    print(monk[items])
    print()
print()
        
for x in range(0,10000):
    for monk in monkeys:
        for item in monk[items]:
            squared=False
            operand, calc_num = monk[operation].split(' ')
            if calc_num=='old':
                squared=True
            else:
                calc_num=int(calc_num)
            new_item=update_primes(squared,operand,calc_num,item)
            
            if new_item[monk[divisor]]==0:
                monkeys[monk[ifTrue]][items].append(new_item)
            else:
                monkeys[monk[ifFalse]][items].append(new_item)
            monk[inspections]+=1
        monk[items]=[]

print(monkeys)
activity=[]
for monk in monkeys:
    activity.append(monk[inspections])
print(activity)
activity.sort(reverse=True)

print(activity[0]*activity[1])


