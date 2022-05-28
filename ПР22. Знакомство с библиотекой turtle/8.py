from turtle import *
leo = Turtle()
colors = ['red', 'green', 'blue', 'brown']
leo.width(1)
leo.speed(25)
r = 100
for j in range(36):
    leo.pencolor(colors[j % 4])
    leo.circle(r)
    leo.left(10)
mainloop()