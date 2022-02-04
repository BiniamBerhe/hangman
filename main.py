""" This is a python module that is created to run the Hangman game"""
from utils import game 

# Here Hangman class is called  to create player object
player = game.Hangman() 

while input("Enter (Y/N) To Play Again \n").upper() == "Y":
    """This is a while loop to let a player play again"""
    player = game.Hangman()
    player.start_game()