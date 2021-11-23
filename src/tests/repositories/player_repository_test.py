import unittest
from src.repositories.player_repository import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player('Mikko')

    def test_nimi_asetettu_oikein(self):
        self.assertEqual(print(self.player.get_name()), "Mikko")