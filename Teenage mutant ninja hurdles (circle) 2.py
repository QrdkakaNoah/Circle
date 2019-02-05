import turtle

turtle = turtle.Turtle()
turtle.speed(0)
def square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
square()
def art():
    for i in range(90):
        turtle.left(1)
        square()
art()
def passpartout():
    for i in range(4):
        art()
passpartout()
input()
        

