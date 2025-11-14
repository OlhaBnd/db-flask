from flask import Flask, url_for, redirect
import sqlite3


def index():
    # Встановлюємо з'єднання з базою даних та надсилаємо запит
    conn = sqlite3.connect("Artistc.db")
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM artists WHERE "Birth Year" = (?)', [year])
    data = cursor.fetchall()


    # При обробці запиту розглянемо кілька варіантів:
    # Варіант 1 - у базі немає даних про художників, що народилися у зазначений рік
    if len(data) == 0:
        return 'У базі немає даних про художників, які народилися в ' + str(year) + 'році'
    
    # Варіант 2 – художник, який народився у зазначений рік, лише один
    elif len(data) == 1:
        return 'У ' + str(year) + 'році народився (народилася)' + data[0][0]
    
    # Варіант 3 - художників, які народилися в зазначений рік, декілька
    else:
        result = '<h3>Список художників, які народилися в ' + str(year) + ' році:</h3><ol>'
        for person in data:
            result += '<li>' + person[0] + '</li>'
        result += '</ol>'
    return result


# Запитуваний рік народження зберігатимемо у глобальній змінній
year = int(input('Введіть рік народження художника: '))        
app = Flask(__name__)
app.add_url_rule('/', 'index', index)   


if __name__ == "__main__":
    # Запускаємо веб-сервер:
    app.run()
