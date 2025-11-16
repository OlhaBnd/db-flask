from turtle import*
from random import randint, choice

colors = ["#c0392b", "#8e44ad", "#2471a3", "#138d75", "#f1c40f", "#e74c3c", "#5dade2"]
x_start, y_start = 400, -150
x, y = x_start, y_start

x_ask, y_ask = -170, 100
x_wrong, y_wrong = -170, 50

r = 95
starting_angle = 360/7
count_right = 0
count_wrong = 0

speed(0)
hideturtle()

def start(x, y):
    penup()
    goto(x, y)
    pendown()

def draw_petal(col, radius):
    color(col)
    begin_fill()
    circle(radius, 60)
    left(120)
    circle(radius, 60)
    end_fill()
def draw_steam():
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
        start(x, y+200)
        setheading(k)
        draw_petal(colors[i], r)
        k+=starting_angle
def draw_flower():
    draw_steam()
    draw_petals()
def draw_down_petal(col):
    draw_flower()
    xd = randint(x-50, x+50)
    start(xd, y)
    h = randint(180, 360)
    setheading(h)
    width(20)
    draw_petal(col, r)
    