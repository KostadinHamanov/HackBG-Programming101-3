import sqlite3
from settings import TABLES
from settings import MOVIES_PROJECTIONS_RESERVATIONS


class CinemaDatabase:

    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def establish_connection(self):
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.connection.close()

    def prepare(self):
        self.establish_connection()
        self.execute_file_to_database(TABLES)
        self.execute_file_to_database(MOVIES_PROJECTIONS_RESERVATIONS)

    def execute_file_to_database(self, filename):
        with open(filename, "r") as f:
            self.cursor.executescript(f.read())
            self.connection.commit()

    def add_movie(self, name, rating):
        add_movie_query = """
        INSERT INTO Movies(name, rating)
        VALUES (?, ?)
        """

        self.cursor.execute(add_movie_query, (name, rating))
        self.connection.commit()

    def add_projection(self, movie_id, type, date, time):
        add_projection_query = """
        INSERT INTO Projections(movie_id, type, date, time)
        VALUES(?, ?, ?, ?)
        """

        self.cursor.execute(add_projection_query, (movie_id, type, date, time))
        self.connection.commit()

    def add_reservation(self, username, projection_id, row, col):
        add_reservation_query = """
        INSERT INTO Reservations(username, projection_id, row, col)
        VALUES(?,?,?,?)
        """

        values = (username, projection_id, row, col)
        self.cursor.execute(add_reservation_query, values)
        self.connection.commit()

    def show_all_movies(self):
        show_movies_query = """
            SELECT Movies.id, Movies.name, Movies.rating
            FROM Movies
            ORDER BY Movies.rating DESC
            """

        self.cursor.execute(show_movies_query)
        all_movies = self.cursor.fetchall()

        return all_movies

    def get_movie_name(self, movie_id):
        get_movie_name_query = """
        SELECT Movies.name
        FROM Movies
        WHERE Movies.id = ?
        """

        self.cursor.execute(get_movie_name_query, (movie_id,))

        movie = self.cursor.fetchone()[0]

        return movie

    def count_non_available_seats(self, projection_id):
        count_busy_seats = """
        SELECT COUNT(*)
        FROM Reservations
        WHERE Reservations.projection_id = ?
        """

        self.cursor.execute(count_busy_seats, (projection_id,))

        seats = self.cursor.fetchone()[0]

        return seats

    def show_movie_projections(self, movie_id, date=None):
        if date is None:
            show_movie_projections_query = """
            SELECT Projections.id,Projections.type,
                   Projections.date, Projections.time
            FROM Projections
            WHERE Projections.movie_id = ?
            """

            self.cursor.execute(show_movie_projections_query, (movie_id,))

        if date is not None:
            show_movie_projections_query = """
            SELECT Projections.id, Projections.type,
                   Projections.date, Projections.time
            FROM Projections
            WHERE Projections.movie_id = ? AND Projections.date = ?
            ORDER BY Projections.date, Projections.time ASC
            """

            self.cursor.execute(show_movie_projections_query, (movie_id, date))

        all_projections = self.cursor.fetchall()

        return all_projections

    def delete_reservation(self, name):
        delete_reservation = """
        DELETE FROM Reservations
        WHERE Reservations.username = ?
        """

        self.cursor.execute(delete_reservation, (name, ))
        self.connection.commit()

    def show_projection(self, projection_id):
        show_projection_query = """
        SELECT Projections.date, Projections.time, Projections.type
        FROM Projections
        WHERE Projections.id = ?
        """

        self.cursor.execute(show_projection_query, (projection_id,))

        projection = self.cursor.fetchone()

        return projection

    def get_non_available_seats(self, projection_id):
        non_available_seats_query = """
        SELECT Reservations.row, Reservations.col
        FROM Reservations
        WHERE Reservations.projection_id IN (
            SELECT Projections.id
            FROM Projections
            WHERE Projections.id = ?)
        """

        self.cursor.execute(non_available_seats_query, (projection_id,))

        busy_seats = self.cursor.fetchall()

        return busy_seats
