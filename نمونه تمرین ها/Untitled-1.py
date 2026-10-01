import turtle

t = turtle.Turtle()
t.speed(0.51)

a = 1
b = 1

for i in range(10):
    for _ in range(4):
        t.forward(a * 5)
        t.left(90)

    a, b = b, a+b


turtle.done()
