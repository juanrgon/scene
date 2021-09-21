from scene import Scene
from blessed import Terminal

scene = Scene.load("scenes/sparta.txt")

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
