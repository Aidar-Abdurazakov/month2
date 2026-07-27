import sqlite3

db = sqlite3.connect("store.db")
cursor = db.cursor()

# Создание таблицы
cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    quantity INTEGER
)
""")

db.commit()


def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products(name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    db.commit()
    print("Товар успешно добавлен!")


def read_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    if not products:
        print("Таблица пустая.")
    else:
        for product in products:
            print(product)


def update_product(id, price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (price, id)
    )
    db.commit()
    print("Цена товара обновлена!")


def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (id,)
    )
    db.commit()
    print("Товар удален!")



create_product("Ноутбук", 55000, 3)
create_product("Мышка", 1200, 15)
create_product("Клавиатура", 2500, 7)

print("\nВсе товары:")
read_products()

update_product(2, 1500)

print("\nПосле обновления:")
read_products()

delete_product(3)

print("\nПосле удаления:")
read_products()


db.close()