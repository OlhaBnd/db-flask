import sqlite3
conn = sqlite3.connect('Artistc.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM artists')
data = cursor.fetchall()
print("Кількість художників у базі: ", len(data))

cursor.execute('SELECT * FROM artists WHERE gender == "Female"')
data = cursor.fetchall()
print("Кількість жінок у базі: ", len(data))

cursor.execute('SELECT * FROM artists WHERE "Birth Year" < 1900')
data = cursor.fetchall()
print("Кількість художників  що народились до 1900року", len(data))