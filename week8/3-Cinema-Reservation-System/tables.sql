CREATE TABLE IF NOT EXISTS Movies(
    id INTEGER PRIMARY KEY,
    name TEXT,
    rating REAL,
    UNIQUE(name, rating)
);

CREATE TABLE IF NOT EXISTS Projections(
    id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    type TEXT,
    date TEXT,
    time TEXT,
    UNIQUE(movie_id, type, date, time)
    FOREIGN KEY (movie_id) REFERENCES Movies(id)
);

CREATE TABLE IF NOT EXISTS Reservations(
    id INTEGER PRIMARY KEY,
    username TEXT,
    projection_id INTEGER,
    row INTEGER,
    col INTEGER,
    UNIQUE(username, projection_id, row, col)
    FOREIGN KEY (projection_id) REFERENCES Projections(id)
);
