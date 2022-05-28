from turtle import *
leo = Turtle()
leo.width(2)
leo.speed(25)
dlina = 40
for j in range(8):
    for i in range(4):
        leo.forward(dlina)
        leo.left(90)
    leo.left(45)
mainloop()