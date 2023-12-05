def solution_one(input):
    visible_trees = 0
    num_edge_trees = (2*len(input)) + (2*len(input[0])) - 4
    visible_inside_trees = 0

    for row in range(1, len(input)-1):
        for col in range(1, len(input[0])-1):
            is_visible = get_visibility(row, col, input)
            if is_visible:
                visible_inside_trees += 1

    visible_trees = num_edge_trees + visible_inside_trees
    return visible_trees

def solution_two(input):
    highest_scenic_score = 0
    for row in range(0, len(input)-1):
        for col in range(0, len(input[0])-1):
            current_scenic_score = get_scenic_score(row, col, input)
            if current_scenic_score > highest_scenic_score:
                highest_scenic_score = current_scenic_score

    return highest_scenic_score

def get_visibility(row, col, trees):
    sides_visible_from = 4
    tree = trees[row][col]
    # search up
    row_itr = row - 1
    while row_itr >= 0:
        current_tree = trees[row_itr][col]
        if current_tree >= tree:
            sides_visible_from -= 1
            break
        row_itr -= 1
    # search down
    row_itr = row + 1
    while row_itr < len(trees):
        current_tree = trees[row_itr][col]
        if current_tree >= tree:
            sides_visible_from -= 1
            break
        row_itr += 1
    # search left
    col_itr = col - 1
    while col_itr >= 0:
        current_tree = trees[row][col_itr]
        if current_tree >= tree:
            sides_visible_from -= 1
            break
        col_itr -= 1
    # search right
    col_itr = col + 1
    while col_itr < len(trees[0]):
        current_tree = trees[row][col_itr]
        if current_tree >= tree:
            sides_visible_from -= 1
            break
        col_itr += 1
    
    if sides_visible_from > 0:
        return True
    else:
        return False

def get_scenic_score(row, col, trees):
    scenic_score = 0
    up_viewing_distance = 0
    down_viewing_distance = 0
    left_viewing_distance = 0
    right_viewing_distance = 0
    tree = trees[row][col]
    # search up
    row_itr = row - 1
    while row_itr >= 0:
        current_tree = trees[row_itr][col]
        if current_tree < tree:
            up_viewing_distance += 1
        else: 
            # count the blocking tree as a tree able to be seen
            up_viewing_distance += 1
            break
        row_itr -= 1
    # search down
    row_itr = row + 1
    while row_itr < len(trees):
        current_tree = trees[row_itr][col]
        if current_tree < tree:
            down_viewing_distance += 1
        else: 
            down_viewing_distance += 1
            break
        row_itr += 1
    # search left
    col_itr = col - 1
    while col_itr >= 0:
        current_tree = trees[row][col_itr]
        if current_tree < tree:
            left_viewing_distance += 1
        else: 
            left_viewing_distance += 1
            break
        col_itr -= 1
    # search right
    col_itr = col + 1
    while col_itr < len(trees[0]):
        current_tree = trees[row][col_itr]
        if current_tree < tree:
            right_viewing_distance += 1
        else: 
            right_viewing_distance += 1
            break
        col_itr += 1
    
    scenic_score = (up_viewing_distance * down_viewing_distance * 
                    left_viewing_distance * right_viewing_distance)
    return scenic_score

if __name__ == "__main__":
    main()