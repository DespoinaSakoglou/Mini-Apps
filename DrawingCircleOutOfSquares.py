# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 16:20:59 2018

@author: Despoina
"""

import turtle

def draw_square(some_turtle):
    for i in range (1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create turtle brad
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    
    #create turtle angie
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    
    window.exitonclick()
    
draw_art()