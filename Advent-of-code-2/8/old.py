# import random
#
# randoe = []
# for i in range(6):
#     randoe.append([])
#     for j in range(6):
#         randoe[i].append(random.randrange(1, 10))
# print(randoe)
#
#   412955
# # 513657
#    0ul0
# # 855472
#    uu0r
# # 656569
#    0udd
# # 648333
#    0ld0
# # 665142

# 6*2 + (6-1)*2
# 22 + 10 = 32
# problem is ...











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

File_object = open("6 by 6", "r")
file = File_object.readlines()
# print(str(file) + "\n")

file = remove_n_s(file)
# print(str(file) + "\n")

tallest_trees_from_above = []
bottom_trees = []
tallest_trees_from_left  = []
right_trees = []
for i in range(1, len(file[0]) - 1):
    tallest_trees_from_above.append(int(file[0][i]))
for i in range(1, len(file[-1]) - 1):
    bottom_trees.append(int(file[-1][i]))
for i in range(1, len(file) - 1):
    tallest_trees_from_left.append(int(file[i][0]))
for i in range(1, len(file) - 1):
    right_trees.append(int(file[i][-1]))
# print(tallest_trees_from_above)
# print(bottom_trees)
# print(tallest_trees_from_left )
# print(right_trees)


trees_known_to_be_visible = len(file) * 2 + len(file[0]) * 2 - 4
outer_trees = trees_known_to_be_visible

inner_trees = remove_outer_trees(file)
inner_trees = break_all_strs_into_lists(inner_trees)
print("\n" + str(inner_trees))

map_of_visibility = []

for i in range(len(inner_trees)):
    map_of_visibility.append([])
    for j in range(len(inner_trees[i])):
        # print(type(inner_trees[i][j]))
        # print(type(tallest_trees_from_above[j]))
        prev_val_of_trees_known_to_be_visible = trees_known_to_be_visible

        taller_than_above = inner_trees[i][j] > tallest_trees_from_above[j]
        if taller_than_above:
            tallest_trees_from_above[j] = inner_trees[i][j]
        taller_than_left = inner_trees[i][j] > tallest_trees_from_left[i]
        if taller_than_left:
            tallest_trees_from_left[i] = inner_trees[i][j]
        if taller_than_above or taller_than_left:
            trees_known_to_be_visible += 1
            pass
        elif inner_trees[i][j] <= right_trees[i] and inner_trees[i][j] <= bottom_trees[j]:
            pass
        else:
            this_one_s_visible_from_right = True
            this_one_s_visible_from_below = True
            # print("ranges: " + str(i) + " " + str(j) + "  " + str(range(j + 1, len(inner_trees) - 1)))
            for k in range(j + 1, len(inner_trees[i])):
                print(str(i) + " " + str(j) + " " + str(k))
                if inner_trees[i][k] >= inner_trees[i][j]:
                    this_one_s_visible_from_right = False
                    break
            for k in range(j + 1, len(inner_trees[i])):
                # print(str(i + k) + " " + str(j))
                print("down: " + str(i) + " " + str(j) + " " + str(inner_trees[k][j]) + " " + str(inner_trees[i][j]))
                if inner_trees[k][j] >= inner_trees[i][j]:
                    this_one_s_visible_from_below = False
                    break
            if this_one_s_visible_from_below or this_one_s_visible_from_right:
                trees_known_to_be_visible += 1
        if trees_known_to_be_visible == prev_val_of_trees_known_to_be_visible:
            map_of_visibility[-1].append([0])
        else:
            map_of_visibility[-1].append([1])



#og
        # 30373
        # 25512
        # 65332
        # 33549
        # 35390

        # 11111
        # 11101
        # 11011
        # 10101
        # 11111
    #21 but getting

#a little bigger
        # 30373
        # 25512
        # 65332
        # 33549
        # 35390
        # 22422

        # 11111
        # 11101
        # 11011
        # 10101
        # 11011
        # 11111
    #26 but getting

for i in map_of_visibility:
    print(i)

print("\n" + str(trees_known_to_be_visible))

# 1865 is too high















