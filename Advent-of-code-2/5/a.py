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

def get_floor_line(file):
    for i in range(len(file)):
        try:
            int(file[i][1])
            return i - 1
        except:
            pass
    print("get floor failed")

def get_num_of_stacks(file, floor_line):
    return int(len(file[floor_line]) / 4)

def get_stacks(file, floor_line, num_of_stacks):
    i = floor_line
    stacks = []
    for i in range(num_of_stacks):
        stacks.append([])
    num_of_stacks_times_4 = num_of_stacks * 4
    while i >= 0:
        j = 1
        while j != num_of_stacks_times_4 + 1:
            try:
                if file[i][j] != ' ':
                    stacks[(j - 1) // 4].append(file[i][j])
            except:
                break
            j += 4
        i -= 1
    return stacks
def find_start_of_movement_instructions(file):
    for i in range(len(file)):
        if file[i][0] == 'm':
            return i
    print('find_start_of_movement_instructions failed')

def convert_string_to_an_array_if_the_nums_in_it(string, first_num_index):
    i = first_num_index
    array_of_nums_found = []
    j = 0
    k = 1
    while i < len(string):
        if string[i].isnumeric():
            collecting_chars_of_single_num = string[i]
            while True:
                if string[i + k].isnumeric():
                    collecting_chars_of_single_num += string[i + k]
                    k += 1
                else:
                    array_of_nums_found.append(int(collecting_chars_of_single_num))
                    i += k
                    k = 1
                    break
        else:
            i += 1
    return array_of_nums_found

def convert_movement_text_to_array_of_3_number_arrays(file, first_num_index):
    start_of_movement_instructions = find_start_of_movement_instructions(file)
    i = start_of_movement_instructions
    array_of_3_number_arrays = []
    while i < len(file):
        array_of_3_numbers = convert_string_to_an_array_if_the_nums_in_it(file[i], first_num_index)
        array_of_3_number_arrays.append(array_of_3_numbers)
        i += 1
    return array_of_3_number_arrays

def move_stacks(stacks, array_of_3_number_arrays): #move 3 from 1 to 2
    moved_stacks = stacks
    for command in array_of_3_number_arrays:
        for num_to_move in range(command[0]):
            moved_stacks[command[2] - 1].append(moved_stacks[command[1] - 1].pop())
    return moved_stacks

def get_top_boxes(stacks_after_movement):
    ans = []
    for i in stacks_after_movement:
        ans.append(i[-1])
    return ans

def list_to_string(list):
    string = ''
    for i in list:
        string += i
    return string


File_object = open("input", "r")
file = File_object.readlines()
print(file)
# for i in range(len(file)):
#     print(i,': ',file[i])

boxes_on_top_at_end = []
floor_line = get_floor_line(file)
print(floor_line)
num_of_stacks = get_num_of_stacks(file, floor_line)
print(num_of_stacks)
stacks = get_stacks(file, floor_line, num_of_stacks)
print(stacks)
array_of_3_number_arrays = convert_movement_text_to_array_of_3_number_arrays(file, 5)
print(array_of_3_number_arrays)
stacks_after_movement = move_stacks(stacks, array_of_3_number_arrays)
print(stacks_after_movement)
top_boxes = get_top_boxes(stacks_after_movement)
print(top_boxes)
string = list_to_string(top_boxes)
print(string)






