
class Player:
    """Luokka, joka kuvaa pelaajaa."""

    def __init__(self, name, wins, defeats):
        """Luokan konstruktori, joka luo uuden pelaajan.

        Args:
            name: Merkkijonoarvo, joka kuvaa uuden pelaajan nimeä.
        """

        self.name = name
        self.wins = wins
        self.defeats = defeats

    def get_name(self):
        """Palauttaa pelaajan nimen.

        Returns:
            Merkkijooarvo, joka kuvaa pelaajan nimeä.
        """
        return self.name

    def get_wins(self):
        """Palauttaa pelaajan voittojen lukumäärän.

        Return:
            Palauttaa pelaajan voittojen lukumäärän kokonaislukuna.
        """
        return self.wins

    def get_defeats(self):
        """Palauttaa pelaajan voittojen lukumäärän.

        Return:
            Palauttaa pelaajan voittojen lukumäärän kokonaislukuna.
        """
        return self.defeats
