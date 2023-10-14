"""
Author: Michael Tenkorang
Class: AS172
"""

from typing import List, Tuple
from turtle import RawTurtle, _Screen

class Star(RawTurtle):

    def __init__(self, screen: _Screen, radius: float) -> None:
        super().__init__(screen)
        self.stage_colors = [(0, 0, 255)]
        self.stage_color: Tuple[int] = self.stage_colors[0]

        self.radius: float = radius

        self.draw()

    def goto_main_position(self):
        self.goto((0, -1*self.radius))

    def draw(self):
        self.goto_main_position()
        self.fillcolor(self.stage_color)
        self.begin_fill()
        self.circle(radius = self.radius)
        self.end_fill()

    def still_growing(self) -> bool:
        pass

    def has_cycle_ended(self) -> bool:
        pass


class HighMassStar(Star):

    def __init__(self, window: _Screen) -> None:
        super().__init__(window, 50)



class LowMassStar(Star):

    def __init__(self, window: _Screen) -> None:
        super().__init__(window, 20)
