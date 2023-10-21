"""
Author: Michael Tenkorang Ofori
Class: AS172
"""

import time
from star import Star, HighMassStar, LowMassStar
from screen import StarWindow
from tkinter import messagebox

def main():
    """
    The function to display the stars and small star undergoing its 
    lifecycle
    """

    window = StarWindow()

    messagebox.showinfo(title="Star Explosion Warning 💀", message="You're lightyears away from Earth! Beware of Supernovas and blackholes!!!💀")
    selected_type = window.textinput("Type of Star", "What type of star do you want to see (high/low): ")

    if selected_type == "high":
        star = HighMassStar(window)
        window.update()
    elif selected_type == "low":
        star = LowMassStar(window)
    else:
        messagebox.showerror("Ooops", "Invalid input entered")
        
    shrinking = False

    while not star.has_cycle_ended():
        if not star.still_growing() and not shrinking:
            star.factor = 0.6
            shrinking = True

        time.sleep(0.02)
        star.draw()
        if shrinking and star.radius < 20:
            star.end_cycle()
        window.update()

    window.mainloop()

if __name__ == "__main__":
    main()
