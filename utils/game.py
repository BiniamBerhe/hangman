from curses.ascii import isalpha
import random

from typing import List


class Hangman:
    """
    Class with 4 methods each with specific functions
    that allows as to play the Hangman game
    -And where all the lists are and other variables are intialized:
    - possible words: List[str]: where all the possible words are stored
    - words to find: List[str]: where the word to be guessed is intialized
    - well_guessed_latters: List[str]: where all correctly guessed latters are stored
    - wrong_guessed_latters: List[str]: wrongly guessed latters stored
    -lives: int: the number of time a player can play the game
    -self.turn_count: int: the number of time the player played
    -self.error_count: int: the wrongly guessed a player made

    """

    name = input("Please Provide Your name: ").upper()
    print(f"\n Hi {name}, Welcome let's play Hangman!", "\n")

    def __init__(self):
        self.possible_words: List[str] = ["becode", "learning", "mathematics", "session"]
        # This is an attribute for words to be guessed
        self.word_to_find: List[str] = [c for c in random.choice(self.possible_words)]
        self.correctly_guessed_latters: List[str] = list("_" * len(self.word_to_find))
        self.well_guessed_latters: List[str] = []
        self.wrong_guessed_latters: List[str] = []
        self.lives: int = 5
        self.turn_count: int = 0
        self.error_count: int = 0
        self.result: bool = False

    def play(self,word: List[str]) -> None:
        """Function that will accept all an input letter and perform the following:
        :param word: a str list of the word to be guessed
        :input latter: an input letter that will be compared and replace _
        :print statement: that displays every possible match in"""

        letter = input("Guess latter:  ")
        if len(letter) == 1 and letter.isalpha(): # This checks if input letter is one letter and letter only!
            if letter in self.wrong_guessed_latters:
                print("You have already guessed the latter", letter)
                self.error_count +=1
                self.turn_count +=1
            elif letter not in word:
                self.lives -=1
                self.error_count +=1
                self.turn_count +=1
                self.wrong_guessed_latters.append(letter)
            else:
                correct_letter = [i for i,x in enumerate(word) if x == letter] #This is un list comprehension that loops over enumerated latters
                for i in correct_letter:
                        self.correctly_guessed_latters[i] = letter
                if letter in self.well_guessed_latters:
                    print("You have already guessed the latter", letter)
                    self.error_count +=1
                    self.lives -=1
                else:
                    self.well_guessed_latters.append(letter)
                self.turn_count +=1
                print(self.correctly_guessed_latters, '\n')
                if "_" not in self.correctly_guessed_latters: # Here the if statement checks that all the letters are answered
                    self.result = True
        else:
            print("Not a valid guess.")
            self.error_count +=1

                
    def start_game(self) -> None:
        """Function that will be called  from main file:
        :First checks if a player has live value expected
        :If he doesn't have calls game over function
        :Second loops over and calles play function
        :Third checks if a player answered all the guess
        :If so calles well_played function"""

        while self.lives > 1: # Here live is checked for the game to continue
            print(f"Remaining Lives {self.lives}, correctly guessed letters {self.well_guessed_latters}, Wrong guessed letters {self.wrong_guessed_latters}, Errors made {self.error_count},Turns played {self.turn_count}")
            if self.result:
                return self._well_played()
            self.play(self.word_to_find)
        self._game_over()

    def _game_over(self) -> None:
        """This is a function that is called when lives is out of range
            and prints game over"""

        print(f"Game over....:(")

    def _well_played(self) -> None:
        """the is a function that is called when 
            all letters are answered correctly
            and prints the result of the player with his name"""

        final_word = ''.join(self.word_to_find)
        print(f'You have found the word: "{final_word}" in {self.turn_count} turns with {self.error_count} errors!')
        print(f"Good Job {self.name}")


# Here Player object is created from Hangman class
player = Hangman()
player.start_game()