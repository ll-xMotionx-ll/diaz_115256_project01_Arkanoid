from graphics import *
import random


# Canvas
def canvasDisplay():

    canvasHeight,canvasWidth=500,500

    win = GraphWin("Arkanoid",canvasWidth,canvasHeight)
    win.setBackground(color_rgb(63, 195, 182))
    win.setCoords(0,0,500,500)
    return win

# Welcome function
def welcome(win):
    welcome = Text(Point(250,250),"Welcome to Arkanoid\nProgram by Daniel Diaz")
    start = Text(Point(250,200),"To start game click in any part of the page to start\n to move the paddle you need to use your left and right directional keys\n objective of the game the ball need to bounce from the paddle \nso you can heat the brick and the brick will disappeard after \nall bricks are gone you win the game")
    welcome.draw(win)
    start.draw(win)
    if win.getMouse():
        welcome.undraw()
        start.undraw()

def gameplay(win):

    # Paddle
    paddle=Rectangle(Point(200,20),Point(300,40))
    paddleCenter = 50
    paddle.setFill("black")
    paddle.draw(win)

    # Ball
    ball=Circle(Point(250,65),ballRadius)
    ball.setFill("red")
    ball.draw(win)
    ballXspeed=5.0
    ballYspeed=5.0
    ballRadius=25.0
    
    #Bricks
    brick=[]
    for i in range(10):
        brick.append(Rectangle(Point(50*i,425),Point((i*50)+50,475)))
        brick[i].setFill(color_rgb(random.randint(30,255),random.randint(30,255),random.randint(30,255)))
        brick[i].draw(win)

    # while gameover is false the loop will continue untill is true
    gameOver=False
    while not gameOver:

        # Making ball bounce on the boundaries of the page
        if (ball.getCenter().getX()+ballRadius) >= canvasWidth or (ball.getCenter().getX()-ballRadius) <= 0:
            ballXspeed = ballXspeed * -1
        if (ball.getCenter().getY()+ballRadius) >= canvasHeight or (ball.getCenter().getY()-ballRadius) <= 0:
            ballYspeed = ballYspeed * -1
        
        # Making ball bounce of brick and eliminate the brick that touches
        for i in range(len(brick)):
            if (ball.getCenter().getY() - ballRadius >= brick[i].getCenter().getY()-50) and (brick[i].getCenter().getX() - 25 < ball.getCenter().getX() < brick[i].getCenter().getX() + 25):
                brick[i].undraw()
                brick[i].move(0,75)
                ballYspeed *= -1

        # Movement of ball
        ball.move(ballXspeed, ballYspeed)

        # Movement of the paddle left or right with keys
        key = win.checkKey()
        if key == "Right":
            if 450!=paddle.getCenter().getX():
                paddle.move(40.0,0.0)
        if key == "Left":
            if 50!=paddle.getCenter().getX():
                paddle.move(-40.0,0.0)
        
        # Make ball bounce from paddle
        if (ball.getCenter().getY() - ballRadius <= 40.0 ) and (ball.getCenter().getX() + ballRadius > paddle.getCenter().getX() - 50) and (ball.getCenter().getX() - ballRadius < paddle.getCenter().getX() + 50):
            ballYspeed = ballYspeed * -1
        update(30)
        #loop to see if all the brick disappear to exit the while loop
        count=0
        for i in range(len(brick)):
            if (brick[i].getCenter().getY()-25)==500:
                count=count+1
            if count == 10:
                gameOver=True

    # Finish the game
    finish = Text(Point(250,250),"You won!!!\n To exit click anywhere in the page")
    finish.draw(win)
    if win.getMouse():
        win.close()

            



def main():

    win=canvasDisplay()
    welcome(win)
    gameplay(win)
    

main()