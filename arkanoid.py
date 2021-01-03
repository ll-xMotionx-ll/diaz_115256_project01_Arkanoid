from graphics import *
import random


# Canvas
canvasHeight,canvasWidth=500,500

win = GraphWin("Arkanoid",canvasWidth,canvasHeight)
win.setBackground(color_rgb(63, 195, 182))
win.setCoords(0,0,500,500)
ballRadius=25.0


# Paddle
#paddle=Rectangle(Point(200,20),Point(300,40))
#paddle.draw(win)
# Bounce ball
# Bricks
# gameplay
def gameplay():

    paddle=Rectangle(Point(200,20),Point(300,40))
    paddleCenter = 50
    paddle.draw(win)

    ball=Circle(Point(250,65),ballRadius)
    ball.draw(win)
    ballXspeed=7
    ballYspeed=7
    
    #Bricks
    brick=[]
    for i in range(10):
        brick.append(Rectangle(Point(50*i,425),Point((i*50)+50,475)))
        brick[i].setFill(color_rgb(random.randint(30,255),random.randint(30,255),random.randint(30,255)))
        brick[i].draw(win)



    gameOver=False

    win.getMouse()

    while True:

        # Making ball bounce on the boundaries of the page
        if (ball.getCenter().getX()+ballRadius) >= canvasWidth or (ball.getCenter().getX()-ballRadius) <= 0:
            ballXspeed = ballXspeed * -1
        if (ball.getCenter().getY()+ballRadius) >= canvasHeight or (ball.getCenter().getY()-ballRadius) <= 0:
            ballYspeed = ballYspeed * -1
        # Define bricks
        for i in range(len(brick)):
            if (ball.getCenter().getY() - ballRadius >= brick[i].getCenter().getY()-50) and (brick[i].getCenter().getX() - 25 < ball.getCenter().getX() < brick[i].getCenter().getX() + 25):
                brick[i].undraw()
                brick[i].move(0,75)
                ballYspeed *= -1

        # movement of ball
        ball.move(ballXspeed, ballYspeed)

        # movement of the paddle left or right with keys
        key = win.checkKey()
        if key == "Right":
            if 450!=paddle.getCenter().getX():
                paddle.move(40.0,0.0)
        if key == "Left":
            if 50!=paddle.getCenter().getX():
                paddle.move(-40.0,0.0)
        
        # make ball bounce from paddle
        if (ball.getCenter().getY() - ballRadius <= 40.0 ) and (ball.getCenter().getX() + ballRadius > paddle.getCenter().getX() - 50) and (ball.getCenter().getX() - ballRadius < paddle.getCenter().getX() + 50):
            ballYspeed = ballYspeed * -1
        
            



def main():
    
    gameplay()
    

main()