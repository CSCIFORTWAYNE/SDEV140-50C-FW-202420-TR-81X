"""
# Card drawing is based on the Deck of Cards Simulator by @TokyoEdtech
# https://github.com/wynand1004/Projects/blob/master/Cards/deck_of_cards.py
# Combo of Turtle and tkinter based on code from
# https://compucademy.net/python-turtle-graphics-and-tkinter-gui-programming/
"""

import random
import turtle
def hexagon(t, length):
    for count in range(6):
        t.forward(length)
        t.left(60)

def radialHexagons(t,n,length):
    for count in range(n):
        hexagon(t,length)
        t.left(360/n)

x = random.randint(0,10)
y = random.randint(0,10)

wn = turtle.Screen()
pen = turtle.Turtle()
pen.speed(1)
pen.penup()
pen.hideturtle()
pen.goto(x,y)
pen.goto(x-50, y+75)
pen.begin_fill()
pen.pendown()
pen.goto(x+50, y+75)
pen.goto(x+50,y-75)
pen.goto(x-50,y-75)
pen.goto(x-50,y+75)
pen.end_fill()
pen.penup()
pen.showturtle()

pen.goto(random.randint(100, 200), random.randint(0,10))
pen.pendown()
pen.width(2)
pen.left(45)
pen.forward(30)
pen.left(45)
pen.up()
pen.forward(10)
pen.setheading(0)
pen.pencolor("red")
pen.down()
pen.forward(20)

pen.up()
pen.goto(random.randint(100,200),random.randint(50, 100))
pen.pencolor("navy")
pen.down()
radialHexagons(pen,10,100)
wn.mainloop()

