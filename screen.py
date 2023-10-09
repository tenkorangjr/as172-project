"""
Author: Michael Tenkorang
Class: AS172
"""
from tkinter import Canvas
import turtle

class StarWindow(turtle._Screen):

    def __init__(self) -> None:
        super().__init__()
        self.title("Stars Life Cycle")
        self.bgcolor("black")
        self.window_height = 500
        self.window_width = 500