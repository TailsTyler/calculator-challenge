def get_unique_items_in_first_compartment(bag):
    items_in_first_compartment = []
    print(bag)
    print(len(bag))
    print(range(int(len(bag) / 2)))
    for l in range(int(len(bag) / 2)):
        items_in_first_compartment += bag[l]
    #sample_set = set(sample_list)
    unique_items_in_first_compartment = set(items_in_first_compartment)
    return unique_items_in_first_compartment

def get_unique_items_in_second_compartment(bag):
    items_in_second_compartment = []
    l = int(len(bag) / 2)
    while l < len(bag) - 1:
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

list_of_items_in_both_compartments_in_a_bag = [] #always only one
for i in file: #aJrwpWtwJgWrhcsFMMfFFhFp
    found = False
    unique_items_in_first_compartment = get_unique_items_in_first_compartment(i)
    unique_items_in_second_compartment = get_unique_items_in_second_compartment(i)
    for j in unique_items_in_first_compartment:
        for k in unique_items_in_second_compartment:
            if j == k:
                list_of_items_in_both_compartments_in_a_bag.append(j)
                found = True
                break
        if found:
            break
list_of_items_in_both_compartments_in_a_bag_s_priorities = to_priorities(list_of_items_in_both_compartments_in_a_bag)
print("here:")
print(list_of_items_in_both_compartments_in_a_bag)
print(list_of_items_in_both_compartments_in_a_bag_s_priorities)
test_list = [2, 4]
print(sum(list_of_items_in_both_compartments_in_a_bag_s_priorities))
# 157 too low



