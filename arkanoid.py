from graphics import *

#TK_SILENCE_DEPRECATION=1

# Canvas
canvasHeight,canvasWidth=500,500

win = GraphWin("Arkanoid",canvasWidth,canvasHeight)
win.setBackground(color_rgb(63, 195, 182))
win.setCoords(0,0,500,500)
ballRadius=25


# Paddle
#paddle=Rectangle(Point(200,20),Point(300,40))
#paddle.draw(win)

def movingPaddle(paddle,clickPoint):
    
    while True:
        #if(clickPoint):
        paddle.move(clickPoint.getX(),30)
            #paddle.draw(win)
    

# Bounce ball
# Bricks
# gameplay
def gameplay():

    paddle=Rectangle(Point(200,20),Point(300,40))
    paddleCenter = 50
    paddle.draw(win)

    ball=Circle(Point(150,200),ballRadius)
    ball.draw(win)
    ballXspeed=7
    ballYspeed=7
    
    gameOver=False


    while True:

        # Making ball bounce un the boundaries of the page
        if (ball.getCenter().getX()+ballRadius) >= canvasWidth or (ball.getCenter().getX()-ballRadius) <= 0:
            ballXspeed = ballXspeed * -1
        if (ball.getCenter().getY()+ballRadius) >= canvasHeight or (ball.getCenter().getY()-ballRadius) <= 0:
            ballYspeed = ballYspeed * -1
        
        # movement of ball
        ball.move(ballXspeed, ballYspeed)

        # movement of the paddle left or right with keys
        key = win.checkKey()
        if key == "Right":
            if 450!=paddle.getCenter().getX():
                paddle.move(20.0,0.0)
        if key == "Left":
            if 50!=paddle.getCenter().getX():
                paddle.move(-20.0,0.0)

                
            
            



def main():
    
    gameplay()
    win.getMouse()

main()