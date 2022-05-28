from turtle import *
leo = Turtle()
colors = ['red', 'green', 'blue', 'brown']
leo.width(2)
leo.speed(25)
dlina = 40
for j in range(20):
    leo.pencolor(colors[j % 4])
    for i in range(4):
        leo.forward(dlina)
        leo.left(90)
    dlina += 5
    leo.left(10)
mainloop()