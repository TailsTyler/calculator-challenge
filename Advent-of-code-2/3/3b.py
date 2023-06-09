def get_unique_items_in_a_bag(bag):
    #print(bag[0:-1]) #remove '\n'
    return set(bag[0:-1])

def get_unique_items_in_second_compartment(bag):
    items_in_second_compartment = []
    l = int(len(bag) / 2)
    while l < len(bag) - 1 :
        items_in_second_compartment += bag[l]
        l += 1
    #sample_set = set(sample_list)
    unique_items_in_second_compartment = set(items_in_second_compartment)
    return unique_items_in_second_compartment

def to_priorities(set_):
    answer = []
    for l in set_:
        #print('to_p\n' + str(ord(l)))
        l_asci = ord(l)
        if l_asci < 91: #Upper case. A is 65 and should be 27.
            l_asci -= (65-27)
        else: #lower case. a is 97 and should be 1
            l_asci -= (97-1)
        answer.append(l_asci)
    return answer

File_object = open("input", "r")
file = File_object.readlines() #['GwrhJPDJCZFRcwfZWV\n', 'LjnQlqNpjjmpmQlLlqNfZRvQcTWcTSTTZcSQcZ\n',
print(file)

list_of_items_in_trio = [] #always only one
i = 0
while i < len(file) - 2: #aJrwpWtwJgWrhcsFMMfFFhFp
    unique_items_in_bag_1 = get_unique_items_in_a_bag(file[i + 0])
    unique_items_in_bag_2 = get_unique_items_in_a_bag(file[i + 1])
    unique_items_in_bag_3 = get_unique_items_in_a_bag(file[i + 2])
    found = False
    for j in unique_items_in_bag_1:
        for k in unique_items_in_bag_2:
            if j == k:
                item_in_bag_1_and_2 = k
                for l in unique_items_in_bag_3:
                    if item_in_bag_1_and_2 == l:
                        list_of_items_in_trio.append(l)
                        found = True
                        break
        if found:
            break
    i += 3
list_of_items_in_trio_s_priorities = to_priorities(list_of_items_in_trio)
print("here:")
print(list_of_items_in_trio)
print(list_of_items_in_trio_s_priorities)
print(sum(list_of_items_in_trio_s_priorities))
#2686 is too low


