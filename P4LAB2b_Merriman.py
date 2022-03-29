import turtle

wn = turtle.Screen()      
tmnt = turtle.Turtle()
tmnt.shape("turtle")
turtle.colormode(255)
tmnt.color(227, 155, 212)
tmnt.pensize(4)

tmnt.left(90)
tmnt.forward(150)
tmnt.left(90)
tmnt.forward(50)
tmnt.left(180)
tmnt.forward(100)#complete the "T"
tmnt.penup()#move into position for the "M"
tmnt.forward(50)
tmnt.right(90)
tmnt.forward(150)
tmnt.right(180)
tmnt.pendown()
tmnt.forward(150)#begin "M"
tmnt.right(135)
tmnt.forward(40)
tmnt.left(90)
tmnt.forward(40)
tmnt.right(135)
tmnt.forward(150)#finish

wn.mainloop()
