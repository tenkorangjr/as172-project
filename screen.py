"""
Author: Michael Tenkorang
Class: AS172
"""
from turtle import _Screen

class StarWindow(_Screen):

    def __init__(self) -> None:
        super().__init__()
        self.title("Stars Life Cycle")
        self.bgcolor("black")
        self.window_height = 500
        self.window_width = 500
        self.colormode(255)

    def clear(self):
        super().clear()
        self.bgcolor("black")
        self.colormode(255)