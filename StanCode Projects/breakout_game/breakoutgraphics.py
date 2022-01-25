"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, dy=0,
                 dx=0, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        self.ball_radius = ball_radius
        self.paddle_width = paddle_width
        self.__dx = dx
        self.__dy = dy
        self.started = False

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=window_width/2-paddle_width/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball)

        # Default initial velocity for the ball
        # self.initial_y_speed = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.move_paddle)
        onmouseclicked(self.start_animation)

        # Draw bricks
        colors = ["red", "red", "orange", "orange", "yellow", "yellow", "green", "green", "blue", "blue"]
        cur_row = 0
        for i in range(0, brick_rows*(brick_width+brick_spacing), brick_width + brick_spacing):
            for j in range(0, brick_cols*(brick_height+brick_spacing), brick_height + brick_spacing):
                brick = GRect(brick_width, brick_height, x=i, y=j)
                brick.filled = True
                brick.fill_color = colors[cur_row]
                cur_row += 1
                self.window.add(brick)
            cur_row = 0


    def move_paddle(self, event):

        if event.x - self.paddle_width/2 < 0:
            self.paddle.x = 0
        elif event.x + self.paddle_width/2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle_width
        else:
            self.paddle.x = event.x - self.paddle_width / 2

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def start_animation(self, event):
        if not self.started:
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            # x velocity possible change signs
            if random.random() > 0.5:
                self.__dx = -self.__dx
            self.started = True

    def hit_object(self, object_):
        if object_ != self.paddle:
            self.window.remove(object_)

    def reset(self):
        self.ball.x, self.ball.y = self.window.width/2-self.ball_radius, self.window.height/2-self.ball_radius

    def lose(self):
        self.window.clear()
        text = GLabel("GAME OVER", x=100, y=100)
        self.window.add(text)
