File_object = open("input", "r")
file = File_object.readlines()  # ['B Y\n', 'C Z\n', 'C Y\n',
print(file)
line = 0
index = 2
print(file[line][index])
score = 0


def find_needed_move_from_needed_outcome(file, line, index):
    if file[line][index] == 'X':  # lose
        if file[line][index - 2] == 'A':
            return 'Z'
        elif file[line][index - 2] == 'B':
            return 'X'
        elif file[line][index - 2] == 'C':
            return 'Y'
    elif file[line][index] == 'Y':  # tie
        if file[line][index - 2] == 'A':
            return 'X'
        elif file[line][index - 2] == 'B':
            return 'Y'
        elif file[line][index - 2] == 'C':
            return 'Z'
    elif file[line][index] == 'Z':  # win
        if file[line][index - 2] == 'A':
            return 'Y'
        elif file[line][index - 2] == 'B':
            return 'Z'
        elif file[line][index - 2] == 'C':
            return 'X'
    else:
        print('\nshit\n')
        return 0


def find_score_from_who_won_a_round(file, line, index):
    if file[line][index] == 'X':  # lose
        return 0
    elif file[line][index] == 'Y':  # tie
        return 3
    elif file[line][index] == 'Z':  # win
        return 6
    else:
        print('\nshit\n')
        return 0


def find_score_from_your_move(move):
    if move == 'X':
        return 1
    elif move == 'Y':
        return 2
    elif move == 'Z':
        return 3
    else:
        print('\nshit\n')
        return 0


while True:
    try:
        score += find_score_from_your_move(
            find_needed_move_from_needed_outcome(file, line, index)) + find_score_from_who_won_a_round(file, line,
                                                                                                       index)
        line += 1
    except IndexError:
        break

print(score)

# 5100 is incorrect
