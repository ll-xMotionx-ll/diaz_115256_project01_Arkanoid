from graphics import *
import random

canvasHeight,canvasWidth=500,500
class Paddle:

    def __init__(self,win):
        self.paddle=Rectangle(Point(200,20),Point(300,40))
        self.paddleCenter = 50
        self.paddle.setFill("black")
        self.paddle.draw(win)
    def setColor(self,color,win):
        self.paddle.setFill(color)
        self.paddle.draw(win)
    def movePaddle(self,):
        pass
    def getCenterX(self):
        return self.paddle.getCenter().getX()
    def getCenterY(self):
        return self.paddle.getCenter().getY()
    def moveRight(self):
         self.paddle.move(40.0,0.0)
    def moveLeft(self):
            self.paddle.move(-40.0,0.0)
    

class Ball:
    def __init__(self,win):
        self.ballRadius=25.0
        self.ball=Circle(Point(250,65),self.ballRadius)
        self.ball.setFill("red")
        self.ball.draw(win)
        self.ballXspeed=5.0
        self.ballYspeed=5.0
    def getCenterX(self):
        return self.ball.getCenter().getX()
    def getCenterY(self):
        return self.ball.getCenter().getY()
    def getBallRadius(self):
        return self.ballRadius
    def setBallXspeed(self,x):
        self.ballXspeed=x
    def setBallYspeed(self,y):
        self.ballYspeed=y
    def getBallXspeed(self):
        return self.ballXspeed
    def getBallYspeed(self):
        return self.ballYspeed
    def ballMove(self):
        self.ball.move(self.ballXspeed,self.ballYspeed)


# Canvas
def canvasDisplay():

    #canvasHeight,canvasWidth=500,500

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

    paddle= Paddle(win)
    ball=Ball(win)
    
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
        if (ball.getCenterX()+ball.getBallRadius()) >= canvasWidth or (ball.getCenterX()-ball.getBallRadius()) <= 0:
            ball.setBallXspeed(ball.getBallXspeed()*-1.0)
            
        if (ball.getCenterY()+ball.getBallRadius()) >= canvasHeight or (ball.getCenterY()-ball.getBallRadius()) <= 0:
            ball.setBallYspeed(ball.getBallYspeed()*-1.0)
            
        
        # Making ball bounce of brick and eliminate the brick that touches
        for i in range(len(brick)):
            if (ball.getCenterY()-ball.getBallRadius() >= brick[i].getCenter().getY()-50) and (brick[i].getCenter().getX() - 25 < ball.getCenterX() < brick[i].getCenter().getX() + 25):
                brick[i].undraw()
                brick[i].move(0,75)
                ball.setBallYspeed(ball.getBallYspeed()*-1.0)

        # Movement of ball
        ball.ballMove()

        # Movement of the paddle left or right with keys
        key = win.checkKey()
        if key == "Right":
            if 450!=paddle.getCenterX():
                paddle.moveRight()
        if key == "Left":
            if 50!=paddle.getCenterX():
                paddle.moveLeft()
        
        # Make ball bounce from paddle
        if (ball.getCenterY()-ball.getBallRadius() <= 40.0 ) and (ball.getCenterX()+ball.getBallRadius() > paddle.getCenterX() - 50) and (ball.getCenterX()-ball.getBallRadius() < paddle.getCenterX() + 50):
            ball.setBallYspeed(ball.getBallYspeed()*-1.0)
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