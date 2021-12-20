from src.database_connection import get_database_connection

class GameRepository:

    def __init__(self, connection):

        self._connection = connection

    def create_game(self, game_id, date, player_1, player_2, winner, duration, moves, board_size):

        cursor = self._connection.cursor()

        cursor.execute(
            'insert into games (game_id, date, player_1, player_2, winner, duration, moves, board_size) values (?,?,?,?,?,?,?,?)',
            (game_id, date, player_1, player_2, winner, duration, moves, board_size)
        )

        self._connection.commit()

    def find_all(self):

        cursor = self._connection.cursor()

        cursor.execute(
            'select * from games'
        )

        row = cursor.fetchone()

        return row

con = GameRepository(get_database_connection())
con.create_game('test1', 'test', 'test', 'test', 'test', 2, 3, 'test')
output = con.find_all()
print(output)