# symb_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
# symb_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
symb_list = [{0: ' ', 1: ' ', 2: ' '}, {3: ' ', 4: ' ', 5: ' '}, {6: ' ', 7: ' ', 8: ' '}]
hor_line = '-' * 11
turn_number = 0
CRED, CGREEN, CEND = '\033[91m', '\033[92m', '\033[0m'


def vert_line(line_number):
    return " {0} | {1} | {2} ".format(*symb_list[line_number].values())


def game(position, symb):
    for idx, lst in enumerate(symb_list):
        if 2 >= position >= 0:
            if symb_list[0][position] == ' ':
                symb_list[0][position] = symb
                break
            else:
                print(CRED + 'Error [Position is taken]. Try another one' + CEND)
                break
        elif 5 >= position > 2:
            if symb_list[1][position] == ' ':
                symb_list[1][position] = symb
                break
            else:
                print(CRED + 'Error [Position is taken]. Try another one' + CEND)
                break
        elif 8 >= position > 5:
            if symb_list[2][position] == ' ':
                symb_list[2][position] = symb
                break
            else:
                print(CRED + 'Error [Position is taken]. Try another one' + CEND)
                break
        else:
            print(CRED + 'Error [Wrong position]. Try again' + CEND)
            break


def draw_fields(hor_line):
    n = 0  # string number in cycle
    print('Current game state:')
    for i in range(5):
        if i % 2 == 0:
            print(vert_line(n))
            n += 1
        else:
            print(hor_line)


def check_results(symb):
    """
    win combinations here: [0, 1, 2], [3, 4, 5], [6, 7, 8]
                            [0,3,6], [1,4,7], [2,5,8]
                            [0,4,8], [2,4,6]
    symb_list = [{0: ' ', 1: ' ', 2: ' '}, {3: ' ', 4: ' ', 5: ' '}, {6: ' ', 7: ' ', 8: ' '}]

    :param symb:
    :return:
    """
    if symb == 'X':
        win_combination = 'XXX'
    else:
        win_combination = 'OOO'

    for dic in symb_list:
        if ''.join(list(dic.values())) == win_combination:
            return True
        elif symb_list[0][0] + symb_list[1][3] + symb_list[2][6] == win_combination:
            return True
        elif symb_list[0][1] + symb_list[1][4] + symb_list[2][7] == win_combination:
            return True
        elif symb_list[0][2] + symb_list[1][5] + symb_list[2][8] == win_combination:
            return True
        elif symb_list[0][0] + symb_list[1][4] + symb_list[2][8] == win_combination:
            return True
        elif symb_list[0][2] + symb_list[1][4] + symb_list[2][6] == win_combination:
            return True
    return False


if __name__ == '__main__':

    while True:
        '''
        here we print current state of game fields
        '''
        draw_fields(hor_line)

        '''
        here we perform the game
        '''
        if turn_number % 2 == 0:
            turn_number += 1
            symb = 'X'
            position = int(input(f'Enter position to fill {CGREEN + symb + CEND} in: '))
            game(position, symb)
            win = check_results(symb)
            if win:
                draw_fields(hor_line)
                print(CGREEN + 'X has won!' + CEND)
                break

        else:
            turn_number += 1
            symb = 'O'
            position = int(input(f'Enter position to fill {CGREEN + symb + CEND} in: '))
            game(position, symb)
            win = check_results(symb)
            if win:
                draw_fields(hor_line)
                print(CGREEN + 'O has won!' + CEND)
                break
