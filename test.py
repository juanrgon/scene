import os
from scene import Scene, Point
from terminology import on_blue, on_green, in_blue, in_green
from itertools import cycle


blue_nums = {i: in_blue(str(i)) for i in range(10)}
green_nums = {i: in_green(str(i)) for i in range(10)}

width, height = 20, 40

pixel_grid = []
for row_num in range(height):
    colorer = blue_nums if row_num % 2 else green_nums
    nums = [str(colorer[i % 10]) for i in range(1, width + 1)]
    pixel_grid.append(nums)

s = Scene(position=Point(0, 0), pixel_grid=pixel_grid)


s.translate(x=5)

s.render()
