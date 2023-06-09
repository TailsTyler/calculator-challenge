import os

# import random
#
# randoe = []
# for i in range(6):
#     randoe.append([])
#     for j in range(6):
#         randoe[i].append(random.randrange(1, 10))


class Tree:
    def __init__(self, height, known_visible):
        self.height = height
        self.known_visible = known_visible
    def __repr__(self):
        letter = ''
        if self.known_visible:
            letter = 'T'
        else:
            letter = 'F'
        return str(self.height) + str(letter)




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

yes_no_s = [[1,1,0],[1,0,1],[0,1,0]]

# /home/ty/vscode/advent of code/Advent-of-code-2/8/
print(os.getcwd())
File_object = open("8/input", "r")
file = File_object.readlines()
# print(str(file) + "\n")

file = remove_n_s(file)
# print(str(file) + "\n")


trees = break_all_strs_into_lists(file)

print(trees)

# for i in range(len(trees)):
#     for j in range(len(trees[i])):
#         trees[i][j] = Tree(trees[i][j], False)
trees = [[Tree(trees[i][j], False) for j in range(len(trees[i]))] for i in range(len(trees))]

def look_from_above(trees):
    for col in range(len(trees[0])):
        trees[0][col].known_visible = True #bc edge
        tallest_so_far = trees[0][col].height
        for row in range(1, len(trees)):
            if trees[row][col].height > tallest_so_far:
                tallest_so_far = trees[row][col].height
                trees[row][col].known_visible = True
            if tallest_so_far == 9:
                break
    return trees
def look_from_below(trees):
    for col in range(len(trees[-1])):
        trees[-1][col].known_visible = True #bc edge
        tallest_so_far = trees[-1][col].height
        for row in reversed(range(1, len(trees))):
            if trees[row][col].height > tallest_so_far:
                tallest_so_far = trees[row][col].height
                trees[row][col].known_visible = True
            if tallest_so_far == 9:
                break
    return trees
def look_from_left(trees):
    for row in range(len(trees)):
        trees[row][0].known_visible = True #bc edge
        tallest_so_far = trees[row][0].height
        for col in (range(1, len(trees[0]))):
            if trees[row][col].height > tallest_so_far:
                tallest_so_far = trees[row][col].height
                trees[row][col].known_visible = True
            if tallest_so_far == 9:
                break
    return trees
def look_from_right(trees):
    for row in range(len(trees)):
        trees[row][-1].known_visible = True #bc edge
        tallest_so_far = trees[row][-1].height
        for col in reversed(range(1, len(trees))):
            if trees[row][col].height > tallest_so_far:
                tallest_so_far = trees[row][col].height
                trees[row][col].known_visible = True
            if tallest_so_far == 9:
                break
    return trees

look_from_above(trees)
look_from_below(trees)
look_from_left(trees)
look_from_right(trees)

for i in trees:
    print(str(i))

visible = 0
for i in trees:
    for j in i:
        if j.known_visible:
            visible += 1
print(visible)

  

     
