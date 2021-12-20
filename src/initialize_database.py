from database_connection import get_database_connection


def drop_tables(connection):

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists games;
    """)

    connection.commit()


def create_tables(connection):

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


def initialize_database():

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == '__main__':
    initialize_database()