#press "f" button for the color "fuchsia"
#press "t" button for the color "turquoise"
#use the "right" click" to draw "MEET"
#use the "left click" to draw "meet"
#press "c" button to clear the screen 


import turtle
x=0
y=0

def m(x,y):
    turtle.penup()
    turtle.goto(x-190,y-30)
    turtle.pendown()
    turtle.goto(x-190,y+30)
    turtle.right(90)
    turtle.circle(25,-180)
    turtle.goto(x-140,y)
    turtle.penup()
    turtle.goto(x-140,y+30)
    turtle.pendown()
    turtle.right(180)
    turtle.circle(25,-180)
    turtle.goto(x-90,y-30)

def e1(x,y):
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(x-60,y+20)
    turtle.pendown()
    turtle.goto(x+5,y+20)
    turtle.circle(32.5,180)
    turtle.goto(x-60,y-5)
    turtle.circle(32.5,80)

def e2(x,y):
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(x+25,y+20)
    turtle.pendown()
    turtle.goto(x+90,y+20)
    turtle.left(100)
    turtle.circle(32.5,180)
    turtle.penup()
    turtle.goto(x+90,y+20)
    turtle.pendown()
    turtle.goto(x+90,y-5)
    turtle.right(180)
    turtle.circle(32.5,-80)

def f(x,y):
    turtle.pensize(15)
    turtle.penup()
    turtle.goto(x+110,y+20)
    turtle.pendown()
    turtle.goto(x+170,y+20)
    turtle.penup()
    turtle.goto(x+135,y+55)
    turtle.pendown()
    turtle.goto(x+135,y-5)
    turtle.right(100)
    turtle.circle(30,90)

def TM(x,y):
    turtle.pensize(15)
    turtle.pensize(3)
    turtle.penup()
    turtle.goto(x+170,y+80)
    turtle.pendown()
    turtle.goto(x+185,y+80)
    turtle.penup()
    turtle.goto(x+177.5,y+80)
    turtle.pendown()
    turtle.goto(x+177.5,y+60)

    turtle.penup()
    turtle.goto(x+195,y+60)
    turtle.pendown()
    turtle.goto(x+195,y+80)
    turtle.goto(x+202.5,y+70)
    turtle.goto(x+210,y+80)
    turtle.goto(x+210,y+60)



def M(x,y):
    turtle.pensize(30)
    turtle.penup()
    turtle.goto(x-340,y-70)
    turtle.pendown()
    turtle.goto(x-340,y+70)
    turtle.goto(x-270,y+70)
    turtle.goto(x-270,y-70)
    turtle.penup()
    turtle.goto(x-270,y+70)
    turtle.pendown()
    turtle.goto(x-200,y+70)
    turtle.goto(x-200,y-70)

def E1(x,y):
    turtle.pensize(30)
    turtle.penup()
    turtle.goto(x-50,y-70)
    turtle.pendown()
    turtle.goto(x-150,y-70)
    turtle.goto(x-150,y)
    turtle.goto(x-50,y)
    turtle.penup()
    turtle.goto(x-150,y+70)
    turtle.pendown()
    turtle.goto(x-150,y)
    turtle.goto(x-150,y+70)
    turtle.goto(x-50,y+70)

def E2(x,y):
    turtle.pensize(30)
    turtle.penup()
    turtle.goto(x,y-70)
    turtle.pendown()
    turtle.goto(x+100,y-70)
    turtle.goto(x+100,y)
    turtle.goto(x,y)
    turtle.penup()
    turtle.goto(x+100,y)
    turtle.pendown()
    turtle.goto(x+100,y+70)
    turtle.goto(x,y+70)

def T(x,y):
    turtle.pensize(30) 
    turtle.penup()
    turtle.goto(x+150,y+70)
    turtle.pendown()
    turtle.goto(x+250,y+70)
    turtle.penup()
    turtle.goto(x+200,y+70)
    turtle.pendown()
    turtle.goto(x+200,y-70)


def frame(x,y):
    turtle.pensize(30)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(x-380,y+100)
    turtle.pendown()
    turtle.goto(-380,y-100)
    turtle.goto(x+290,y-100)
    turtle.goto(x+290,y+100)
    turtle.goto(x-380,y+100)
    turtle.end_fill()

def meet(x,y):
    turtle.pensize(15)
    m(x,y)
    e1(x,y)
    e2(x,y)
    f(x,y)
    TM(x,y)   

def MEET(x,y):
    M(x,y)
    E1(x,y)
    E2(x,y)
    T(x,y)



def color_fuchsia():
    turtle.pencolor("fuchsia")

def color_turquoise():
    turtle.pencolor("turquoise")

def clear():
    turtle.clear()

turtle.getscreen().onkeypress(color_fuchsia,"f")
turtle.getscreen().listen()

turtle.getscreen().onkeypress(color_turquoise,"t")
turtle.getscreen().listen()

turtle.getscreen().onkeypress(clear,"c")
turtle.getscreen().listen()


turtle.onscreenclick(meet,btn=1,add=True)
turtle.onscreenclick(MEET,btn=3,add=True)

turtle.mainloop



    




