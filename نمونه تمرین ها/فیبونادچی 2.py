import turtle
import time

while True:
    user_input = input(" Draw a few spirals (suggestion: 15-40) ")

    try:
        steps = int(user_input)
        if steps <= 0:
            print("You can only enter a positive number.")
            continue
        break
    except ValueError:
        print("This is not a number! Please enter a number. ")

if user_input.strip() == "":
    steps = 26
else:
    steps = int(user_input)

print(f" Please wait for {user_input} to be drawn. ")
time.sleep(1.4)

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0) 

min_x, max_x = -400, 400
min_y, max_y = -300, 300
screen.setworldcoordinates(min_x, min_y, max_x, max_y)

t = turtle.Turtle()
t.speed(2) 
t.penup()
t.goto(0, 0)
t.pendown()

a, b = 1, 1
colors = ["#250900", "#3A0000", "#580000", "#780000", "#8D0000", "#CC0000", "#DC143C", "#FF4747",
 "#FF5252", "#ff5a16", "#e34200", "#bb3600", "#892700"]

zoom_factor = 1.80

margin = 0.85


for i in range(steps):  
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
    time.sleep(0.32)

turtle.done()
