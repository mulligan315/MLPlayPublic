import ast

def Compare(left,right):
    print('\tComparing',left,'to',right)
    if left==[] and right != []:
        print('left is []. List is in right order')
        return True
    elif left !=[] and right == []:
        print('right is []. List is in wrong order')
        return False
    elif isinstance(left,int) and isinstance(right,int):
        if left < right:
            print(left,'is less than',right)
            print('List is in right order')
            return True
        if left > right:
            print(left,'is greater than',right)
            print('List is in wrong order')
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
            print(left, 'is shorter than', right)
            print('List is in right order')
            return True
        elif len(left) > len(right):
            print(right, 'is shorter than', left)
            print('List is in wrong order')
            return False
        
file = 'PacketData.txt'
packetpairs=[]
index_counter=0


with open(file,'rt',encoding='utf-8-sig') as packet_data:
    counter=1
    for line in packet_data:
        if counter % 3==0:
            counter+=1
            continue
        elif counter % 3==1:
            packet=[]
            packet.append(ast.literal_eval(line.strip()))
            counter+=1
            continue
        elif counter % 3 ==2:
            packet.append(ast.literal_eval(line.strip()))
            packetpairs.append(packet)
            counter+=1
            continue
        
index=0

for pair in packetpairs:
    index+=1
    print('PAIR',index,':')
    left=pair[0]
    right=pair[1]
    result = Compare(left,right)
    if result==True:
        index_counter+=index
        print('Counter is now',index_counter,'\n')
    elif result==False:
        print('Counter remains',index_counter,'\n')
    elif result==None:
        continue


print(index_counter)