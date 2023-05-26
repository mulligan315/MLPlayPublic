file = 'SandScanData.txt'
stopped_stuff=[]
    


with open(file,'rt',encoding='utf-8-sig') as rock_data:
    rock_scans=list((line.strip() for line in rock_data))
    
for rocks in rock_scans:
    coord_array=rocks.split(' -> ')
    x=range(1,len(coord_array))
    for point in x:
        end=coord_array[point]
        start=coord_array[point-1]
        
        end=end.split(',')
        start=start.split(',')
        
        start_x=int(start[0])
        start_y=int(start[1])
        end_x=int(end[0])
        end_y=int(end[1])
        
        if point==1:
            stopped_stuff.append((start_x,start_y))
        
        
        change_x=end_x-start_x
        if change_x < 0:
            for delta in range(-1,change_x,-1):
                stopped_stuff.append((start_x + delta,start_y))
        elif change_x > 0:
            for delta in range(1,change_x,1):
                stopped_stuff.append((start_x + delta,start_y))
        
        change_y=end_y-start_y
        if change_y < 0:
            for delta in range(-1,change_y,-1):
                stopped_stuff.append((start_x,start_y + delta))
        elif change_y > 0:
            for delta in range(1,change_y,1):
                stopped_stuff.append((start_x,start_y+delta))
        stopped_stuff.append((end_x,end_y))
    


max_y = max(list(item[1] for item in stopped_stuff))


sand_still_stopping=True
sand_counter=0

while(sand_still_stopping):
    sand_falling=True
    sand=(500,0)
    while(sand_falling):
        spot_below=(sand[0],sand[1]+1)
        if spot_below in stopped_stuff:
            spot_below_left=(sand[0]-1,sand[1]+1)
            if spot_below_left in stopped_stuff:
                spot_below_right=(sand[0]+1,sand[1]+1)
                if spot_below_right in stopped_stuff:
                    stopped_stuff.append(sand)
                    sand_counter+=1
                    sand_falling=False
                else:
                    sand=spot_below_right
            else:
                sand=spot_below_left
        else:
            sand=spot_below
        if sand[1]>max_y:
            sand_falling=False
            sand_still_stopping=False

print(sand_counter)