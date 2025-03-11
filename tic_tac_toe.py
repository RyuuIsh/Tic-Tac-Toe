import random


class TicTacToe:
    _row = {'1': 0, '2': 1, '3': 2}

    _col = {'A': 0, 'B': 1, 'C': 2}

    def __init__(self, player_start=True, intelligent_play=False):

        self.intelligent_play = intelligent_play

        self.grid = []

        self.player_start = player_start

        self.player_1 = 'X'

        self.player_2 = 'O'  # Computer

        self.winner = None

        self.no_more_moves = False

        self.restart_game()  # start the first game

    def restart_game(self):

        self.grid = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]

        self.winner = None

        self.no_more_moves = False

        if not self.player_start:
            self._player_2_move()

    def game_play(self, position):

        position = position.upper()

        if not len(position) == 2:
            return

        row, col = position[0], position[1]

        if row in ['1', '2', '3'] and col in ['A', 'B', 'C']:

            if self.grid[TicTacToe._row[row]][TicTacToe._col[col]] == '.':

                self.grid[TicTacToe._row[row]][TicTacToe._col[col]] = self.player_1

                # Check for winner

                self._check_for_winner()

                self._check_no_more_moves()

                if self.winner is None and self.no_more_moves == False:
                    self._player_2_move()

                    self._check_for_winner()

                self._check_no_more_moves()

                return

    def _player_2_move(self):

        if not self.intelligent_play:

            while True:

                # Randomly choose empty position

                row = random.choice([0, 1, 2])

                col = random.choice([0, 1, 2])

                if self.grid[row][col] == '.':
                    self.grid[row][col] = self.player_2

                    break

        else:

            # Move intelligently

            if self._try_to_win_or_block(self.player_2):  # Try to win

                return

            if self._try_to_win_or_block(self.player_1):  # Try to block player

                return

            if self._take_center():  # Take center if available

                return

            if self._take_corner():  # Take a corner if available

                return

            self._take_random()  # Take any random empty spot as last resort

    def _try_to_win_or_block(self, player):

        for i in range(3):

            # Check rows and columns

            if self._check_two_in_line(self.grid[i][0], self.grid[i][1], self.grid[i][2], player, (i, 0), (i, 1),
                                       (i, 2)):
                return True

            if self._check_two_in_line(self.grid[0][i], self.grid[1][i], self.grid[2][i], player, (0, i), (1, i),
                                       (2, i)):
                return True

        # Check diagonals

        if self._check_two_in_line(self.grid[0][0], self.grid[1][1], self.grid[2][2], player, (0, 0), (1, 1), (2, 2)):
            return True

        if self._check_two_in_line(self.grid[0][2], self.grid[1][1], self.grid[2][0], player, (0, 2), (1, 1), (2, 0)):
            return True

        return False

    def _check_two_in_line(self, a, b, c, player, pos_a, pos_b, pos_c):

        if a == b == player and c == '.':
            self.grid[pos_c[0]][pos_c[1]] = self.player_2

            return True

        if a == c == player and b == '.':
            self.grid[pos_b[0]][pos_b[1]] = self.player_2

            return True

        if b == c == player and a == '.':
            self.grid[pos_a[0]][pos_a[1]] = self.player_2

            return True

        return False

    def _take_center(self):

        if self.grid[1][1] == '.':
            self.grid[1][1] = self.player_2

            return True

        return False

    def _take_corner(self):

        for (row, col) in [(0, 0), (0, 2), (2, 0), (2, 2)]:

            if self.grid[row][col] == '.':
                self.grid[row][col] = self.player_2

                return True

        return False

    def _take_random(self):

        while True:

            row = random.choice([0, 1, 2])

            col = random.choice([0, 1, 2])

            if self.grid[row][col] == '.':
                self.grid[row][col] = self.player_2

                break

    def _check_for_winner(self):

        if self.winner is None:

            # Check for winner in 3 rows

            for i in range(3):

                if self.grid[i][0] == self.player_1 and self.grid[i][1] == self.player_1 and self.grid[i][
                    2] == self.player_1:

                    self.winner = self.player_1

                    break

                elif self.grid[i][0] == self.player_2 and self.grid[i][1] == self.player_2 and self.grid[i][
                    2] == self.player_2:

                    self.winner = self.player_2

                    break

        if self.winner is None:

            # Check for winner in 3 columns

            for i in range(3):

                if self.grid[0][i] == self.player_1 and self.grid[1][i] == self.player_1 and self.grid[2][
                    i] == self.player_1:

                    self.winner = self.player_1

                    break

                elif self.grid[0][i] == self.player_2 and self.grid[1][i] == self.player_2 and self.grid[2][
                    i] == self.player_2:

                    self.winner = self.player_2

                    break

        if self.winner is None:

            # Check for winner in main diagonal

            if self.grid[0][0] == self.player_1 and self.grid[1][1] == self.player_1 and self.grid[2][
                2] == self.player_1:

                self.winner = self.player_1

            elif self.grid[0][0] == self.player_2 and self.grid[1][1] == self.player_2 and self.grid[2][
                2] == self.player_2:

                self.winner = self.player_2

        if self.winner is None:

            # Check for winner in anti-diagonal

            if self.grid[0][2] == self.player_1 and self.grid[1][1] == self.player_1 and self.grid[2][
                0] == self.player_1:

                self.winner = self.player_1

            elif self.grid[0][2] == self.player_2 and self.grid[1][1] == self.player_2 and self.grid[2][
                0] == self.player_2:

                self.winner = self.player_2

    def _check_no_more_moves(self):

        self.no_more_moves = all(cell != '.' for row in self.grid for cell in row)


def draw_grid(grid):
    print(' ', 'A', 'B', 'C')

    for i, row in enumerate(grid, start=1):
        print(i, row[0], row[1], row[2])


def print_instructions():
    print('Tic Tac Toe Game')

    print()

    print('You play against the computer. You can choose start first.')

    print('The position is entered as <row><col>. For example, the center is 2B and to the right of it is 2C.')

    print('The top right is 1C.  The bottom left is 1A.')

    print()


if __name__ == '__main__':

    print_instructions()

    start = input('Do you want to start? (Y for yes): ')

    intelligent = input('Play against intelligent computer? (Y for yes): ')

    player_start = False

    if start.upper() == 'Y':
        player_start = True

    intelligent_play = False

    if intelligent.upper() == 'Y':
        intelligent_play = True

    ttt = TicTacToe(player_start=player_start, intelligent_play=intelligent_play)

    while True:

        # ttt.draw_grid()

        draw_grid(ttt.grid)

        if ttt.winner is None:

            position = input('Enter position <row><col> :')

            ttt.game_play(position)



        else:

            print(f'----->> Winner is {ttt.winner}!!!!')

            ttt.restart_game()

        if ttt.no_more_moves:
            ttt.draw_grid()

            print(f'----->> It is a draw game.')

            ttt.restart_game()
