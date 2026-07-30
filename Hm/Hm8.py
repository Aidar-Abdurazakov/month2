import sqlite3

connect = sqlite3.connect("grades.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS movies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    genre TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS reviews(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    movie_id INTEGER,
    rating INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(movie_id) REFERENCES movies(id)
)
""")

users = [
    ("Aidar",),
    ("Adilet",),
    ("Ardager",),
    ("Azamat",),
    ("Nurbek",)
]
cursor.executemany(
    "INSERT INTO users(name) VALUES(?)",
    users
)

movies = [
    ("Мстители", "Фантастика"),
    ("Нелегал", "Боевик"),
    ("Джокер", "Драма"),
    ("Бейиш", "Драма"),
    ("Курош", "Боевик")
]
cursor.executemany(
    "INSERT INTO movies(title, genre) VALUES(?, ?)",
    movies
)

reviews = [
    (1, 1, 10),
    (1, 2, 9),
    (2, 3, 8),
    (2, 1, 10),
    (3, 5, 9),
    (3, 4, 7),
    (4, 2, 8),
    (4, 3, 9),
    (5, 5, 10),
    (5, 1, 8)
]

cursor.executemany(
    "INSERT INTO reviews(user_id, movie_id, rating) VALUES(?, ?, ?)",
    reviews
)

connect.commit()

print("Имя пользователя | Фильм | Оценка")
print("-" * 40)

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")

for row in cursor.fetchall():
    print(row)

print("\nВсе фильмы:")

cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews
ON movies.id = reviews.movie_id
""")

for row in cursor.fetchall():
    print(row)

    cursor.execute("SELECT AVG(rating) FROM reviews")
print("\nСредняя оценка:", round(cursor.fetchone()[0], 2))

cursor.execute("SELECT MAX(rating) FROM reviews")
print("Максимальная оценка:", cursor.fetchone()[0])

cursor.execute("SELECT MIN(rating) FROM reviews")
print("Минимальная оценка:", cursor.fetchone()[0])
connect.close()