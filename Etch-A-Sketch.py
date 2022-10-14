from turtle import Turtle, Screen

a = Turtle()
screen = Screen()


def forward():
    a.forward(10)


def backward():
    a.backward(10)


def turnLeft():
    a.left(10)


def turnRight():
    a.right(10)


def clear():
    a.clear()
    a.penup()
    a.home()
    a.pendown()



screen.listen()
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(turnLeft, "a")
screen.onkey(turnRight, "d")
screen.onkey(clear, "space")
screen.exitonclick()
