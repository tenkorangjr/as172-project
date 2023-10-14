"""
Author: Michael Tenkorang
Class: AS172
"""

from typing import List, Tuple
from turtle import RawTurtle, _Screen
from color_loader import colors
import random

class Star(RawTurtle):

    def __init__(self, screen: _Screen, radius: float) -> None:
        super().__init__(screen)
        self.penup()
        self.__color_index = 0
        self.stage_colors: List[Tuple[int]] = None
        self.load_colors()
        self.stage_color: Tuple[int] = None
        self.speed("fastest")

        self.factor = 1.02 # factor for star scaling

        self.window = screen

        self.ended = False

        self.radius: float = radius

        self.draw()

    def load_colors(self):
        self.stage_colors = colors

    def goto_main_position(self):
        self.hideturtle()
        self.goto((0, -1*self.radius))

    def draw(self):
        self.goto_main_position()
        self.stage_color: Tuple[int] = self.stage_colors[self.__color_index]
        if self.__color_index < 99:
            self.__color_index += 1
        self.fillcolor(self.stage_color)
        self.begin_fill()
        if self.__color_index == 99:
            self.screen.clear()
        self.circle(radius = self.radius)
        self.radius *= self.factor
        self.end_fill()

    

    def still_growing(self) -> bool:
        return True if self.__color_index < 98 else False # switch back to 99

    def has_cycle_ended(self) -> bool:
        return self.ended


class HighMassStar(Star):

    def __init__(self, window: _Screen) -> None:
        super().__init__(window, 50)

    def end_cycle(self):
        self.radius = 30
        self.fillcolor((128, 128, 128))
        self.begin_fill()
        self.circle(self.radius)
        self.end_fill()
        self.supernova()
        self.ended = True

    def supernova(self):
        height = self.window.window_height
        width = self.window.window_width

        for _ in range(140):
            self.goto(random.randint(-(width/2), width/2), random.randint(-(height/2), height/2))
            self.dot(5, random.choice(["white", "red", "yellow", "blue", "gray"]))


class LowMassStar(Star):

    def __init__(self, window: _Screen) -> None:
        super().__init__(window, 20)

    def end_cycle(self):
        self.radius = 10
        self.fillcolor((255, 255, 255))
        self.begin_fill()
        self.circle(self.radius)
        self.end_fill()
        self.ended = True
