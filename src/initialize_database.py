from database_connection import get_database_connection


def drop_games(connection):

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists games;
    """)

    connection.commit()


def drop_players(connection):

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists players;
    """)

    connection.commit()


def create_games(connection):

    cursor = connection.cursor()

    cursor.execute("""
        create table games(
            game_id text primary key,
            date text,
            player_1 varchar(10),
            player_2 varchar(10),
            winner varchar(10),
            duration int,
            moves int,
            board_size varchar(100)
        );
    """)

    connection.commit()


def create_players(connection):

    cursor = connection.cursor()

    cursor.execute("""
        create table players(
            name text primary key,
            wins int,
            defeats int
        );
    """)

    connection.commit()


def initialize_database():

    connection = get_database_connection()

    drop_players(connection)
    drop_games(connection)
    create_games(connection)
    create_players(connection)


if __name__ == '__main__':
    initialize_database()