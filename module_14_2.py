import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users(email)")

# Заполним ТАБЛИЦУ 10 записями:
for i in range(1, 11):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", f"{i*10}", "1000"))

# Обновим balance у каждой 2ой записи начиная с 1ой на 500:
for i in range(1, 11):
    if i % 2 != 0:
        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?",   ("500", f"{i}"))

# Удалим каждую 3ую запись в таблице начиная с 1ой:
for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE id = ?", (f"{i}",))

# Сделаем выборку всех записей при помощи fetchall():
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", ("60",))
users = cursor.fetchall()
# for user in users:
    # print(f"Имя: {user[0]}, Почта: {user[1]}, Возраст: {user[2]}, Баланс: {user[3]}")


# Удалим из базы данных not_telegram.db запись с id = 6:

cursor.execute("DELETE FROM Users WHERE id = ?", ("6", ))

# Подсчитаем общее количество записей:
cursor.execute("SELECT COUNT (*) FROM Users")
# total = cursor.fetchone()[0]
# print(total)

# Подсчитаем сумму всех балансов:
cursor.execute("SELECT SUM(balance)  FROM Users")
# total1 = cursor.fetchone()[0]
# print(total1)

# Выведем в консоль средний баланс всех пользователей:
cursor.execute("SELECT AVG(balance) FROM Users")
avg_age = cursor.fetchone()[0]
print(avg_age)


connection.commit()
connection.close()