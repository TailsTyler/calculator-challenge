def get_first_working_chars(file, length_where_no_chars_same):
    working_chars = []
    for i in range(length_where_no_chars_same):
        # print(file)
        # print(file[i])
        working_chars += file[0][i]
    return working_chars

def repeats_in(chars):
    return len(chars) != len(set(chars))

def cut_off_first_thing_in_list(list):
    return list[1::]

def scan_for_signal(file, length_where_no_chars_same):
    working_chars = get_first_working_chars(file, length_where_no_chars_same)
    test = range(len(file[0]) - length_where_no_chars_same)
    for i in range(len(file[0]) - length_where_no_chars_same):
        working_chars = cut_off_first_thing_in_list(working_chars)
        index_where_next_char_is = i + length_where_no_chars_same
        working_chars.append(file[0][index_where_next_char_is])
        if not repeats_in(working_chars):
            return index_where_next_char_is + 1
        else:
            i += 1
    return("No signal found")



File_object = open("test", "r")
file = File_object.readlines()
print(file)
# for i in range(len(file)):
#     print(i,': ',file[i])
length_where_no_chars_same = 4

working_chars = get_first_working_chars(file, length_where_no_chars_same)
print("working_chars: " + str(working_chars))
print("\nrepeats_in(working_chars): " + str(repeats_in(working_chars)))
print("\n" + str(scan_for_signal(file, length_where_no_chars_same)))










