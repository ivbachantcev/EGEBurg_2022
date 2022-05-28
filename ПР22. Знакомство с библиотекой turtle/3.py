from turtle import *
colors_for_pens = ['yellowgreen', 'red', 'green', 'blue', 'brown']
leo = Turtle()
leo.width(2)
leo.speed(10)
dlina = 450
for i in range(10):
    leo.begin_fill()
    for j in range(3):
        leo.fillcolor(colors_for_pens[i % 5])
        leo.forward(dlina)
        leo.left(120)
    leo.end_fill()
    leo.forward(20)
    dlina -= 40
mainloop()