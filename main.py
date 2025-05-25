import turtle
from turtle import Turtle,Screen
tim=turtle.Turtle()
screen=turtle.Screen()

tim.speed(7)
def d():
    tim.right(10)
def w():
    tim.forward(10)
def s():
    tim.backward(10)
def a():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkeypress(a,"a")
screen.onkeypress(w,"w")
screen.onkeypress(s,"s")
screen.onkeypress(d,"d")
screen.onkey(key="c",fun=clear)

screen.exitonclick()