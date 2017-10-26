from turtle import *
shape('turtle')
color('black')
bgcolor('light blue')

penup()
forward(600)
left(90)
pendown()
forward(475)
left(90)
forward(1200)
left(90)
forward(935)
left(90)
forward(1200)
left(90)
forward(475)
penup()

    

home()
def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    angle = 180 - (360 / points)

    color(line, fill)
    begin_fill()
    for i in range(points):
        forward(200)
        left(angle)
    end_fill()

    
speed(100)

def f():
    fd(50)
    lt(60)
onscreenclick(f, btn=1, add=None)
draw_star(-500, 300, 24, 'white', 'yellow')
penup()
colormode(225)
home()
penup()
color('green')
right(90)
forward(300)
left(90)
back(600)
pendown()
forward(1200)

if filling():
    pensize(5)
else:
    pensize(3)

colormode(255)
color('red')

penup()
home()
pendown()
penup()
right(90)
forward(300)
left(360)
left(90)
pendown()



def drawSquare(t, dist):
    for x in range(4):
        forward(dist)
        left(90)

def drawRegularPolygon(t, dist, s):
    for x in range(s):
        forward(dist)
        left(360/s)


def drawHouse(t, dist):
    drawRegularPolygon(t, dist, 4) 
    up()
    left(90)
    forward(dist) 
    right(90) 
    down()
    drawRegularPolygon(t, dist, 3)
drawHouse(-300, 200)

move = Turtle()
showturtle()

def k1():
    move.forward(45)

def k2():
    move.left(45)

def k3():
    move.right(45)

def k4():
    move.back(45)

onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")

listen()
mainloop()
turtle.shape("turtle")
turtle.color("green")






    



