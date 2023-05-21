file='HeadMoves.txt'
moves_list=[]
head=[0,0]
tail=[0,0]
tail_locations=set()
tail_locations.add(tuple(tail))

with open(file, encoding='utf-8-sig') as move_data:
    for moves in move_data:
        moves_list.append(moves.removesuffix('\n'))
        
for moves in moves_list:
    direction, magnitude=moves.split(' ')
    magnitude=int(magnitude)
    
    for x in range(0,magnitude):
        if direction=='L':
            head[0]=head[0]-1
        if direction=='R':
            head[0]=head[0]+1
        if direction=='U':
            head[1]=head[1]+1
        if direction=='D':
            head[1]=head[1]-1
        horizontal_distance=head[0]-tail[0]
        vertical_distance=head[1]-tail[1]
        
        if horizontal_distance==2 and vertical_distance==0:
            tail[0]=tail[0]+1
        if horizontal_distance==2 and vertical_distance==1:
            tail[0]=tail[0]+1
            tail[1]=tail[1]+1
        if horizontal_distance==2 and vertical_distance==-1:
            tail[0]=tail[0]+1
            tail[1]=tail[1]-1
        
        if horizontal_distance==-2 and vertical_distance==0:
            tail[0]=tail[0]-1
        if horizontal_distance==-2 and vertical_distance==1:
            tail[0]=tail[0]-1
            tail[1]=tail[1]+1
        if horizontal_distance==-2 and vertical_distance==-1:
            tail[0]=tail[0]-1
            tail[1]=tail[1]-1            
        
        if vertical_distance==2 and horizontal_distance==0:
            tail[1]=tail[1]+1
        if vertical_distance==2 and horizontal_distance==1:
            tail[1]=tail[1]+1
            tail[0]=tail[0]+1
        if vertical_distance==2 and horizontal_distance==-1:
            tail[1]=tail[1]+1
            tail[0]=tail[0]-1
        
        if vertical_distance==-2 and horizontal_distance==0:
            tail[1]=tail[1]-1
        if vertical_distance==-2 and horizontal_distance==1:
            tail[1]=tail[1]-1
            tail[0]=tail[0]+1
        if vertical_distance==-2 and horizontal_distance==-1:
            tail[1]=tail[1]-1
            tail[0]=tail[0]-1
            
        new_tail=tuple(tail)
        tail_locations.add(new_tail)   
        
print(len(tail_locations))

        