from turtle import *
leo = Turtle()
colors = ['red', 'orange', 'pink', 'blue']  # список цветов
leo.width(2)
radius = 140  # стартовый радиус окружности
leo.speed(10)  # скорость рисований
for i in range(10):
    leo.begin_fill()
    leo.fillcolor(colors[i % 4])  # установка цвета заливки
    leo.circle(radius)  # рисование окружности с нужным радиусом
    leo.end_fill()
    radius -= 10
mainloop()