from utils import game # Here game.py file is imported from the same file
""" This is a python module that is created to run the Hangman game"""
player = game.Hangman() # Here Hangman class is called  to create player method
while input("Enter (Y/N) To Play Again \n").upper() == "Y":
    """This is a while loop to let a player play again"""
    player.start_game()