import turtle
import random

wn = turtle.Screen()      
tmnt = turtle.Turtle()
tmnt.shape("turtle")
colours = ["cyan", "purple", "white", "blue"]
tmnt.color("cyan")
tmnt.pensize(2)
wn.bgcolor("grey")


tmnt.penup()
tmnt.forward(90)
tmnt.left(45)
tmnt.pendown()

def branch():
    for i in range(3):
        for i in range(3):
            tmnt.forward(30)
            tmnt.backward(30)
            tmnt.right(45)
        tmnt.left(90)
        tmnt.backward(30)
        tmnt.left(45)
    tmnt.right(90)
    tmnt.forward(90)

for i in range(8):
    branch()
    tmnt.left(45)
    tmnt.color(random.choice(colours))

#for i in range(20):   #first snowflake
    #for i in range(2):
        #tmnt.forward(150)
        #tmnt.right(160)
        #tmnt.forward(100)
        #tmnt.left(140)
        #tmnt.forward(150)
        #tmnt.right(145)
        #tmnt.forward(25)
        #tmnt.left(120)
        #tmnt.forward(25)
        #tmnt.right(140)
        #tmnt.forward(150)
    #tmnt.right(32)
    #tmnt.color(random.choice(colours))

wn.mainloop()
