
file='TreeGrid.txt'
trees=[]
visible_count=0

with open(file, encoding='utf-8-sig') as tree_data:
    for tree_line in tree_data:
        tree_row=list(tree_line.removesuffix('\n'))
        for index, tree in enumerate(tree_row):
            tree_row[index]=int(tree)
        trees.append(tree_row)
row_count=len(trees)
clm_count=len(trees[0])

print(row_count,clm_count)

for row_idx, tree_row in enumerate(trees):
    for clm_idx, tree in enumerate(tree_row):
        visible=False
        if clm_idx==0 or row_idx==0 or clm_idx==99 or row_idx==99:
            visible_count+=1
        else:
            check_row_left=list(range(0,clm_idx))
            check_row_right=list(range(clm_idx+1,99))
            check_clm_up=list(range(0,row_idx))
            check_clm_down=list(range(row_idx+1,99))
            if visible==False:
                visible_left=True
                for other in check_row_left:
                    if trees[row_idx][other]>=tree:
                        visible_left=False
                        break
                if visible_left==True:
                    visible=True
            if visible==False:
                visible_right=True
                for other in check_row_right:
                    if trees[row_idx][other]>=tree:
                        visible_right=False
                        break
                if visible_right==True:
                    visible=True
            if visible==False:
                visible_up=True
                for other in check_clm_up:
                    if trees[other][clm_idx]>=tree:
                        visible_up=False
                        break
                if visible_up==True:
                    visible=True
            if visible==False:
                visible_down=True
                for other in check_clm_down:
                    if trees[other][clm_idx]>=tree:
                        visible_down=False
                        break
                if visible_down==True:
                    visible=True
            if visible==True:
                visible_count+=1

print(visible_count)