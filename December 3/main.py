def count_trees(tree_map, x, y):
    column_index = 0
    line_index = 0
    counter = 0
    while line_index < len(tree_map):
        if tree_map[line_index][column_index] == '#':
            counter += 1
        line_index += y
        column_index = (column_index + x + len(tree_map[0])) % len(tree_map[0])
    
    return counter


def main(file_name):
    tree_map = []
    with open(file_name, 'r') as file:
        
        for line in file:
            line = line.strip()
            tree_map.append(line)
    
    print(count_trees(tree_map, 3, 1))
    print(count_trees(tree_map, 1, 1) * count_trees(tree_map, 3, 1) * count_trees(tree_map, 5, 1) * count_trees(tree_map, 7, 1) * count_trees(tree_map, 1, 2))

if __name__ == '__main__':
    main('train_dataset.txt')
    main('dataset.txt')
            

