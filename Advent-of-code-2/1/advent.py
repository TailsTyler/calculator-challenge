
def advent_():
    File_object = open("cals.txt", "r")
    file = File_object.readlines()
    #print(file) #['6471\n', '1935\n', '1793\n', '3843\n', '6059\n', '6736\n', '6101\n', '3133\n', '6861\n', '1330\n', '1962\n', '5538\n', '6760\n', '\n', '5212\n',
    sums = []
    elf_count = 0
    sum_index = 0
    current_sum = 0
    file_index = 0
    while True:
        x = elf_loop(sums, file, current_sum, sum_index, file_index)
        print(sum_index)
        sums = x[0]
        sum_index = x[1]
        file_index = x[2]
        stop = x[3]
        if stop:
            break
    print(sums)
    print(greatest(sums))
    print(sum_3_greatest(sums))

def elf_loop(sums, file, current_sum, sum_index, file_index):
    #you_should_sum = False
    sums.append(0)
    stop = False
    if file[file_index] == '\n' and file[file_index + 1] == '\n':# end of file?
        stop = True
    while True: #loop thru each food item and elf seperator once
        try:
            print(file[file_index])
        except IndexError:
            print("\ndarn. index: " + str(file_index) + "\n")
            stop = True
            break
        if file[file_index] == '\n': #end of elf
            file_index += 1
            break
        current_sum += int(file[file_index])
        file_index += 1
    sums[sum_index] = current_sum
    sum_index += 1
    return [sums, sum_index, file_index, stop]

def greatest(listy):
    greatest = listy[0]
    for i in listy:
        if i > greatest:
            greatest = i
    return greatest

def sum_3_greatest(listy):
    greatest_1 = greatest(listy)
    modified_listy = listy
    modified_listy.remove(greatest_1)
    greatest_2 = greatest(modified_listy)
    modified_listy.remove(greatest_2)
    greatest_3 = greatest(modified_listy)
    return greatest_1 + greatest_2 + greatest_3

advent_()



