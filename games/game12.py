from turtle import *
from random import choice, randint

# -----------------------------
# Налаштування
# -----------------------------

colors = ["#c0392b", "#8e44ad", "#2471a3", "#138d75", "#f1c40f", "#e74c3c", "#5dade2"]

# координати квітки
x_start, y_start = 400, -150
x, y = x_start, y_start   # для сумісності з модульним кодом

# координати завдання
x_ask, y_ask = -170, 100

# координати неправильних літер
x_wrong, y_wrong = -170, 50

# радіус пелюстки
r = 95

# стартовий кут для обертання пелюсток
starting_angle = 360 / 7

# лічильники
count_right = 0
count_wrong = 0

speed(0)
hideturtle()


# -----------------------------
# ФУНКЦІЇ (з модулів + допоміжні)
# -----------------------------

def start(x, y):
    penup()
    goto(x, y)
    pendown()


# ---- Пелюстки ----
def draw_petal(col, radius):
    color(col)
    begin_fill()
    circle(radius, 60)
    left(120)
    circle(radius, 60)
    end_fill()


def draw_stem():
    start(x_start, y_start)
    setheading(90)
    color("green")
    width(20)
    forward(50)
    setheading(135)
    draw_petal("green", 100)
    setheading(25)
    draw_petal("green", 65)
    setheading(90)
    forward(150)


def draw_petals():
    width(20)
    k = starting_angle
    for i in range(7):
        start(x, y + 200)
        setheading(k)
        draw_petal(colors[i], r)
        k += starting_angle


def draw_flower():
    draw_stem()
    draw_petals()


def draw_down_petal(col):
    # перемалювати квітку
    draw_flower()

    # випадкове місце падіння пелюстки
    xd = randint(x - 50, x + 50)
    start(xd, y)
    h = randint(180, 360)
    setheading(h)
    width(20)
    draw_petal(col, r)


# ---- Написи ----

def write_ask(word):
    """Малює порожні лінії для слова."""
    start(x_ask, y_ask)
    setheading(0)
    width(4)
    color("black")
    penup()
    for w in word:
        pendown()
        forward(30)
        penup()
        forward(15)


def write_wrong(letter):
    """Малює неправильну літеру з хрестиком."""
    color("black")
    write(letter, font=("Arial", 28))

    # хрестик
    color("red")
    width(2)
    setheading(45)
    forward(30)
    setheading(180)
    penup()
    forward(20)
    setheading(315)
    pendown()
    forward(30)
    color("grey")


def write_right(letter):
    """Показує знайдену літеру на підкресленнях."""
    start(x_ask, y_ask + 5)
    penup()
    color("black")
    setheading(0)
    count = 0

    for w in word:
        if w == letter:
            pendown()
            write(letter, font=("Arial", 32))
            penup()
            count += 1
        forward(45)

    return count


def end_game(col, txt):
    start(-50, -50)
    color(col)
    write(txt, font=("Arial", 50, "bold"))


# -----------------------------
# Основна логіка гри
# -----------------------------

words = ["flower", "python", "cat", "apple", "sun", "world", "game"]
word = choice(words)

write_ask(word)     # підкреслення
draw_flower()       # квітка

current_wrong_x = x_wrong

while True:
    letter = input("Введіть літеру: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Введіть ОДНУ літеру!")
        continue

    # правильно
    if letter in word:
        c = write_right(letter)
        count_right += c

    # неправильно
    else:
        start(current_wrong_x, y_wrong)
        write_wrong(letter)
        current_wrong_x += 45

        count_wrong += 1

        col = colors[count_wrong - 1]
        colors[count_wrong - 1] = "white"

        draw_down_petal(col)

    # програш
    if count_wrong == 7:
        end_game("red", "Ти програв :(")
        break

    # виграш
    if count_right == len(word):
        end_game("blue", "Ти виграв!")
        break

done()
