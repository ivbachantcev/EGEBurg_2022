from turtle import *
colors_for_pens = ['yellowgreen', 'red', 'green', 'blue', 'brown']
leo = Turtle()
leo.width(2)
leo.speed(10)
dlina = 250
for i in range(10):
    leo.begin_fill()
    for j in range(4):
        leo.fillcolor(colors_for_pens[i % 5])
        leo.forward(dlina)
        leo.left(90)
    leo.end_fill()
    dlina -= 20
mainloop()