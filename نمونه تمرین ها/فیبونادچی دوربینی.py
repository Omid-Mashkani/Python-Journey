tekrar = int(input("vared kon"))


import turtle
import time

# تنظیمات صفحه
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0) 

# مختصات اولیه دنیا
min_x, max_x = -400, 400
min_y, max_y = -300, 300
screen.setworldcoordinates(min_x, min_y, max_x, max_y)

t = turtle.Turtle()
t.speed(1) 
t.penup()
t.goto(0, 0)
t.pendown()

a, b = 1, 1
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# ضریب زوم: هرچی این عدد به 1 نزدیک‌تر باشه، دوربین "زوم‌تر" می‌مونه!
# 1.25 یعنی 25 درصد بزرگ‌نمایی در هر مرحله (خیلی دقیق‌تر از 1.5)
zoom_factor = 1.61

for i in range(tekrar): # تعداد تکرار بیشتر برای دیدن رشد مارپیچ
    t.pencolor(colors[i % len(colors)])
    t.pensize(2)
    
    # رسم مربع و قوس
    for _ in range(4):
        t.forward(a * 10)
        t.left(90)
    t.circle(a * 10, 90)
    
    # منطق هوشمند دوربین
    # اگر لاک‌پشت به 85% لبه‌های صفحه رسید (یکم سخت‌گیرتر کردیم)
    margin = 0.85 
    
    if abs(t.xcor()) > (max_x - min_x) * margin / 2 or abs(t.ycor()) > (max_y - min_y) * margin / 2:
        # بزرگ‌نمایی دنیا با ضریب جدید و دقیق‌تر
        min_x *= zoom_factor
        max_x *= zoom_factor
        min_y *= zoom_factor
        max_y *= zoom_factor
        screen.setworldcoordinates(min_x, min_y, max_x, max_y)

    a, b = b, a + b
    screen.update()
    time.sleep(0.5) # سرعت انیمیشن رو هم یکم بیشتر کردم

turtle.done()
