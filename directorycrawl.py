file='FileDir.txt'
dir_stream=[]
all_dirs=[]
home_dir=['/',[],[],[],0]
current_dir=home_dir
bigDirs=[]



name=0
subs=1
files=2
parent=3
size=4

    
    
with open(file, encoding='utf-8-sig') as dir_data:
    for line in dir_data:
        dir_stream.append(line.removesuffix('\n'))

for line in dir_stream:
    if line[0:3]=='dir':
        dir_name=line[4:]
        new_dir=[dir_name,[],[],current_dir,0]
        current_dir[subs].append(new_dir)
        continue
    elif line[0].isnumeric():
        fileinfo=line.split(' ')
        current_dir[files].append(int(fileinfo[0]))
        continue
    elif line[0:7]=='$ cd ..':
        print(f'{current_dir[name]} before ..')
        if current_dir[name]=='/':
            print(f'Already in home directory!!!!!!!!!!!!!!!!!!!!!!!!!!')
            continue
        if current_dir[parent]==[]:
            print((f'{current_dir} does not have a parent!!!!!!!!!!!!!!!!!!'))
        current_dir=current_dir[parent]
        print(f'{current_dir[name]} after ..')
        continue
    elif line[0:4]=='$ cd':
        print(f'{current_dir[name]} before cd')
        found=False
        dirinfo=line.split(' ')
        #if dirinfo[2]==current_dir[name]:
        #    print(f'Already in dir {dirinfo[2]}!')
        #    continue
        for dir in current_dir[subs]:
            if dir[name]==dirinfo[2]:
                current_dir=dir
                print(f'{current_dir[name]} after cd')
                found=True
                break
        if found==False:
            print(f"dir {dirinfo[2]} not found!!!!!!!!!!!!!!!!!!!!!")
        continue
    elif line[0:4]=='$ ls':
        continue
    print("exception")
    break
        

def crawl_for_size(dir):
    total=0
    for sub in dir[subs]:
        total+=crawl_for_size(sub)
    for file in dir[files]:
        total+=file
    dir[size]=total
    all_dirs.append(total)
    if total<=100000:
        bigDirs.append(total)
    return total

mega_total=crawl_for_size(home_dir)
    

total_of_biggies=0
for biggie in bigDirs:
    total_of_biggies+=biggie
print(total_of_biggies)

all_dirs.sort()
space_needed=30000000-70000000+mega_total


for dir in all_dirs:
    if dir>space_needed:
        print(dir)
        break