"""
Author: Michael Tenkorang
Class: AS172
"""

from typing import List, Tuple
from turtle import Turtle

class Star(Turtle):

    def __init__(self, color: Tuple[int], position: Tuple[int], radius: float) -> None:
        super().__init__()
        self.stage_colors = []
        self.stage_color: Tuple[int] = color
        self.position: Tuple[float] = position

        self.radius: float = radius

    def goto_main_position(self):
        self.goto((0, -1*self.radius))

    def draw(self):
        self.goto_main_position()
        self.begin_fill(self.stage_color)
        self.circle(radius = self.radius)
        self.end_fill()

    def still_growing(self) -> bool:
        pass


class HighMassStar(Star):

    def __init__(self, color: Tuple[int], position: Tuple[int], radius: float) -> None:
        super().__init__(color, position, radius)

    def draw(self):
        pass


class LowMassStar(Star):

    def __init__(self, color: Tuple[int], position: Tuple[int], radius: float) -> None:
        super().__init__(color, position, radius)
        self.radius_limit: int = 100