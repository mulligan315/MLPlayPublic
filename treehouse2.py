
file='TreeGrid.txt'
trees=[]
max_scenic_score=0

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
        visible_count_up=0
        visible_count_down=0
        visible_count_right=0
        visible_count_left=0
        check_row_left=list(range(0,clm_idx))
        check_row_left.reverse()
        check_row_right=list(range(clm_idx+1,99))
        check_clm_up=list(range(0,row_idx))
        check_clm_up.reverse()
        check_clm_down=list(range(row_idx+1,99))
        for other in check_row_left:
            if trees[row_idx][other]>=tree:
                visible_count_left+=1
                break
            else:
                visible_count_left+=1
        
        for other in check_row_right:
            if trees[row_idx][other]>=tree:
                visible_count_right+=1
                break
            else:
                visible_count_right+=1
        
        for other in check_clm_up:
            if trees[other][clm_idx]>=tree:
                visible_count_up+=1
                break
            else:
                visible_count_up+=1
        
        for other in check_clm_down:
            if trees[other][clm_idx]>=tree:
                visible_count_down+=1
                break
            else:
                visible_count_down+=1
        
        scenic_score=visible_count_down*visible_count_left*visible_count_right*visible_count_up
        max_scenic_score=max(scenic_score,max_scenic_score)
        

print(max_scenic_score)