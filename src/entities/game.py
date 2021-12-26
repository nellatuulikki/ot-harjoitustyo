import string
import random
import timeit

class Game:
    """Luokka, jonka avulla ylläpidetään peliä

    Attributes:
            player_1: Pelaaja-olio, joka pelaa risti-merkillä
            player_2: Pelaaja-olio, joka pelaa o-merkillä
            board_width: peli-laudan leveys
            board_height: peli-laudan korkeus

    """

    def __init__(self, player_1, player_2, board_width, board_height):
        """Luokan konstruktori, joka luo uuden pelin

        Args:
            player_1: Pelaaja-olio, joka pelaa risti-merkillä
            player_2: Pelaaja-olio, joka pelaa o-merkillä
            board_width: peli-laudan leveys
            board_height: peli-laudan korkeus
            winner:
        """

        self.player_1 = player_1
        self.player_2 = player_2
        self.board_width = board_width
        self.board_height = board_height
        self.winner = None
        self.player_1_turn = None
        self.game_board = None
        self.game_id = None
        self.duration = None
        self.moves = None

    def initialize_game(self):
        """"""

        self.create_game_board()
        self.winner = 'No winner yet'
        self.player_1_turn = True
        self.duration = timeit.default_timer()
        self.game_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.moves = 0

    def end_timing(self):
        self.duration = round(timeit.default_timer() - self.duration)

    def create_game_board(self):
        """Luo pelilauta"""

        board = []

        for _ in range(0, self.board_height):
            board.append(['']*self.board_width)

        self.game_board = board

    def get_winner(self):
        """Palauta voittaja

        Returns:
            Palauta voittanut Pelaaja-olio
        """
        if self.winner == 'No winner yet' or self.winner == 'No winner':
            return self.winner
        else:
            return self.winner.get_name()

    def change_turns(self):
        """Palauta voittaja

        Returns:
            Palauta voittanut Pelaaja-olio
        """
        if self.player_1_turn:
            self.player_1_turn = False
        else:
            self.player_1_turn = True

    def make_move(self, row, column, mark):
        """Suorittaa Pelaajan siirron, tarkistaa pelin tilanteen ja vaihtaa vuoroa

        Args:
            row: pelaajan siirron x-koordinaatti kokonaislukuna
            column: pelaajan siirron y-koordinaatti kokonaislukuna
        :return:
        """

        self.moves += 1
        self.game_board[row][column] = mark
        self.get_game_status(row, column, mark)
        self.change_turns()

    def get_game_status(self, row, column, mark):

        if self.check_horizontal(row, mark) is True \
                or self.check_vertical(column, mark) is True \
                or self.check_left_diagonal(row, column, mark) is True \
                or self.check_right_diagonal(row, column, mark) is True:
            self.check_winner()
        elif any("" in row for row in self.game_board) is False:
            self.winner = 'No winner'
            self.end_timing()

    def check_winner(self):

        if self.player_1_turn:
            self.winner = self.player_1
        else:
            self.winner = self.player_2
        self.end_timing()

    def check_horizontal(self, row, mark):

        count = 0
        for i in range(0, self.board_width):
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

    def check_left_diagonal(self, row, column, mark):
        while not column == 0 and not row == self.board_height - 1:
            column -= 1
            row += 1
        start_col = column
        count = 0
        for col in range(start_col, self.board_width):
            if self.game_board[row][col] == mark:
                count += 1
            else:
                count = 0
            row -= 1

            if count == 5:
                return True
            elif row == self.board_height or row < 0:
                return False

        return False

    def check_right_diagonal(self, row, column, mark):
        while not column == 0 and not row == 0:
            column -= 1
            row -= 1

        start_col = column
        count = 0
        for col in range(start_col, self.board_width):
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
