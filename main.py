"""
Author: Michael Tenkorang Ofori
Class: AS172
"""

import random
from star import Star
from screen import StarWindow

def main():
    """
    The function to display the stars and small star undergoing its 
    lifecycle
    """

    window = StarWindow()

    window.mainloop()


    # stars = [Star()] # Creating a list of random stars on the screen with varying colors
    # for _ in range(30):
    #     pass


if __name__ == "__main__":
    main()
