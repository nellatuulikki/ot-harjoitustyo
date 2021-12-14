from entities.player import Player
from entities.game import Game


class PlayService:
    """Sovelluslogiikasta vastaava luokka"""
    def __init__(self):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun"""

        self.player_1 = None
        self.player_2 = None
        self.game = None
        self.board_height = None
        self.board_width = None

    def create_players(self, player_1, player_2, board_height, board_width):
        """Luo 2 Pelaaja-oliota ja Peli-olion.

        Args:
            player_1: Merkkijonoarvo, joka kuvaa Pelaajan 1 nimeä.
            player_2: Merkkojonoarvo, joka kuvaa Pelaajan 2 nimeä.
            board_height: Kokonaislukuarvo, joka kuvaa pelilaudan korkeutta
            board_width: Kokonaislukuarvo, joka kuvaa pelilaudan leveyttä
        """

        self.player_1, self.player_2 = Player(player_1), Player(player_2)

        self.board_width, self.board_height = board_width, board_height

        self.game = Game(self.player_1, self.player_2, self.board_width, self.board_height)

    def start_new_game(self):
        """"Luo pelilaudan ja asettaa muuttujille pelivuoro ja voittaja arvot"""

        self.game.initialize_game()

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

        self.game.player_1_makes_move(row, column)

        if self.game.get_winner() == self.get_player_2():
            self.player_1.add_win()

    def player_2_move(self, row, column):
        """Pelaaja 2 asettaa merkinsä pelilaudalle ja tarkistaa mikä pelin tilanne on.

        Args:
            row: Kokonaisluku, joka on pelilaudan x-koordinaatti

            column: Kokonaisluku, joka on pelilaudan y-koordinaatti
        """

        self.game.player_2_makes_move(row, column)

        if self.game.get_winner() == self.get_player_1():
            self.player_2.add_win()


play_service = PlayService()
