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
                Game.perform_game(self.symb)
                if self.win:
                    break

            else:
                Game.turn_number += 1
                self.symb = 'O'
                Game.perform_game(self.symb)
                if self.win:
                    break

    def perform_game(self, symb):
        self.position = int(input(f'Enter position to fill {super().CGREEN + symb + super().CEND} in: '))
        self.game_init(self.position, symb)
        self.win = self.check_results(symb)
        if self.win:
            super().draw_fields(super().horizontal_line)
            msg = f'{symb} has won'
            print(super().CGREEN + msg + super().CEND)
