import sqlite3

db = sqlite3.connect('itproger.db')
c = db.cursor()

# c.execute("""CREATE TABLE IF NOT EXISTS articles(
#     title TEXT,
#     full_text TEXT,
#     view INTEGER,
#     avtor TEXT                  
# )""")

c.execute(
    "INSERT INTO articles VALUES (?, ?, ?, ?)",
    ('FACEBOOK is cool', 'FACEBOOK is realy cool', 500, 'AIDAR')
)

c.execute("SELECT rowid, * FROM articles")

# print(c.fetchall())       Показывает весь список
# print(c.fetchmany(1))     Показывает какой список показать
# print(c.fetchone()[1])    Можно выбрать какой именно текст вывести

print(c.fetchall())
for el in items:
    print(el[1] + "/n" + el[4])
db.commit()
db.close()