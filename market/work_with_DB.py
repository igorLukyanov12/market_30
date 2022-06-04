import sqlite3
try:
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    cursor.execute('SELECT name FROM main_category WHERE[name] = "Машина" ')
    print(cursor.fetchall())
    cursor.close()
    connect.commit()
except:
    print('Ошибка')
finally:
    print("Я выполняюсь всегда независимо от ошибки")
