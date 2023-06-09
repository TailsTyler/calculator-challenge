File_object = open("input", "r")
file = File_object.readlines() #['B Y\n', 'C Z\n', 'C Y\n',
print(file)
line = 0
index = 2
print(file[line][index])
score = 0


def find_score_from_your_move(file, line, index):
    if file[line][index] == 'X':
        return 1
    elif file[line][index] == 'Y':
        return 2
    elif file[line][index] == 'Z':
        return 3
    else:
        print('\nshit\n')
        return 0

def find_score_from_who_won_a_round(file, line, index):
    if file[line][index] == 'X':
        if file[line][index - 2] == 'A': #tie
            return 3
        elif file[line][index - 2] == 'B': #loss
            return 0
        elif file[line][index - 2] == 'C': #win
            return 6
    elif file[line][index] == 'Y':
        if file[line][index - 2] == 'A':  # win
            return 6
        elif file[line][index - 2] == 'B':  # tie
            return 3
        elif file[line][index - 2] == 'C':  # loss
            return 0
    elif file[line][index] == 'Z':
        if file[line][index - 2] == 'A':  # loss
            return 0
        elif file[line][index - 2] == 'B':  # win
            return 6
        elif file[line][index - 2] == 'C':  # tie
            return 3
    else:
        print('\nshit\n')
        return 0

while True:
    try:
        score += find_score_from_your_move(file, line, index) + find_score_from_who_won_a_round(file, line, index)
        line += 1
    except IndexError:
        break

print(score)

# 5100 is incorrect