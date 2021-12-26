import unittest
from entities.game import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player_1 = 'Nella'
        self.player_2 = 'Mikko'
        self.game = Game(self.player_1, self.player_2, 5, 5)
        self.game.initialize_game()

    def test_create_game_board_correct(self):
        self.assertEqual(self.game.game_board,
                         [['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', '']])

    def test_make_x_move_correct(self):
        self.game.make_move(0, 0, 'X')
        self.assertEqual(self.game.game_board,
                         [['X', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', '']])

    def test_make_o_move_correct(self):
        self.game.make_move(0, 0, 'O')
        self.assertEqual(self.game.game_board,
                         [['O', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', '']])

    def test_change_turns_correct(self):
        self.game.change_turns()
        self.assertEqual(self.game.player_1_turn, False)

    def test_game_status_winner_correct(self):
        self.game.game_board = [['', '', '', '', ''],
                                ['O', '', '', '', ''],
                                ['O', '', '', '', ''],
                                ['O', '', '', '', ''],
                                ['O', '', '', '', '']]
        self.game.make_move(0, 0, 'O')
        self.game.check_winner()
        self.assertEqual(self.game.winner, 'Mikko')

    def test_game_status_even_correct(self):
        self.game.game_board = [['O', 'O', 'X', 'O', 'O'],
                                ['X', 'X', 'O', 'O', 'X'],
                                ['O', 'O', 'X', 'X', 'X'],
                                ['X', 'X', 'O', 'O', 'O'],
                                ['O', 'O', 'X', 'X', '']]
        self.game.make_move(4, 4, 'X')
        self.assertEqual(self.game.winner, 'No winner')

    def test_horizontal(self):
        self.game.game_board = [['O', 'O', 'O', 'O', 'O'],
                                ['', '', '', '', ''],
                                ['', '', '', '', ''],
                                ['', '', '', '', ''],
                                ['', '', '', '', '']]

        win = self.game.check_horizontal(0, 'O')
        self.assertEqual(win, True)

        win = self.game.check_horizontal(1, 'O')
        self.assertEqual(win, False)

    def test_vertical(self):
        self.game.game_board = [['O', '', '', '', ''],
                                ['O', '', '', '', ''],
                                ['O', '', '', '', ''],
                                ['O', '', '', '', ''],
                                ['O', '', '', '', '']]

        win = self.game.check_vertical(0, 'O')
        self.assertEqual(win, True)

        win = self.game.check_vertical(1, 'O')
        self.assertEqual(win, False)

    def test_right_diagonal(self):
        self.game.game_board = [['O', '', '', '', ''],
                                ['', 'O', '', '', ''],
                                ['', '', 'O', '', ''],
                                ['', '', '', 'O', ''],
                                ['', '', '', '', 'O']]

        win = self.game.check_right_diagonal(0, 0, 'O')
        self.assertEqual(win, True)

        win = self.game.check_right_diagonal(0, 1, 'O')
        self.assertEqual(win, False)

    def test_left_diagonal(self):
        self.game.game_board = [['', '', '', '', 'O'],
                                ['', '', '', 'O', ''],
                                ['', '', 'O', '', ''],
                                ['', 'O', '', '', ''],
                                ['O', '', '', '', '']]

        win = self.game.check_left_diagonal(0, 4, 'O')
        self.assertEqual(win, True)

        win = self.game.check_left_diagonal(0, 3, 'O')
        self.assertEqual(win, False)


