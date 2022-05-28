from turtle import *
leo = Turtle()
leo.width(2)
leo.speed(20)
#рисование крыши
leo.fillcolor('brown')
leo.begin_fill()
for _ in range(3):
    leo.forward(100)
    leo.left(120)
leo.end_fill()
# рисование тела дома
leo.fillcolor('yellowgreen')
leo.begin_fill()
for _ in range(4):
    leo.forward(100)
    leo.right(90)
leo.end_fill()
# рисование окна
leo.up()
leo.right(45)
leo.forward(40)
leo.left(45)
leo.down()
leo.fillcolor('blue')
for j in range(4):
    leo.begin_fill()
    for i in range(4):
        leo.forward(15)
        leo.right(90)
    leo.end_fill()
    leo.left(90)
# рисование двери
leo.up()
leo. goto(50, -50)
leo.down()
leo.fillcolor('orange')
leo.begin_fill()
for _ in range(2):
    leo.forward(30)
    leo.right(90)
    leo.forward(50)
    leo.right(90)
leo.end_fill()
mainloop()