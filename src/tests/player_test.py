import unittest
from entities.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player('Mikko', 0, 0)

    def test_nimi_asetettu_oikein(self):
        self.assertEqual(self.player.get_name(), 'Mikko')

