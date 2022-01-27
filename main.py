from utils import game

player = game.Hangman()
while input("Enter (Y/N) To Play Again \n").upper() == "Y":
    player.start_game()