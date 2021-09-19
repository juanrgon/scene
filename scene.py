import os
from typing import List


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other) -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def origin(cls):
        return cls(0, 0)


class Scene:
    def __init__(self, position: Point, pixel_grid: List[List[str]]):
        self.position = position
        self._pixel_grid = pixel_grid

    @classmethod
    def empty(cls, width: int, height: int) -> "Scene":
        return Scene(
            position=Point.origin(),
            pixel_grid=[[" " for _ in range(width)] for _ in range(height)],
        )

    def render(self):
        terminal_width, terminal_height = os.get_terminal_size()
        # clear the terminal,
        os.system("clear")

        # determine the coordinates of the view window,
        top_left = Point(
            self.position.x if self.width() > terminal_width else Point.origin().x,
            self.position.y if self.height() > terminal_height else Point.origin().y,
        )

        bottom_right = top_left + Point(
            min(self.width(), terminal_width),
            min(self.height(), terminal_height),
        )

        # show the pixel grid
        text_rows = []
        for row in self._pixel_grid[top_left.y : bottom_right.y]:
            text_rows.append("".join(row[top_left.x : bottom_right.x]))
        print("\n".join(text_rows))

    def height(self) -> int:
        return len(self._pixel_grid)

    def width(self) -> int:
        return len(self._pixel_grid[0])

    def translate(self, *, x=0, y=0):
        self.position = self.position + Point(x, y)
