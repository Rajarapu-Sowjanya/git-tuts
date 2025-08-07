import turtle
import time
import math
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Analog Clock")
screen.setup(width=600, height=600)
screen.tracer(0)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")

def draw_clock_face():
    pen.up()
    pen.goto(0, -150)
    pen.down()
    pen.width(3)   
    
    # Draw hour numbers
    pen.up()
    for hour in range(1, 13):
        angle = math.radians(30 * hour)
        x = 120 * math.sin(angle)
        y = 120 * math.cos(angle)
        pen.goto(x - 10, y - 10)
        pen.write(str(hour), font=("Arial", 18, "bold"))

def draw_hand(angle, length, width, color):
    pen.penup()
    pen.goto(0, 0)
    pen.color(color)
    pen.setheading(90)
    pen.right(angle)
    pen.pendown()
    pen.width(width)
    pen.forward(length)
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

def update_clock():
    pen.clear()
    draw_clock_face()

    # Get current time
    t = time.localtime()
    hour = t.tm_hour % 12
    minute = t.tm_min
    second = t.tm_sec

    # Calculate angles
    hour_angle = (30 * hour) + (0.5 * minute)
    minute_angle = 6 * minute
    second_angle = 6 * second

    # Draw hands
    draw_hand(hour_angle, 80, 6, "white")
    draw_hand(minute_angle, 120, 4, "white")
    draw_hand(second_angle, 140, 2, "blue")

    screen.update()
    # Call this function again after 1000ms (1 second)
    screen.ontimer(update_clock, 1000)

# Initial call to start the clock
update_clock()
turtle.done()
