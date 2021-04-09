import turtle
import math

turtle.showturtle()
turtle.pensize(3)
turtle.speed(0)
turtle.shape("turtle")
turtle.color("pink")

def draw_parabola():
    turtle.penup()
    turtle.goto(-1000, 0)
    turtle.pendown()
    turtle.goto(1000, 0)
    turtle.penup()
    turtle.goto(0, -1000)
    turtle.pendown()
    turtle.goto(0, 1000)

    turtle.penup()
    turtle.goto(-40, 1600)
    turtle.pendown()
    for x in range(-40, 40):
        turtle.goto(x, x ** 2)

def draw_menu(anchor):
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.circle(100)
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()
    turtle.goto(50, 50)
    turtle.penup()
    turtle.goto(-80, 60)
    turtle.pendown()
    turtle.circle(5)
    turtle.penup()
    turtle.goto(80, 60)
    turtle.pendown()
    turtle.circle(7)
    input("")

def draw_arc(radius, anchor, scale_factor, arc_portion, start_angle):
    rad_start_angle = start_angle * (math.pi / 180)
    arc = (2 * math.pi * radius) / arc_portion
    step = arc / scale_factor
    turtle.penup()
    turtle.goto(anchor[0] + (radius * math.cos(rad_start_angle)), anchor[1] + (radius * math.sin(rad_start_angle)))
    turtle.pendown()
    turtle.seth(start_angle + 90)
    for i in range(0, scale_factor):
        turtle.fd(step)
        turtle.lt((360 / arc_portion) / scale_factor)
    turtle.fd(step)
    input("")

draw_menu((100, 100))
draw_arc(200, (0, 0), 100, 4, 45)