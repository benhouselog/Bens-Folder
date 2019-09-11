"""
import turtle

window= turtle.screen()
drawing_turtle = turtle.Pen()

colors = {'red', 'purple', 'blue', 'green', 'orange', 'yellow'}
window.bgcolor('black')

for i in range(360)
drawing_turtle.pencolor(colors[i%6])
drawing_turtle.width(1/100+1)
drawing_turtle.forward(i)
drawing_turtle.left(59)

turtle.done()
"""




"""
#print("What is your favorite number?")
#favorite_number = input("What is your favorite number?")
#num_1 = int(input("input number 1: "))
#num_2 = int(input("input number 2: "))
#"1+1 = 2"

#print("X + X = X")
#print("%d + %d = %d") % (num_1, num_2)
"""
"""
import turtle 
screen = turtle.Screen()
screen.bgcolor("pink") 
screen.title("CIS-121") 
drawing_turtle = turtle.Turtle() 
drawing_turtle.forward(100)
drawing_turtle.left(90)

drawing_turtle.forward(100)
drawing_turtle.left(90)

drawing_turtle.forward(100)
drawing_turtle.left(90)

drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)
drawing_turtle.left(90)
drawing_turtle.forward(100)




turtle.done()
"""

import turtle

window = turtle.Screen()
window.title("Danny Devito")
window.bgcolor("blue")
drawing_turtle = turtle.Turtle()
drawing_turtle.forward(100)
drawing_turtle.left(60)
drawing_turtle.forward(100)
drawing_turtle.left(60)
drawing_turtle.forward(100)
drawing_turtle.left(60)
drawing_turtle.forward(100)
drawing_turtle.left(60)
drawing_turtle.forward(100)
drawing_turtle.left(60)
drawing_turtle.forward(100)
drawing_turtle.left(60)
drawing_turtle.forward(100)
drawing_turtle.left(60)


turtle.done()



import turtle
import time
import random
window = turtle.Screen()
drawing_turtle = turtle.Turtle()

num_sides= input("Enter the number of sides of the shape you want.")
if num_sides.isdigit():
    num_sides = int(num_sides)

angle= 180-180*(num_sides-2)/num_sides
drawing_turtle.up

x = 0
y = 0
drawing_turtle,setpos(x,y)

num_shapes = 24
for _ in range (num_shapes): 
    drawing_turtle.color(random.random(), random.random(), random.random())
    x += 5
    y += 5
    drawing_turtle.forward(x)
    drawing_turtle.left(y)
    for _ in range(num_sides):
    drawing_turtle.begin_fill()
    drawing_turtle.down()
    drawing_turtle.forward(40)
    drawing_turtle.left(angle)
    drawing_turtle.forward(40)
    print(drawing_turtle.pos())
    drawing_turtle.up()
    drawing_turtle.end_fill()

    turtle.done()





































