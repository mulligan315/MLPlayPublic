file = 'RealSignals.txt'
signals=[]
frequency=1
cycle=0
values_per_cycle=[]

with open(file,encoding='utf-8-sig') as signals_data:
    for line in signals_data:
        signals.append(line.removesuffix('\n'))

for line in signals:
    if line=='noop':
        values_per_cycle.append((cycle,frequency))
        cycle+=1
        
        
    if line[0:4]=='addx':
        addx=line.split(" ")
        increment=addx[1]
        values_per_cycle.append((cycle,frequency))
        cycle+=1
        values_per_cycle.append((cycle,frequency))
        cycle+=1
        frequency+=int(increment)
        
print(values_per_cycle)

for crt,sprite in values_per_cycle:
    if crt % 40==0:
        print('')
    adj_crt=crt%40
    if(abs(sprite-adj_crt)<=1):
        print('#',end='')
    else:
        print('.',end='')
    