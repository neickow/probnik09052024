from turtle import *

tracer(0)
screensize(3000, 3000)
n = 50
left(90)
down()
for i in range(4):
    forward(6*n)
    right(150)
    forward(6*n)
    right(30)
up()
color('red')
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * n, y * n)
        dot(3)
done()