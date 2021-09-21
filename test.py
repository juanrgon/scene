import curses
import os
from scene import Scene, Point
from itertools import cycle
from blessed import Terminal

width, height = 150, 40

pixel_grid = []
pixel_grid.append(["*" for _ in range(width)])

for row_num in range(height - 2):
    nums = [str(i % 10) for i in range(row_num, row_num + (width - 2))]
    nums = ["*"] + nums + ["*"]
    pixel_grid.append(nums)

pixel_grid.append(["*" for _ in range(width)])

scene = Scene(position=Point(0, 0), pixel_grid=pixel_grid)

term = Terminal()

key = ""
with term.cbreak(), term.hidden_cursor():
    while key != "q":
        print(term.home + term.clear + term.move_y(term.height // 2), end="")
        print(term.center(scene.render()), end="")

        key = term.inkey().code

        if key == term.KEY_RIGHT:
            scene.scroll(x=1)
        elif key == term.KEY_LEFT:
            scene.scroll(x=-1)
        elif key == term.KEY_UP:
            scene.scroll(y=-1)
        elif key == term.KEY_DOWN:
            scene.scroll(y=1)
