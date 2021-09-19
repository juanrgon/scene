from pixel_grid import PixelGrid
import os

class Scene:
    def __init__(self, width, height):
        self.position = 0
        self._pixel_grid = [
            ['\x1b[44m \x1b[0m' for _ in range(width)] for _ in range(height)
       ]

    def render(self):
        terminal_width, terminal_height = os.get_terminal_size()
        # clear the terminal,
        os.system('clear')

        # show the pixel grid,
        string = ""
        for row in self._pixel_grid[:min(len(self._pixel_grid), terminal_height)]:
            for pixel in row[:min(len(row), terminal_width)]:
                string += pixel
            string += '\n'
        print(string)
        #
