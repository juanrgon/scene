import os
from terminology import on_blue, on_green, in_blue, in_green
from itertools import cycle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other) -> "Point":
        return Point(self.x + other.x, self.y+ other.y)

    @classmethod
    def origin(cls):
        return cls(0, 0)


blue_nums = {i: in_blue(str(i)) for i in range(10)}
green_nums = {i: in_green(str(i)) for i in range(10)}


class Scene:
    def __init__(self, width, height):
        self.position = Point.origin()

        self._pixel_grid = []
        for row_num in range(height):
            colorer = blue_nums if row_num % 2 else green_nums
            nums = [str(colorer[i % 10]) for i in range(1, width + 1)]
            self._pixel_grid.append(nums)

    def render(self):
        terminal_width, terminal_height = os.get_terminal_size()
        # clear the terminal,
        os.system("clear")

        # show the pixel grid,
        string = ""
        y_start, y_end = (
            self.position.y if self.height() > terminal_height else Point.origin().y,
            self.position.y + min(self.height(), terminal_height),
        )
        x_start, x_end = (
            self.position.x if self.width() > terminal_width else Point.origin().x,
            self.position.x + min(self.width(), terminal_width),
        )

        text_rows = []
        for row in self._pixel_grid[y_start:y_end]:
            text_rows.append("".join(row[x_start:x_end]))
        print("\n".join(text_rows))

    def height(self) -> int:
        return len(self._pixel_grid)

    def width(self) -> int:
        return len(self._pixel_grid[0])

    def translate(self, *, x=0, y=0):
        self.position = self.position + Point(x, y)

