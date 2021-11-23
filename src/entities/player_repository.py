

class Player:

    def __init__(self, name):
        """"Luokka jossa säilytetään tietoja pelaajista"""

        self.name = name
        self.wins = 0

    def get_name(self):
        return self.name

    def player_wins(self):
        self.wins += 1

    def get_wins(self):
        return self.wins
