def get_number_substring_from_beginning_of_a_string(string):
    number_s_substring = ''
    for i in string:
        if is_a_digit(i):
            number_s_substring += i
        else:
            break
    return number_s_substring
def remove_x_num_of_chars_from_beginning_of_string(string, x):
    return string[x::]
def remove_first_char_in_string(string):
    return string[1::]
def is_a_digit(x):
    try:
        int(x)
        return True
    except:
        return False
def get_ranges(line_from_input):
    range_1 = []
    range_1.append(int(get_number_substring_from_beginning_of_a_string(line_from_input)))
    modified_line_from_input = remove_x_num_of_chars_from_beginning_of_string(line_from_input, len(str(range_1[0])))
    modified_line_from_input = remove_first_char_in_string(modified_line_from_input)
    range_1.append(int(get_number_substring_from_beginning_of_a_string(modified_line_from_input)))
    modified_line_from_input = remove_x_num_of_chars_from_beginning_of_string(modified_line_from_input, len(str(range_1[1])))
    modified_line_from_input = remove_first_char_in_string(modified_line_from_input)
    range_2 = []
    range_2.append(int(get_number_substring_from_beginning_of_a_string(modified_line_from_input)))
    modified_line_from_input = remove_x_num_of_chars_from_beginning_of_string(modified_line_from_input, len(str(range_2[0])))
    modified_line_from_input = remove_first_char_in_string(modified_line_from_input)
    range_2.append(int(get_number_substring_from_beginning_of_a_string(modified_line_from_input)))
    modified_line_from_input = remove_x_num_of_chars_from_beginning_of_string(modified_line_from_input, len(str(range_2[1])))
    ranges = [range_1, range_2]
    return ranges

def has_overlap(ranges):
    range_0_is_smaller = ranges[0][1] < ranges[1][0]
    if range_0_is_smaller:
        return False
    range_1_is_smaller = ranges[1][1] < ranges[0][0]
    if range_1_is_smaller:
        return False
    return True

File_object = open("input", "r")
file = File_object.readlines() #['71-71,42-72\n', '27-28,27-99\n',
# print(file)
# for i in range(len(file)):
#     print(i,': ',file[i])

assignment_pairs_where_one_range_fully_contains_the_other = 0
z = 1
for i in file:

    ranges = get_ranges(i)
    is_a_subset = False
    if has_overlap(ranges):
        assignment_pairs_where_one_range_fully_contains_the_other += 1
        is_a_subset = True
    print(z, ': ', i,": ", is_a_subset)
    z += 1
print(assignment_pairs_where_one_range_fully_contains_the_other)






