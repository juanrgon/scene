import curses
import os
from scene import Scene, Point
# from terminology import on_blue, on_green, in_blue, in_green
from itertools import cycle
from blessed import Terminal


blue_nums = {i: (str(i)) for i in range(10)}
green_nums = {i: (str(i)) for i in range(10)}

width, height = 150, 40

pixel_grid = []
pixel_grid.append(["*" for _ in range(width)])

for row_num in range(height - 2):
    colorer = blue_nums if row_num % 2 else green_nums
    nums = [str(colorer[i % 10]) for i in range(row_num, row_num + (width - 2))]
    nums = ["*"] + nums + ["*"]
    pixel_grid.append(nums)

pixel_grid.append(["*" for _ in range(width)])

scene = Scene(position=Point(0, 0), pixel_grid=pixel_grid)

term = Terminal()

print(term.home + term.clear + term.move_y(term.height // 2))
print(term.black_on_darkkhaki(term.center("press any key to continue.")))

inp = ""
with term.cbreak(), term.hidden_cursor():
    while inp != "q":
        print(term.home + term.clear + term.move_y(term.height // 2), end="")
        print(term.center(scene.render()), end="")

        key = term.inkey().code

        if key == term.KEY_RIGHT:
            scene.translate(x=1)
        elif key == term.KEY_LEFT:
            scene.translate(x=-1)
        elif key == term.KEY_UP:
            scene.translate(y=-1)
        elif key == term.KEY_DOWN:
            scene.translate(y=1)
