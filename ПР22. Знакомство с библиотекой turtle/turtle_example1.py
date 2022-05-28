from turtle import *
leo = Turtle()
dlina = 40  # длина стороны
for i in range(5):  # рисуем 5 квадратов
    leo.width(i + 1)
    leo.color('red', 'grey')  # цвет пера и цвет заливки
    leo.begin_fill()  # включаем закрашивание области
    for j in range(4):  # русуем очередной квадрат
        leo.forward(dlina)
        leo.left(90)
    leo.end_fill()  # выключаем закрашивание области
    leo.up()  # поднимаем перо, чтобы при перемещении на нувую позицию не оставался след
    dlina += 10  # увеличиваем длину стороны следующего квадрата
    leo.forward(dlina)  # перемещаемся на стартовую позицию нового квадрата
    leo.down()  # опускаем перо
mainloop()
