from database_connection import get_database_connection
import pandas as pd
from entities.player import Player


def get_player(row):
    return Player(row['name'], row['wins'], row['defeats']) if row else None


class PlayerRepository:

    def __init__(self, connection):

        self._connection = connection

    def create_player(self, name):

        cursor = self._connection.cursor()

        cursor.execute(
            'insert into players (name, wins, defeats) values (?,?,?)',
            (name, 0, 0)
        )

        self._connection.commit()

    def find_all(self):

        query = 'select * from players'
        all_df = pd.read_sql(query, self._connection)

        return all_df

    def get_top_ten(self):

        query = 'select name, wins, defeats from players order by wins desc limit 5'
        top_ten_df = pd.read_sql(query, self._connection)

        return top_ten_df

    def check_player(self, name):
        cursor = self._connection.cursor()

        cursor.execute(
            'select * from players where name = ?', (name,)
        )

        row = cursor.fetchone()
        return get_player(row)

    def update_wins(self, player):
        wins = player.get_wins() + 1

        cursor = self._connection.cursor()

        cursor.execute(
            'update players set wins = ? where name = ?',
            (wins, player.get_name())
        )

        self._connection.commit()

    def update_defeats(self, player):
        defeats = player.get_defeats() + 1

        cursor = self._connection.cursor()

        cursor.execute(
            'update players set defeats = ? where name = ?',
            (defeats, player.get_name())
        )

        self._connection.commit()

    def delete_all(self):
        """Poistaa kaikki pelaajat."""

        cursor = self._connection.cursor()

        cursor.execute('delete from players')

        self._connection.commit()


player_repository = PlayerRepository(get_database_connection())
