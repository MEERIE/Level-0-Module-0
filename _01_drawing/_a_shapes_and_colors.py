import turtle
from turtle import Turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('orange')

    # This code makes a new Turtle. Pick a new name for the turtle
    chad: Turtle = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    chad.shape('turtle')
    # Set your turtle's speed using .speed(2)
    chad.speed(10)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    chad.color('green')
    chad.pencolor('blue')
    # Move your turtle forward using .forward(100)

    # TEST    Did your turtle move forward?
    # Move your turtle left or right using .left(90) or .right(90)

    # Now put the forward and left/right code into a for loop to repeat 4 times.

    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen

    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    radius = 50
    chad.color("blue")
    chad.begin_fill()
    chad.circle(radius, steps=100)
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    chad.end_fill()
    # Draw 3 more shapes with different fill colors!
    chad.penup()
    chad.goto(100, 300)
    chad.pendown()
    chad.begin_fill()
    for i in range(50):
        chad.right(108)
        chad.forward(75)
        chad.color("red")
    chad.end_fill()

    chad.penup()
    chad.goto(100, 50)
    chad.pendown()
    chad.begin_fill()
    for i in range(5):
        chad.right(72)
        chad.forward(75)
        chad.color("green")
    chad.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
