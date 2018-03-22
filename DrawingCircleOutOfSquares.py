
"""
A program that uses the turtle module to draw shapes.
Drawing a circle out of drawing consecutive squares.

Created on Mon Mar 19 16:20:59 2018

@author: Despoina
"""

# import turtle graphics module to draw shapes
import turtle

# define a draw_square function that draws a single square
def draw_square(some_turtle):
    # use range() function to iterate over with for loop 4 times
    for i in range (1,5):
        # use turtle motion method forward() to move forward 100 pixels
        some_turtle.forward(100)
         # use turtle motion method right() to turn 90 degrees to the right
        some_turtle.right(90)

# define a draw_art() function that draws a cirlce out of drawing squares
def draw_art():
    # use turtle Screen to view drawing and set background color to red
    window = turtle.Screen()
    window.bgcolor("red")
    # create turtle object named my_turtle (object/instance of the class Turtle)
    my_turtle = turtle.Turtle()
    # set turtle shape to turtle and color to yellow
    my_turtle.shape("turtle")
    my_turtle.color("yellow")
    # set turtle speed to 2 for slow animation of line drawing and turtle turning
    my_turtle.speed(2)
    # use range() function to iterate over with for loop 36 times (this creates the circle)
    for i in range(1,37):
        # call draw_square() function by inputting the object my_turtle created above
        draw_square(my_turtle)
        # after drawing a square, object is turned 10 degrees to the right and the iteration continues for 36 times (360 degrees)
        my_turtle.right(10)
    
    # exit the Screen that displays the animation with a click
    window.exitonclick()
 
# call the draw_art() function 
draw_art()
