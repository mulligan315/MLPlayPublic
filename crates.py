from pprint import pprint as pp

file='CratesMove.txt'
crate_list=[]
stacks=['',[],[],[],[],[],[],[],[],[]]

def slice_up_into_lists(text):
    if text[1] != ' ':
        stacks[1].append(text[1])
    if text[5] != ' ':        
        stacks[2].append(text[5])
    if text[9] != ' ':
        stacks[3].append(text[9])
    if text[13] != ' ':
        stacks[4].append(text[13])
    if text[17] != ' ':
        stacks[5].append(text[17])
    if text[21] != ' ':
        stacks[6].append(text[21])
    if text[25] != ' ':
        stacks[7].append(text[25])
    if text[29] != ' ':
        stacks[8].append(text[29])
    if text[33] != ' ':
        stacks[9].append(text[33])
        
def get_move_info(line):
    line=line.replace('move ','')
    line=line.replace('from ','')
    line=line.replace('to ','')
    line_values=line.split(' ')
    move_num=int(line_values[0])
    from_stack=int(line_values[1])
    to_stack=int(line_values[2])
    return move_num,from_stack,to_stack

with open(file,encoding='utf-8-sig') as crate_data:
    for line in crate_data:
        crate_list.append(line.removesuffix('\n'))
        
for line in crate_list:
    if line=='':
        continue
    if line[0]=='[':
        slice_up_into_lists(line)
    elif line[1]=='1':
        for stack in stacks:
            if stack !='':
                stack.reverse()
    elif line[0:4] == 'move':
        move, fr, to = get_move_info(line)
        for val in range(0,move):
            crate_value=stacks[fr].pop()
            stacks[to].append(crate_value)
                
answer=''
for val in range(1,10):
        answer+=stacks[val][-1]
        
print(answer)