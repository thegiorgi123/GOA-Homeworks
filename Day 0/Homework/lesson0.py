from turtle import *

#we want to draw a house
speed(5)
#step 1: draw a square
width(8)
begin_fill()
color("Purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
end_fill()
#step 2: draw a door
begin_fill()
left(90)
forward(70)
color("Green")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()

#step 3: draw a triangle
goto(200, 200)
pendown()
color("yellow")

begin_fill()

right(150)
forward(200)
left(120)
forward(200)
end_fill()
penup()

#step 4: draw first window

goto(0, 0)
right(150)
color("brown")
begin_fill()
forward(125)
pendown()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
penup()


#draw second window
penup()
goto(200, 200)
left(90)
pendown()
color("purple")
forward(25)
color("brown")
begin_fill()
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

exitonclick()