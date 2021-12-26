from database_connection import get_database_connection
import pandas as pd
from datetime import date


class GameRepository:

    def __init__(self, connection):

        self._connection = connection
        self.date = date.today().strftime("%d/%m/%Y")

    def create_game(self, game, player_1, player_2):

        cursor = self._connection.cursor()

        cursor.execute(
            'insert into games (game_id, date, player_1, player_2, winner, duration, moves, board_size) values (?,?,?,?,?,?,?,?)',
            (game.game_id,
             self.date,
             player_1.name,
             player_2.name,
             game.get_winner(),
             game.duration,
             game.moves,
             f"{game.board_height}x{game.board_width}")
        )

        self._connection.commit()

    def get_last_ten(self):

        query = 'select * from games limit 5'
        df = pd.read_sql(query, self._connection)
        df.reset_index(drop=True, inplace=True)

        return df

    def delete_all(self):
        """Poistaa kaikki käyttäjät.
        """

        cursor = self._connection.cursor()

        cursor.execute('delete from games')

        self._connection.commit()

    def check_game(self, game):
        cursor = self._connection.cursor()

        cursor.execute(
            'select * from games where game_id = ?', (game.game_id,)
        )

        row = cursor.fetchone()
        return row


game_repository = GameRepository(get_database_connection())

