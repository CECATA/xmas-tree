import time
import os
import random
import argparse

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("--size", "-S", type=int, default=21)
    parse.add_argument("--time", "-T", type=int, default=5)
    args = parse.parse_args()
    SIZE = args.size
    TIMES = args.time

    tree = Tree(SIZE)
    time_ = 0
    while time_ < TIMES:
        tree.build()
        print()
        print(tree.color.CYAN + "FELIZ NAVIDAD CECATA")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        time_ += 1


class Tree(object):
    class color(object):
        BLACK = "\x1b[1;30m"
        RED = "\x1b[1;31m"
        GREEN = "\x1b[1;32m"
        YELLOW = "\x1b[1;33m"
        BLUE = "\x1b[1;34m"
        MAGENTA = "\x1b[1;35m"
        CYAN = "\x1b[1;36m"
        WHITE = "\x1b[1;37mm"
        BROWN = "\x1b[38;5;136m"

    def __init__(self, size=11):
        if size % 2 == 0:
            size += 1
        self._size = size

    def build(self):
        self.build_tree()
        self.build_root()

    def build_tree(self):
        blank_spaces = self._size // 2
        for i in range(0, self._size, 2):
            self.print_times(n=blank_spaces)
            for _ in range(i+1):
                color = self.select_color()
                print(color + "*", end="")
            self.print_times(n=blank_spaces, endline=True)
            blank_spaces -= 1

    def build_root(self): 
        char = self.color.BROWN + "ℿ"
        for _ in range(2):
            blank_spaces = (self._size - 2) // 2
            self.print_times(n=blank_spaces)
            self.print_times(n=2, char=char)
            self.print_times(n=blank_spaces, endline=True)
        for _ in range(2):
            blank_spaces = (self._size - 4) // 2
            self.print_times(n=blank_spaces)
            self.print_times(n=4, char=char)
            self.print_times(n=blank_spaces, endline=True)

    def print_times(self, n=1, char=" " ,endline=False):
        for _ in range(n):
            print(char, end="")
        if endline:
            print()

    def select_color(self) -> str:
        colors = {
            self.color.GREEN: 0.80,
            self.color.BLUE: 0.05,
            self.color.MAGENTA: 0.05,
            self.color.YELLOW: 0.05,
            self.color.RED: 0.05
        }
        color = random.choices(list(colors.keys()), list(colors.values()))
        return color[0]
        





if __name__ == "__main__":
    main()
