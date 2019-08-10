class Drawing:
    horizontal_line = '-' * 11
    CRED, CGREEN, CEND = '\033[91m', '\033[92m', '\033[0m'

    def vertical_line(self, line_number):
        return " {0} | {1} | {2} ".format(*Game.symb_list[line_number].values())

    def draw_fields(self, horizontal_line):
        self.line_number = 0  # string number in cycle
        print('Current game state:')
        for i in range(5):
            if i % 2 == 0:
                print(self.vertical_line(self.line_number))
                self.line_number += 1
            else:
                print(Drawing.horizontal_line)


class Game(Drawing):
    symb_list = [{0: ' ', 1: ' ', 2: ' '}, {3: ' ', 4: ' ', 5: ' '}, {6: ' ', 7: ' ', 8: ' '}]
    turn_number = 0

    def __init__(self):
        while True:
            '''
            here we print current state of game fields
            '''
            super().draw_fields(super().horizontal_line)

            '''
            here we perform the game
            '''
            if Game.turn_number % 2 == 0:
                Game.turn_number += 1
                self.symb = 'X'
                self.position = int(input(f'Enter position to fill {super().CGREEN + self.symb + super().CEND} in: '))
                self.game_init(self.position, self.symb)
                self.win = self.check_results(self.symb)
                if self.win:
                    super().draw_fields(super().horizontal_line)
                    print(super().CGREEN + 'X has won!' + super().CEND)
                    break

            else:
                Game.turn_number += 1
                self.symb = 'O'
                self.position = int(input(f'Enter position to fill {super().CGREEN + self.symb + super().CEND} in: '))
                self.game_init(self.position, self.symb)
                self.win = self.check_results(self.symb)
                if self.win:
                    super().draw_fields(super().horizontal_line)
                    print(super().CGREEN + 'O has won!' + super().CEND)
                    break

    def check_results(self, symb):
        """
            win combinations here: [0, 1, 2], [3, 4, 5], [6, 7, 8]
                                    [0,3,6], [1,4,7], [2,5,8]
                                    [0,4,8], [2,4,6]
            symb_list = [{0: ' ', 1: ' ', 2: ' '}, {3: ' ', 4: ' ', 5: ' '}, {6: ' ', 7: ' ', 8: ' '}]

            :param symb:
            :return:
            """
        if symb == 'X':
            self.win_combination = 'XXX'
        else:
            self.win_combination = 'OOO'

        for dic in Game.symb_list:
            if ''.join(list(dic.values())) == self.win_combination:
                return True
            elif Game.symb_list[0][0] + Game.symb_list[1][3] + Game.symb_list[2][6] == self.win_combination:
                return True
            elif Game.symb_list[0][1] + Game.symb_list[1][4] + Game.symb_list[2][7] == self.win_combination:
                return True
            elif Game.symb_list[0][2] + Game.symb_list[1][5] + Game.symb_list[2][8] == self.win_combination:
                return True
            elif Game.symb_list[0][0] + Game.symb_list[1][4] + Game.symb_list[2][8] == self.win_combination:
                return True
            elif Game.symb_list[0][2] + Game.symb_list[1][4] + Game.symb_list[2][6] == self.win_combination:
                return True
        return False

    def game_init(self, position, symb):
        for _ in Game.symb_list:
            if 2 >= position >= 0:
                if Game.symb_list[0][position] == ' ':
                    Game.symb_list[0][position] = symb
                    break
                else:
                    print(super().CRED + 'Error [Position is taken]. Try another one' + super().CEND)
                    break
            elif 5 >= position > 2:
                if Game.symb_list[1][position] == ' ':
                    Game.symb_list[1][position] = symb
                    break
                else:
                    print(super().CRED + 'Error [Position is taken]. Try another one' + super().CEND)
                    break
            elif 8 >= position > 5:
                if Game.symb_list[2][position] == ' ':
                    Game.symb_list[2][position] = symb
                    break
                else:
                    print(super().CRED + 'Error [Position is taken]. Try another one' + super().CEND)
                    break
            else:
                print(super().CRED + 'Error [Wrong position]. Try again' + super().CEND)
                break


class StartGame(Game):

    def __init__(self):
        print("Welcome to tic-tac-toe!")
        Game()


if __name__ == '__main__':
    StartGame()
