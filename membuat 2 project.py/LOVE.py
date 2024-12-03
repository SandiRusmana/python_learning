import turtle

turtle.bgcolor("black")
turtle.pensize(2)


def smakzie():
    for x in range(200):
        turtle.right(1)
        turtle.forward(2)

turtle.speed()
turtle.color("pink","red")

turtle.begin_fill()
turtle.left(150)
turtle.forward(111.0)
smakzie()

turtle.left(120)
smakzie()
turtle.forward(111.60)
turtle.end_fill()
turtle.hideturtle

sandi = turtle.Turtle()
sandi.penup()
sandi.goto(-200,50)
sandi.pendown()
sandi.color("white")
style = ('courier',20,'italic')
sandi.write('I',font=style,align="left")
sandi.hideturtle()


sandi=turtle.Turtle()
sandi.penup()
sandi.goto(-2,75)
sandi.pendown()
sandi.color("white")
style = ('courier',20,'italic')
sandi.write('LOVE',font=style,align='left')
sandi.hideturtle()

sandi=turtle.Turtle()
sandi.penup()
sandi.goto(190,80)
sandi.pendown()
sandi.color("white")
style = ('courier',20,'italic')
sandi.write('YOU',font=style,align='left')
sandi.hideturtle()

sandi=turtle.Turtle()
sandi.penup()
sandi.goto(-150,-130)
sandi.pendown()
sandi.color("white")
style = ('courier',20,'italic')
sandi.write('CLEVERZIE',font=style,align='left')
sandi.hideturtle()

turtle.done()



#link youtube
#https://youtu.be/D8dm7_c500CY?si=4yOYxzjJlGOtS8bK