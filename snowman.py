Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from turtle import*

# creating the base or Bottom circle for snow man and women
title("snow man")
Phani=Turtle()

Phani.up()
Phani.goto(50,-260)
Phani.down()
Phani.color("black")
Phani.width(width=5)
Phani.fill(1)
Phani.fill(0)
Phani.circle(90)
Phani.hideturtle()

Phani=Turtle()
Phani.up()
Phani.goto(-200,-250)
Phani.down()
Phani.color("red")
Phani.width(width=5)
Phani.fill(1)
Phani.fill(0)
Phani.circle(90)
Phani.hideturtle()

    
# creating the center circle for snow man and women

Phani.up()
Phani.goto(50,-80)
Phani.down()
Phani.color("black")
Phani.width(width=5)
Phani.fill(1)
Phani.fill(0)
Phani.circle(60)
Phani.hideturtle()

Phani.up()
Phani.goto(-200,-70)
Phani.down()
Phani.color("red")
Phani.width(width=5)
Phani.fill(1)
Phani.fill(0)
Phani.circle(60)
Phani.hideturtle()

Phani.up()
Phani.goto(50,0)
Phani.down()
Phani.color("green")
Phani.width(width = 3)
Phani.fill(1)
Phani.fill(0)
Phani.circle(4)
Phani.hideturtle()

Phani.up()
Phani.goto(-200,20)
Phani.down()
Phani.color("green")
Phani.width(width = 3)
Phani.fill(1)
Phani.fill(0)
Phani.circle(4)
Phani.hideturtle()

Phani.up()
Phani.goto(50,20)
Phani.down()
Phani.color("green")
Phani.width(width = 3)
Phani.fill(1)
Phani.fill(0)
Phani.circle(4)
Phani.hideturtle()

Phani.up()
Phani.goto(-200,10)
Phani.down()
Phani.color("green")
Phani.width(width = 3)
Phani.fill(1)
Phani.fill(0)
Phani.circle(4)
Phani.hideturtle()

Phani.up()
Phani.goto(50,30)
Phani.down()
Phani.color("green")
Phani.width(width = 3)
Phani.fill(1)
Phani.fill(0)
Phani.circle(4)
Phani.hideturtle()

Phani.up()
Phani.goto(-200,-10)
Phani.down()
Phani.color("green")
Phani.width(width = 3)
Phani.fill(1)
Phani.fill(0)
Phani.circle(4)
Phani.hideturtle()

   
# creating the top circle for snow man and women

Phani.up()
Phani.goto(50,40)
Phani.down()
Phani.color("black")
Phani.width(width=5)
Phani.fill(1)
Phani.fill(0)
Phani.circle(30)
Phani.hideturtle()

#creating the eyes for snow man
Phani.up()
Phani.goto(60,80)
Phani.down()
Phani.color("blue")
Phani.width(width = 3)
Phani.fill(1)
Phani.fill(0)
Phani.circle(2)
Phani.hideturtle()

Phani.up()
Phani.goto(40,80)
Phani.down()
Phani.color("blue")
Phani.width(width = 3)
Phani.fill(1)
Phani.fill(0)
Phani.circle(2)
Phani.hideturtle()

 # creating the top circle for snow women
Phani.up()
Phani.goto(-200,50)
Phani.down()
Phani.color("red")
Phani.width(width=3)
Phani.fill(1)
Phani.fill(0)
Phani.circle(30)
Phani.hideturtle()

#creating the eyes for snow women
Phani.up()
Phani.goto(-190,90)
Phani.down()
Phani.color("blue")
Phani.width(width = 2)
Phani.fill(1)
Phani.fill(0)
Phani.circle(3)
Phani.hideturtle()

Phani.up()
Phani.goto(-210,90)
Phani.down()
Phani.color("blue")
Phani.width(width = 2)
Phani.fill(1)
Phani.fill(0)
Phani.circle(3)
Phani.hideturtle()



#creating the hats for snow women
Phani=Turtle()

for i in range(1):
    Phani.right(2/2)

Phani.penup()
Phani.goto(-250, 110)
Phani.pendown()
Phani.forward(100)
Phani.left(90)
Phani.forward(10)
Phani.left(90)
Phani.forward(100)
Phani.left(90)
Phani.forward(10)
Phani.left(90)
Phani.pencolor("brown")

for i in range(3):

    Phani.forward(90)

    Phani.left(360/3)

for i in range(1):

    Phani.right(2/2)

# creating a cap for snow mann

for i in range(1):

    Phani.right(4/4)

    Phani.forward(60)

Phani.penup()

Phani.goto(0, 100)
Phani.pencolor("brown")
Phani.pendown()

Phani.forward(100)

Phani.left(90)

Phani.forward(10)

Phani.left(90)

Phani.forward(100)

Phani.left(90)

Phani.forward(10)

Phani.left(90)

for i in range(3):

    Phani.forward(90)

    Phani.left(400/4)

for i in range(1):

    Phani.right(2/2)

    Phani.forward(60)
    Phani.hideturtle()


#creating the nose for snow man and women

Phani.penup()
Phani.goto(50, 70)
Phani.pendown()
Phani.fill(1)
Phani.circle(2)
Phani.color("blue")


Phani.penup()
Phani.goto(-200, 80)
Phani.pendown()
Phani.fill(1)
Phani.circle(2)
Phani.color("blue")

#creating the hands for snow man and women

Phani.penup()
Phani.goto(110,0)
Phani.pendown()
Phani.forward(90)

Phani.penup()
Phani.goto(-10, 00)
Phani.pendown()
for i in range(1):

    Phani.right(90/2)

    Phani.forward(90)
Phani.hideturtle()


Phani.penup()
Phani.goto(-60, 40)
Phani.pendown()
Phani.hideturtle()
for i in range(1):
    Phani.right(90/2)
    Phani.forward(90)

Phani.penup()
Phani.goto(-260,0)
Phani.pendown()
Phani.hideturtle()


for i in range(1):

    Phani.right(60/2)

    Phani.forward(90)

