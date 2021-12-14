class Game:

    def __init__(self, player_1, player_2, board_length, board_height):

        self.player_1 = player_1
        self.player_2 = player_2
        self.board_length = board_length
        self.board_height = board_height
        self.winner = None
        self.player_1_turn = None
        self.game_board = None

    def initialize_game(self):
        self.create_game_board()
        self.winner = 'No winner yet'
        self.player_1_turn = True

    def create_game_board(self):

        board = []

        for _ in range(0, self.board_height):
            board.append(['']*self.board_length)

        self.game_board = board

    def add_winner(self, player):

        self.winner = player

        return player

    def get_winner(self):

        if self.winner == 'No winner yet' or self.winner == 'No winner':
            return self.winner
        else:
            return self.winner.get_name()

    def change_turns(self):

        if self.player_1_turn:
            self.player_1_turn = False
        else:
            self.player_1_turn = True

    def player_1_makes_move(self, row, column):

        self.game_board[row][column] = 'X'
        self.get_game_status(row, column)
        self.change_turns()

    def player_2_makes_move(self, row, column):

        self.game_board[row][column] = 'O'
        self.get_game_status(row, column)
        self.change_turns()


    def get_game_status(self, row, column):

        if self.player_1_turn:
            mark = "X"
        else:
            mark = "O"

        print(self.game_board)

        if self.check_horizontal(row, mark) == True or self.check_vertical(column, mark) == True or self.check_left_diagonal(row, column, mark) == True or self.check_right_diagonal(row, column, mark) == True:
            self.check_winner()
        elif any("" in row for row in self.game_board) is False:
            self.winner = 'No winner'

    def check_winner(self):

        if self.player_1_turn:
            print('toimii')
            self.winner = self.player_1
        else:
            print('toimii')
            self.winner = self.player_2

    def check_horizontal(self, row, mark):

        count = 0
        for i in range(0, self.board_length):
            if self.game_board[row][i] == mark:
                count += 1
            else:
                count = 0

            if count == 5:
                return True

        return False

    def check_vertical(self, column, mark):

        count = 0
        for i in range(0, self.board_height):
            if self.game_board[i][column] == mark:
                count += 1
            else:
                count = 0

            if count == 5:
                return True

        return False

    def check_left_diagonal(self, column, row, mark):

        while not column == 0 and not row == self.board_height - 1:
            #print(column, row)
            column -= 1
            row += 1

        start_row = row
        count = 0
        for col in range(start_row, self.board_length):
            if self.game_board[row][col] == mark:
                count += 1
            else:
                count = 0
            row -= 1

            if count == 5:
                return True
            elif row == self.board_height:
                return False

        return False

    def check_right_diagonal(self, column, row, mark):

        while not column == 0 and not row == 0:
            column -= 1
            row -= 1

        start_row = row
        count = 0
        for col in range(start_row, self.board_length):
            if self.game_board[row][col] == mark:
                count += 1
            else:
                count = 0
            row += 1

            if count == 5:
                return True
            elif row == self.board_height:
                return False

        return False

