from turtle import *
colors_for_pens = ['yellowgreen', 'red', 'green', 'blue', 'brown']
leo = Turtle()
leo.width(2)
leo.speed(10)
dlina = 50
for i in range(10):
    for j in range(4):
        leo.pencolor(colors_for_pens[i % 5])
        leo.forward(dlina)
        leo.left(90)
    dlina += 20
leo.width(2)
mainloop()