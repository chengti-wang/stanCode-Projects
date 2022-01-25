"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
clicks = 0
prev_coord = (0, 0)
cir = None
def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(create_circle)

def create_circle(event):
    global clicks, prev_coord, cir
    # to record the clicks
    clicks += 1

    # check click is odd or even
    if clicks % 2 == 1:
        # save this coordinate for next click to use to form a line
        prev_coord = (event.x, event.y)

        # create a circle
        cir = GOval(SIZE, SIZE, x=event.x-SIZE/2, y=event.y-SIZE/2)
        window.add(cir)

    else:
        # delete circle
        window.remove(cir)

        # create line from the two points
        line = GLine(prev_coord[0], prev_coord[1], event.x, event.y)
        window.add(line)
if __name__ == "__main__":
    main()
