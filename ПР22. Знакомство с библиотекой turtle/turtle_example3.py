from turtle import *
leo = Turtle()
leo.speed(10)
leo.fillcolor('orange')
leo.begin_fill()
for i in range(4):
    leo.circle(100, 90)  # рисование дуги радиусом 100 и углом 90 градусов
    leo.right(180)
leo.end_fill()
mainloop()