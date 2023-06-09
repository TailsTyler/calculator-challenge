import os

def remove_n_s(file):
    for i in range(len(file) - 1):
        file[i] = file[i][0:-1]
    return file
def remove_outer_trees(file):
    file = file[1:-1]
    for i in range(len(file)):
        file[i] = file[i][1:-1]
    return file

def break_all_strs_into_lists (list_of_strings):
    new_list = []
    for i in range(len(list_of_strings)):
        new_list.append([])
        for j in range(len(list_of_strings[i])):
            j = new_list[i].append(int(list_of_strings[i][j]))
    return new_list


# /home/ty/vscode/advent of code/Advent-of-code-2/8/
print(os.getcwd())
File_object = open("8/input", "r")
file = File_object.readlines()
# print(str(file) + "\n")

file = remove_n_s(file)
# print(str(file) + "\n")


trees = break_all_strs_into_lists(file)

# print(trees)

class Tree:
    def __init__(self, height):
        self.height = height
        self.visible_trees_above_count = 0
        self.visible_trees_below_count = 0
        self.visible_trees_to_left_count = 0
        self.visible_trees_to_right_count = 0 
    def get_scenic_score(self):
        return self.visible_trees_above_count * self.visible_trees_below_count * self.visible_trees_to_left_count * self.visible_trees_to_right_count
    def __repr__(self):
        return str(self.height) + "|" + str(self.visible_trees_above_count) + "|" + str(self.visible_trees_below_count) + "|" + str(self.visible_trees_to_left_count) + "|" + str(self.visible_trees_to_right_count) + "|" + str(self.get_scenic_score())

# for i in range(len(trees)):
#     for j in range(len(trees[i])):
#         trees[i][j] = Tree(trees[i][j], False)
trees = [[Tree(trees[i][j]) for j in range(len(trees[i]))] for i in range(len(trees))]

# for i in trees:
#     print(str(i))

# for distence_from in reversed(range(5, 0)):
#     print(distence_from)

for row in range(1, len(trees) - 1):
    for col in range(1, len(trees[0]) - 1):
        #above
        tallest_so_far = -1
        for distence_from in reversed(range(0, row)):
            trees[row][col].visible_trees_above_count += 1
            if trees[distence_from][col].height >= trees[row][col].height:
                break
        #below
        tallest_so_far = -1
        for distence_from in (range(row + 1, len(trees))):
            trees[row][col].visible_trees_below_count += 1
            if trees[distence_from][col].height >= trees[row][col].height:
                break
        #left
        tallest_so_far = -1
        for distence_from in reversed(range(0, col)):
            trees[row][col].visible_trees_to_left_count += 1
            if trees[row][distence_from].height >= trees[row][col].height:
                break
        #right
        tallest_so_far = -1
        for distence_from in range(col + 1, len(trees[0])):
            trees[row][col].visible_trees_to_right_count += 1
            if trees[row][distence_from].height >= trees[row][col].height:
                break

for i in trees:
    print(str(i))

biggest_scenic_score = 0
for i in trees:
    for j in i:
        if j.get_scenic_score() > biggest_scenic_score:
            biggest_scenic_score = j.get_scenic_score()

print(biggest_scenic_score)

#9072 too low
#you only see the first tree taller than you
  

     

