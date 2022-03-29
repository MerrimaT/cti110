import turtle

wn = turtle.Screen()      
tmnt = turtle.Turtle()
tmnt.shape("turtle")
turtle.colormode(255)
tmnt.color(127, 255, 212)
tmnt.pensize(5)


for i in range(4):
    tmnt.forward(150)
    tmnt.left(90)
else:
    tmnt.forward(150)

tmnt.right(45)
tmnt.penup()
tmnt.forward(150)
tmnt.pendown()
tmnt.right(45)

for j in range(4):
    tmnt.forward(150)
    tmnt.right(120)

wn.mainloop()

                
    
