import unittest
from repositories.player_repository import player_repository
from entities.player import Player


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        player_repository.delete_all()
        self.player = Player('Tuulikki', 0, 0)

    def test_create_player(self):
        player_repository.create_player(self.player.name)
        player = player_repository.check_player(self.player.name)
        self.assertEqual(player.name, self.player.name)

    def test_update_defeats(self):
        player_repository.create_player(self.player.name)
        player_repository.update_defeats(self.player)
        player = player_repository.check_player(self.player.name)
        self.assertEqual(player.defeats, 1)

    def test_update_wins(self):
        player_repository.create_player(self.player.name)
        player_repository.update_wins(self.player)
        player = player_repository.check_player(self.player.name)
        self.assertEqual(player.wins, 1)