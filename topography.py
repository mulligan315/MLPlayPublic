class Node:
    all_Nodes=[]
    def __init__(self,altitude,row,column,isStart,isEnd) -> None:
        self.altitude=altitude
        self.row=row
        self.column=column
        self.steps=0
        self.isStart=isStart
        self.isEnd=isEnd
        Node.all_Nodes.append(self)

file='MapGrid.txt'
row=0
column=1
start=None
end=None
shortest_route=None

def convertToNodes(letter_string,row_num):
    global start
    global end
    node_list=[]
    column_num=0
    for letter in letter_string:
        isStart=False
        isEnd=False
        if letter=='S':
            isStart=True
            letter=='a'
        if letter=='E':
            isEnd=True
            letter='z'
        int_temp=ord(letter)-97
        node_temp=Node(int_temp,row_num,column_num,isStart,isEnd)
        node_list.append(node_temp)
        if isStart:
            start=node_temp
        if isEnd:
            end=node_temp
        
        column_num += 1
    return node_list


def search_for_route(source_direction,source_elevation,node_index,steps=0): #node index = (grid row, grid column)
    global grid
    global shortest_route
    current_node=grid[node_index[row]][node_index[column]]
    
    if current_node.altitude > source_elevation + 1:
        return
    if all([current_node.steps !=0,current_node.steps <= steps+1]):
        return
    steps += 1
    print(node_index,steps)
    current_node.steps=steps
    if current_node.isEnd==True:
        shortest_route=steps
        return
    
    directions=[]
    
    
    if all([node_index[row] !=0,source_direction !='up']):
        directions.append([(node_index[row]-1,node_index[column]),'down'])
    if all([node_index[column] !=171,source_direction !='right']):
        directions.append([(node_index[row],node_index[column]+1),'left'])
    if all([node_index[row] !=40,source_direction !='down']):
        directions.append([(node_index[row]+1,node_index[column]),'up'])
    if all([node_index[column] !=0,source_direction !='left']):
        directions.append([(node_index[row],node_index[column]-1),'right'])
    
    for way in directions:
        search_for_route(way[1],current_node.altitude,way[0],steps)
    
        
with open(file,'rt',encoding='utf-8-sig') as grid_data:
    grid_list=list(x.strip() for x in grid_data)
    
grid=[]
row_num=0
for line in grid_list:
    rowNodes=convertToNodes(line,row_num)
    grid.append(rowNodes)
    row_num += 1

search_for_route('left',0,(start.row,start.column),-1)

print(shortest_route)