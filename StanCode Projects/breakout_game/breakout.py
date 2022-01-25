"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    lose = False
    # Add the animation loop here!
    vx = graphics.get_dx()
    vy = graphics.get_dy()
    print(vx, vy)
    while True:
        if graphics.started:
            vx = graphics.get_dx()
            vy = graphics.get_dy()
            graphics.started = False

        graphics.ball.move(vx, vy)

        if graphics.ball.x <= 0 or graphics.ball.x >= graphics.window.width - graphics.ball.width:
            vx = -vx
        if graphics.ball.y <= 0 or graphics.ball.y >= graphics.window.height - graphics.ball.height:

            if graphics.ball.y >= graphics.window.height - graphics.ball.height:
                graphics.reset()
                lives -= 1
                print("Lives minus 1")
                if lives == 0:
                    print("LOSE")
                    lose = True
                    break
            vy = -vy

        for x in range(int(graphics.ball.x), int(graphics.ball.x + graphics.ball_radius*2), graphics.ball_radius*2):
            for y in range(int(graphics.ball.y), int(graphics.ball.y + graphics.ball_radius*2), graphics.ball_radius*2):
                maybe_object = graphics.window.get_object_at(x, y)
                if maybe_object != None:
                    vy = -vy
                    graphics.hit_object(maybe_object)
                    break

        pause(FRAME_RATE)

    if lose:
        graphics.lose()


if __name__ == '__main__':
    main()
