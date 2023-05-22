file = 'RealSignals.txt'
signals=[]
frequency=1
cycle=0
strengths=[]

def check_cycle():
    if cycle==20 or cycle==60 or cycle==100 or cycle ==140 or cycle==180 or cycle==220:
        strengths.append(cycle*frequency)

with open(file,encoding='utf-8-sig') as signals_data:
    for line in signals_data:
        signals.append(line.removesuffix('\n'))

for line in signals:
    if line=='noop':
        cycle+=1
        check_cycle()
        
    if line[0:4]=='addx':
        addx=line.split(" ")
        increment=addx[1]
        cycle+=1
        check_cycle()
        cycle+=1
        check_cycle()
        frequency+=int(increment)
        
        
print(strengths)
print(sum(strengths))