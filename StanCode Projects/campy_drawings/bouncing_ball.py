"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = (0, 0, 0)
window.add(ball)

# boolean to checking if the animation is running or not
finished_running = 1

# variable for counting number of animation ran
animation_ran = 0
def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(start_animation)


def start_animation(event):
    global finished_running, animation_ran

    # stopping the animation from starting if animation is currently running OR the animation has run for over 3 times
    if finished_running == 1 and animation_ran < 3:
        # add one to the animation count
        animation_ran += 1
        # start the animation therefore the the code hasn't finished running
        finished_running = 0
        # vertical velocity starts with 0
        vy = 0
        while True:
            finished_running = 0

            # move the ball
            ball.move(VX, vy)
            # increase the y-velocity by GRAVITY
            vy += GRAVITY
            # check if the ball hits the ground
            if ball.y+ball.height >= window.height:
                vy = -vy
                vy *= REDUCE
            # check if the ball is out of the screen
            if ball.x+ball.width >= window.width:
                break;
            pause(DELAY)

        # setting ball back to original position
        ball.x = START_X
        ball.y = START_Y
        finished_running = 1
if __name__ == "__main__":
    main()
