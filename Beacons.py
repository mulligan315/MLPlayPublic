class Beacon:
    all_beacons=[]
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
        Beacon.all_beacons.append(self)
        if y==magic_y:
            beacons_on_y.add((x,y))    


class Sensor:
    all_sensors=[]
    
    def __init__(self,x,y,beacon):
        self.x=x
        self.y=y
        
        self.closest_beacon=(beacon.x,beacon.y)
        self.reachable_distance = abs(x-beacon.x) + abs(y-beacon.y)
        Sensor.all_sensors.append(self)
        

file='BeaconData.txt'
beacon_list=[]
magic_y=1

beacons_on_y=set()
reachable_on_y=[]

with open(file,'rt',encoding='utf-8') as beacon_data:
    for item in beacon_data:
        new_string=item.strip()
        new_string=new_string.replace('Sensor at x=','')
        new_string=new_string.replace(' y=','')
        new_string=new_string.replace(': closest beacon is at x=',',')
        beacon_list.append(new_string)

for location in beacon_list:
    coords=location.split(',')
    beacon=Beacon(int(coords[2]),int(coords[3]))
    sensor=Sensor(int(coords[0]),int(coords[1]),beacon)


        
for sensor in Sensor.all_sensors:
    print('x =',sensor.x)
    print('y =',sensor.y)
    print('closest beacon =',sensor.closest_beacon)
    print('reachable distance =',sensor.reachable_distance)
    distance_to_magic_y=abs(sensor.y-magic_y)
    print('distance from magic y=',distance_to_magic_y)
    reachable = sensor.reachable_distance
    
    if distance_to_magic_y<=reachable:
        overlap=abs(reachable-distance_to_magic_y)
        print('overlap =',overlap)
        left_x_on_y=sensor.x-overlap
        right_x_on_y=sensor.x+overlap
        reachable_on_y.append((left_x_on_y,right_x_on_y))

reachable_on_y.sort()

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
        
print(reachable_collapsed)
reachable=0
for ranges in reachable_collapsed:
    reachable+=ranges[1]-ranges[0]+1
print(reachable)
reachable=reachable-len(beacons_on_y)
print(reachable)


    
