import os
from typing import List, Dict
import attr
from pathlib import Path

from blessed import terminal


@attr.define
class Point:
    x: int
    y: int

    def __add__(self, other) -> "Point":
        return Point(x=self.x + other.x, y=self.y + other.y)


@attr.define
class Scene:
    position: Point
    pixel_grid: List[List[str]]

    def render(self):
        # determine the coordinates of the view window,
        top_left = Point(
            x=(
                self.position.x
                if self.width() > self.terminal_width()
                else 0
            ),
            y=(
                self.position.y
                if self.height() > self.terminal_height()
                else 0
            ),
        )

        bottom_right = top_left + Point(
            x=min(self.width(), self.terminal_width()),
            y=min(self.height(), self.terminal_height()),
        )

        # show the pixel grid
        text_rows = []
        for row in self.pixel_grid[top_left.y : bottom_right.y]:
            text_rows.append("".join(row[top_left.x : bottom_right.x]))

        return "\n".join(text_rows)

    def height(self) -> int:
        return len(self.pixel_grid)

    def width(self) -> int:
        return len(self.pixel_grid[0])

    def terminal_width(self):
        terminal_width, _ = os.get_terminal_size()
        return terminal_width

    def terminal_height(self):
        _, terminal_height = os.get_terminal_size()
        return terminal_height

    def scroll(self, *, x=0, y=0):
        # don't allow horizontal scroll if the scene is narrower than the terminal
        if self.width() <= self.terminal_width():
            x = 0

        # don't allow vertical scroll if the scene is shorter than the terminal
        if self.height() <= self.terminal_height():
            y = 0

        self.position = Point(
            x=min(
                # Don't allow scrolling past the left edge of the screen
                max(self.position.x + x, 0),
                # Don't allow scrolling past the right edge of the screen
                self.width() - self.terminal_width(),
            ),
            y=min(
                # Don't allow scrolling above the screen's top edge
                max(self.position.y + y, 0),
                # Don't allow scrolling below the screen's bottom edge
                self.height() - self.terminal_height(),
            ),
        )
