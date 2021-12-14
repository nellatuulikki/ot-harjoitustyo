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

    def test_player_1_move_correct(self):
        self.game.player_1_makes_move(0, 0)
        self.assertEqual(self.game.game_board,
                         [['X', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', ''],
                          ['', '', '', '', '']])

    def test_player_2_move_correct(self):
        self.game.player_2_makes_move(0, 0)
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
        self.game.player_2_makes_move(0, 0)
        self.game.check_winner()
        self.assertEqual(self.game.winner, 'Mikko')

    def test_game_status_even_correct(self):
        self.game.game_board = [['O', 'O', 'X', 'O', 'O'],
                          ['X', 'X', 'O', 'O', 'X'],
                          ['O', 'O', 'X', 'X', 'X'],
                          ['X', 'X', 'O', 'O', 'O'],
                          ['O', 'O', 'X', 'X', '']]
        self.game.player_1_makes_move(4, 4)
        self.assertEqual(self.game.winner, 'No winner')
