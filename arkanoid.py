from graphics import *

#TK_SILENCE_DEPRECATION=1

# Canvas

#draw(win)
# Paddle
# Bounce ball
# Bricks
# gameplay


def main():
    canvasHeight,canvasWidth=500,500

    win = GraphWin("Arkanoid",canvasWidth,canvasHeight)
    win.setBackground(color_rgb(63, 195, 182))
    
    win.getMouse()
    #gameplay()

main()