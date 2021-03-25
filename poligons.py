import turtle
import math

a = turtle.Turtle()
a.shape('turtle')
a.speed(5)

base = 50
radius = base / (2 * math.sin(math.radians(360 / (6))))

for n in range(3, 21):
    i = n
    a.left(180 - (180 - (360 / n)) / 2)

    base = radius * (2 * math.sin(math.radians(360 / (n * 2))))

    while 0 < i <= n:
        a.forward(base)
        a.left(360 / n)
        i -= 1

    radius += 20

    a.setheading(0)
    a.penup()
    a.forward(20)
    a.pendown()

turtle.done()