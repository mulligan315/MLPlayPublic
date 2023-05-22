file='HeadMoves.txt'
moves_list=[]
snake=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

tail_locations=set()
tail_locations.add(tuple(snake[9]))

with open(file, encoding='utf-8-sig') as move_data:
    for moves in move_data:
        moves_list.append(moves.removesuffix('\n'))
        
for moves in moves_list:
    direction, magnitude=moves.split(' ')
    magnitude=int(magnitude)

    
    
    for x in range(0,magnitude):
        if direction=='L':
            snake[0][0]=snake[0][0]-1
        if direction=='R':
            snake[0][0]=snake[0][0]+1
        if direction=='U':
            snake[0][1]=snake[0][1]+1
        if direction=='D':
            snake[0][1]=snake[0][1]-1
        for x in range(0,9):
            head=snake[x]
            tail=snake[x+1]
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
            if horizontal_distance==2 and vertical_distance==-2:
                tail[0]=tail[0]+1
                tail[1]=tail[1]-1
            if horizontal_distance==2 and vertical_distance==2:
                tail[0]=tail[0]+1
                tail[1]=tail[1]+1

            if horizontal_distance==-2 and vertical_distance==0:
                tail[0]=tail[0]-1
            if horizontal_distance==-2 and vertical_distance==1:
                tail[0]=tail[0]-1
                tail[1]=tail[1]+1
            if horizontal_distance==-2 and vertical_distance==-1:
                tail[0]=tail[0]-1
                tail[1]=tail[1]-1            
            if horizontal_distance==-2 and vertical_distance==-2:
                tail[0]=tail[0]-1
                tail[1]=tail[1]-1 
            if horizontal_distance==-2 and vertical_distance==2:
                tail[0]=tail[0]-1
                tail[1]=tail[1]+1 
                
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
                
            
            #input()
            
            new_tail=tuple(snake[9])
            tail_locations.add(new_tail)   
        
print(len(tail_locations))
print(snake)

        