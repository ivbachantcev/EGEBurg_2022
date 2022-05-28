from turtle import *
leo = Turtle()
colors = ['red', 'green', 'blue', 'brown']
leo.width(1)
leo.speed(25)
dlina = 40
for j in range(20):
    for i in range(4):
        leo.pencolor(colors[i % 4])
        leo.forward(dlina)
        leo.left(90)
    dlina += 5
    leo.left(10)
mainloop()