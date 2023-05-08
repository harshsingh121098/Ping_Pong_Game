import turtle 
import winsound

wn=turtle.Screen()
wn.title("MY pong game")
wn.bgcolor("Black")
wn.setup(width=800, height=800)
wn.tracer(0)

#Score 
score_a=0
score_b=0
#Paddle A
pad_a=turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.penup()
pad_a.goto(-350,0)
pad_a.shapesize(stretch_wid=5, stretch_len=1)


#Paddle B
pad_b=turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.penup()
pad_b.goto(350,0)
pad_b.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx =0.3
ball.dy =-0.3

# Pen
pen= turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B:0", align="center",font=("courier",14,"normal"))


#function
def pad_a_up():
    y=pad_a.ycor()
    y+=20
    pad_a.sety(y)

#function
def pad_a_dn():
    y=pad_a.ycor()
    y-=20
    pad_a.sety(y)

#function
def pad_b_up():
    y=pad_b.ycor()
    y+=20
    pad_b.sety(y)

#function
def pad_b_dn():
    y=pad_b.ycor()
    y-=20
    pad_b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(pad_a_up, "w")
wn.onkeypress(pad_a_dn, "s")
wn.onkeypress(pad_b_up, "y")
wn.onkeypress(pad_b_dn, "h")



#Main game 
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)


    #Border Checking 
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        score_a+=1
        pen.clear()
        pen.write("Player A: {} Player B:{}".format(score_a, score_b), align="center",font=("courier",14,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *=-1
        score_b+=1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Player A: {} Player B:{}".format(score_a, score_b), align="center",font=("courier",14,"normal"))


    # Paddle Ball Collision
    if (ball.xcor()> 340 and ball.xcor()< 350) and (ball.ycor()<pad_b.ycor() +40 and ball.ycor() > pad_b.ycor()-50):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    
    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor()<pad_a.ycor() +40 and ball.ycor() > pad_a.ycor()-50):
        ball.setx(-340)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)



    
