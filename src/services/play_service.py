from entities.player import Player
from entities.game import Game

from repositories.game_repository import (
    game_repository as default_game_repository
)

from repositories.player_repository import (
    player_repository as default_player_repository
)


class PlayService:
    """Sovelluslogiikasta vastaava luokka"""

    def __init__(self, game_repository=default_game_repository, player_repository=default_player_repository):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun"""

        self.player_1 = None
        self.player_2 = None
        self.game = None
        self.board_height = None
        self.board_width = None
        self._game_repository = game_repository
        self._player_repository = player_repository

    def create_players(self, player_1, player_2, board_height, board_width):
        """Luo 2 Pelaaja-oliota ja Peli-olion.

        Args:
            player_1: Merkkijonoarvo, joka kuvaa Pelaajan 1 nimeä.
            player_2: Merkkojonoarvo, joka kuvaa Pelaajan 2 nimeä.
            board_height: Kokonaislukuarvo, joka kuvaa pelilaudan korkeutta
            board_width: Kokonaislukuarvo, joka kuvaa pelilaudan leveyttä
        """

        self.player_1 = self.initialize_player(player_1)
        self.player_2 = self.initialize_player(player_2)

        self.board_width, self.board_height = board_width, board_height

        self.game = Game(self.player_1, self.player_2, self.board_width, self.board_height)

    def start_new_game(self):
        """"Luo pelilaudan ja asettaa muuttujille pelivuoro ja voittaja arvot"""

        self.game.initialize_game()

    def initialize_player(self, name):
        player_data = self._player_repository.check_player(name)
        if player_data is None:
            self._player_repository.create_player(name)
            return Player(name, 0, 0)
        else:
            return player_data

    def get_height(self):
        """Palauttaa pelilaudan korkeuden

        Returns:
            Palauttaa pelilaudan korkeuden
        """

        return self.board_height

    def get_width(self):
        """Palauttaa pelilaudan leveyden

        Returns:
             Palauttaa pelilaudan leveyden
        """

        return self.board_width

    def get_player_1(self):
        """Palauttaa pelaajan 1 nimen

        Returns:
            Palauttaa Pelaaja-olion nimen merkkijonoarvoina
        """

        return self.player_1.get_name()

    def get_player_2(self):
        """Palauttaa pelaajan 1 nimen

        Returns:
               Palauttaa Pelaaja-olion nimen merkkijonoarvoina
        """

        return self.player_2.get_name()

    def get_winner(self):
        """Palauttaa pelin voittajan

        Returns:
               Palauttaa Peli-olion voittaja-attribuutin arvon
               Jos peli on kesken tai voittajaa ei ole palauttaa merkkijonoarvoina
               Jos jompikumpi pelaaja on voittanut, palauttaa Pelaaja-olion nimen
        """

        return self.game.get_winner()

    def player_1_turn(self):
        """Määrittelee kenen pelaajan vuoro pelata."""

        return self.game.player_1_turn

    def player_1_move(self, row, column):
        """Pelaaja 1 asettaa merkinsä pelilaudalle ja tarkistaa mikä pelin tilanne on.

        Args:
            row: Kokonaisluku, joka on pelilaudan x-koordinaatti
            column: Kokonaisluku, joka on pelilaudan y-koordinaatti
        """

        self.game.make_move(row, column, 'X')

        if self.game.get_winner() == self.get_player_1():
            self.initialize_outcome(self.player_1, self.player_2)

    def player_2_move(self, row, column):
        """Pelaaja 2 asettaa merkinsä pelilaudalle ja tarkistaa mikä pelin tilanne on.

        Args:
            row: Kokonaisluku, joka on pelilaudan x-koordinaatti

            column: Kokonaisluku, joka on pelilaudan y-koordinaatti
        """

        self.game.make_move(row, column, 'O')

        if self.game.get_winner() == self.get_player_2():
            self.initialize_outcome(self.player_2, self.player_1)

    def initialize_outcome(self, winner, loser):
        self.update_wins(winner)
        self.update_defeats(loser)

    def save_game(self):
        self._game_repository.create_game(self.game, self.player_1, self.player_2)

    def get_last_ten(self):
        return self._game_repository.get_last_ten()

    def update_wins(self, player):
        self._player_repository.update_wins(player)

    def update_defeats(self, player):
        self._player_repository.update_defeats(player)

    def get_top_players(self):
        return self._player_repository.get_top_ten()


play_service = PlayService()
# testi = play_service.initialize_player('testi5')
# play_service.update_wins(testi)
# play_service.update_defeats(testi)
