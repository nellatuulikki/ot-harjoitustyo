class Game:

    def __init__(self, player_1, player_2, board_size):

        self.player_1 = player_1
        self.player_2 = player_2
        self.game_board_size = board_size
        self.winner = None
        self.player_1_turn = None
        self.game_board = None

    def initialize_game(self):
        self.create_game_board(3)
        self.winner = 'No winner yet'
        self.player_1_turn = True

    def create_game_board(self, height):

        board = []

        for _ in range(0, height):
            board.append(['']*height)

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
        self.change_turns()
        self.get_game_status()

    def player_2_makes_move(self, row, column):

        self.game_board[row][column] = 'O'
        self.player_1_turn = True
        self.get_game_status()

    def get_game_status(self):

        if (self.game_board[0][0] == self.game_board[0][1] == self.game_board[0][2] == "X"
                or self.game_board[1][0] == self.game_board[1][1] == self.game_board[1][2] == "X"
                or self.game_board[2][0] == self.game_board[2][1] == self.game_board[2][2] == "X"
                or self.game_board[0][0] == self.game_board[1][0] == self.game_board[2][0] == "X"
                or self.game_board[0][1] == self.game_board[1][1] == self.game_board[2][1] == "X"
                or self.game_board[0][2] == self.game_board[1][2] == self.game_board[2][2] == "X"
                or self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == "X"
                or self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == "X"):
            self.winner = self.player_1

        elif (self.game_board[0][0] == self.game_board[0][1] == self.game_board[0][2] == "O"
              or self.game_board[1][0] == self.game_board[1][1] == self.game_board[1][2] == "O"
              or self.game_board[2][0] == self.game_board[2][1] == self.game_board[2][2] == "O"
              or self.game_board[0][0] == self.game_board[1][0] == self.game_board[2][0] == "O"
              or self.game_board[0][1] == self.game_board[1][1] == self.game_board[2][1] == "O"
              or self.game_board[0][2] == self.game_board[1][2] == self.game_board[2][2] == "O"
              or self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] == "O"
              or self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] == "O"):
            self.winner = self.player_2

        elif any("" in row for row in self.game_board) is False:
            self.winner = 'No winner'

