
all_beacons=set()
all_sensors=[]

file='BeaconData.txt'

MaxY=4_000_000
beacon_list=[]

with open(file,'rt',encoding='utf-8') as beacon_data:
    for item in beacon_data:
        new_string=item.strip()
        new_string=new_string.replace('Sensor at x=','')
        new_string=new_string.replace(' y=','')
        new_string=new_string.replace(': closest beacon is at x=',',')
        beacon_list.append(new_string)

for location in beacon_list:
    coords=location.split(',')
    reachable_distance = abs(int(coords[0])-int(coords[2])) + abs(int(coords[1])-int(coords[3]))
    all_beacons.add((int(coords[2]),int(coords[3])))
    all_sensors.append((int(coords[0]),int(coords[1]),reachable_distance))


for magic_y in range(MaxY+1):
    reachable_on_y=[]        
    for sensor in all_sensors:
        distance_to_magic_y=abs(sensor[1]-magic_y)
        
        if distance_to_magic_y<=sensor[2]:
            overlap=abs(sensor[2]-distance_to_magic_y)
            left_x_on_y=sensor[0]-overlap
            right_x_on_y=sensor[0]+overlap
            reachable_on_y.append((left_x_on_y,right_x_on_y))
    #print(reachable_on_y)
    reachable_on_y.sort()
    #print(reachable_on_y)
    reachable_collapsed=[]        
    for index in range(1,len(reachable_on_y)):
        if index==1:
            left=reachable_on_y[index-1]
        right=reachable_on_y[index]
        if left[1]>=right[0]:
            new_start=left[0]
            new_end=max(left[1],right[1])
            left=(new_start,new_end)
        else:
            reachable_collapsed.append(left)
            left=right
        if index==len(reachable_on_y)-1:
            reachable_collapsed.append(left)
    if len(reachable_collapsed)>1:
        break
    
print(reachable_collapsed,magic_y)

answer=(reachable_collapsed[0][1]+1)*4_000_000+magic_y
print(answer)


    
