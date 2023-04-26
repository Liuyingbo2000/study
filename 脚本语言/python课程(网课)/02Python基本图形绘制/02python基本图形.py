# Python蟒蛇绘制实列
import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/30)
turtle.down()

# 举一反三

# import turtle
# turtle.left(45)
# turtle.fd(150)
# turtle.right(135)
# turtle.fd(300)
# turtle.left(135)
# turtle.fd(150)

#from 库名 import *

# from turtle import *
# setup(650,350,200,200)
# penup()
# fd(-250)
# pendown()
# pensize(25)
# pencolor("purple")
# seth(-40)
# for i in range(4):
#     circle(40,80)
#     circle(-40,80)
# circle(40,80/2)
# fd(40)
# circle(16,180)
# fd(40*2/30)
# down()