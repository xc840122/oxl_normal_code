"""
    welcome.py
    author: Peter
    description: Welcome screen
"""
import time


def welcome_screen():
    print("\n")
    print("====================================")
    print("  WELCOME TO THE HIGHER OR LOWER GAME")
    print("====================================")
    print("      _______    _______    _______ ")
    print("     |       |  |       |  |       |")
    print("     | higher|  |   ?   |  | lower |")
    print("     |_______|  |_______|  |_______|")
    print(" ")
    print("Guess which one has more followers!")
    print("Try to get more scores")
    print("Try to guess as many correct as possible!")
    print(" ")

    # Give the user some time to read the welcome screen
    time.sleep(2)
    input("Press Enter to start the game...")
    print("\nStarting the game...\n")
