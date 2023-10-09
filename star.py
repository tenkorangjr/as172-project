"""
Author: Michael Tenkorang
Class: AS172
"""

from typing import List, Tuple

class Star:

    def __init__(self, color: Tuple[int], position: Tuple[int], radius: float) -> None:
        self.color: Tuple[int] = color
        self.position: Tuple(float) = position

        self.radius: float = radius