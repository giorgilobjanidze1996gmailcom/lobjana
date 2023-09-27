from turtle import *

#we want paint a house
#step 1:draw a square
width(7)
speed(10)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

forward(70)
color("green")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
penup()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)

end_fill()

#paint windows
goto(140,180)
begin_fill()
color("yellow")
left(30)
pendown()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

penup()
begin_fill()
color("yellow")
goto(40,180)
left(90)
pendown()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


exitonclick()

