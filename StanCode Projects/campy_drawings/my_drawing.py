"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    window = GWindow(width=500, height=500, title="drawing")
    ear1 = GOval(100, 100, x=90, y=90)
    paint(ear1, (184, 115, 51))
    window.add(ear1)

    ear3 = GOval(80, 80, x=100, y=100)
    paint(ear3, (0, 0, 0))
    window.add(ear3)

    ear2 = GOval(100, 100, x=310, y=90)
    paint(ear2, (184, 115, 51))
    window.add(ear2)

    ear2 = GOval(80, 80, x=320, y=100)
    paint(ear2, (0,0,0))
    window.add(ear2)

    face = GOval(300, 310, x=100, y=100)
    face.filled = True
    face.fill_color = (184, 115, 51)
    window.add(face)

    eye1 = GOval(28, 40, x=200, y=215)
    eye1.filled = True
    paint(eye1, (0,0,0))
    window.add(eye1)

    eye2 = GOval(28, 40, x=270, y=215)
    paint(eye2, (0,0,0))
    window.add(eye2)

    pupil1 = GOval(12, 12, x=212,y=223)
    paint(pupil1, (255, 255, 255))
    window.add(pupil1)

    pupil2 = GOval(12, 12, x=282, y=223)
    paint(pupil2, (255, 255, 255))
    window.add(pupil2)

    mouth = GOval(170, 110, x=165, y=290)
    paint(mouth, (222,184,135))
    window.add(mouth)

    mouth1 = GOval(50, 50, x=225, y=300)
    paint(mouth1, (0, 0, 0))
    window.add(mouth1)

    mouth2 = GOval(20, 20, x=220, y=350)
    paint(mouth2, (0, 0, 0))
    window.add(mouth2)
def paint(obj, color):
    obj.filled = True
    obj.fill_color = color
if __name__ == '__main__':
    main()
