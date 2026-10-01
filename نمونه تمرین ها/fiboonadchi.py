import turtle
import time

user_input = input("chand marpich rasm beshe? (pishnahad: 15-40) ")

if user_input.strip() == "":
    steps = 25
    steps = int(user_input)

print(f" Please wait for {user_input} to be drawn. ")
time.sleep(3)

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0) 

min_x, max_x = -400, 400
min_y, max_y = -300, 300
screen.setworldcoordinates(min_x, min_y, max_x, max_y)

t = turtle.Turtle()
t.speed(0) 
t.penup()
t.goto(0, 0)
t.pendown()

a, b = 1, 1
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

zoom_factor = 1.61 
margin = 0.85


    t.pencolor(colors[i % len(colors)])
    t.pensize(2)
    
    for _ in range(4):
        t.forward(a * 10)
        t.left(90)
    t.circle(a * 10, 90)
    
    if abs(t.xcor()) > (max_x - min_x) * margin / 2 or abs(t.ycor()) > (max_y - min_y) * margin / 2:
        min_x *= zoom_factor
        max_x *= zoom_factor
        min_y *= zoom_factor
        max_y *= zoom_factor
        screen.setworldcoordinates(min_x, min_y, max_x, max_y)

    a, b = b, a + b
    screen.update()
    time.sleep(0.50)

turtle.done()

for i in range(steps):  # 