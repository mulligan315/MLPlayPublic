import ast

def Compare(left,right):
    #print('\tComparing',left,'to',right)
    if left==[] and right != []:
        #print('left is []. List is in right order')
        return True
    elif left !=[] and right == []:
        #print('right is []. List is in wrong order')
        return False
    elif isinstance(left,int) and isinstance(right,int):
        if left < right:
            #print(left,'is less than',right)
            #print('List is in right order')
            return True
        if left > right:
            #print(left,'is greater than',right)
            #print('List is in wrong order')
            return False
        if left==right:
            return None
    elif isinstance(left,int) and isinstance(right,list):
        left=[left]
        return Compare(left,right)
    elif isinstance(left,list) and isinstance(right,int):
        right=[right]
        return Compare(left,right)
    elif isinstance(left,list) and isinstance(right,list):
        cycles=min(len(left),len(right))
        for item in range(cycles):
            result=Compare(left[item],right[item])
            if result==None:
                continue
            else:
                return result
        if len(left) < len(right):
            #print(left, 'is shorter than', right)
            #print('List is in right order')
            return True
        elif len(left) > len(right):
            #print(right, 'is shorter than', left)
            #print('List is in wrong order')
            return False
        
file = 'PacketData.txt'
packets=[]
index_counter=0


with open(file,'rt',encoding='utf-8-sig') as packet_data:
    
    for line in packet_data:
        if line !='\n':
            packets.append(ast.literal_eval(line.strip()))
    packets.append([[2]])
    packets.append([[6]])
#for packet in packets:
    #print('\n',packet,'\n')        
        
index=0
was_a_swap=True

while(was_a_swap):
    was_a_swap=False
    for packet_index in range(1,len(packets)):

        left=packets[packet_index-1]
        right=packets[packet_index]
        result = Compare(left,right)
        if result==True:
            print('no swap\n')
        elif result==False:
            print('swapped!\n')
            was_a_swap=True
            packets[packet_index],packets[packet_index-1]=packets[packet_index-1],packets[packet_index]

        elif result==None:
            print('boom')


for index, packet in enumerate(packets):
    if packet==[[2]]:
        index1=index+1
    if packet==[[6]]:
        index2=index+1

answer=index1*index2

print('[[2]] is at',index1,'and [[6]] is at',index2,'Answer is',answer)
