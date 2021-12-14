class Player:
    """Luokka, joka kuvaa pelaajaa."""

    def __init__(self, name):
        """Luokan konstruktori, joka luo uuden pelaajan.

        Args:
            name: Merkkijooarvo, joka kuvaa uuden pelaajan nimeä.
        """

        self.name = name
        self.wins = 0

    def get_name(self):
        """Palauttaa pelaajan nimen.

        Returns:
            Merkkijooarvo, joka kuvaa pelaajan nimeä.
        """
        return self.name

    def add_win(self):
        """Lisää pelaajalle voiton."""
        self.wins += 1

    def get_wins(self):
        """Palauttaa pelaajan voittojen lukumäärän.

        Return:
            Palauttaa pelaajan voittojen lukumäärän kokonaislukuna.
        """
        return self.wins
