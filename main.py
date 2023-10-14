"""
Author: Michael Tenkorang Ofori
Class: AS172
"""

import random
from star import Star, HighMassStar, LowMassStar
from turtle import RawTurtle
from screen import StarWindow
from tkinter import messagebox

def main():
    """
    The function to display the stars and small star undergoing its 
    lifecycle
    """

    window = StarWindow()
    selected_type = window.textinput("Type of Star", "What type of star do you want to see (high/low): ")

    if selected_type == "high":
        star = HighMassStar(window)
        window.update()
    elif selected_type == "low":
        star = LowMassStar(window)
    else:
        messagebox.showerror("Ooops", "Invalid input entered")
        

    window.mainloop()

if __name__ == "__main__":
    main()
