"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
By: Christin Gines
--------------------------------
"""

import random
import sys

def start_game():
    answer = random.randint(1,20)
    number_of_attempts = 1
    print("Welcome to the guessing game")
    try:
        guess = int(input("Guess a number between 1 and 20: "))
    except ValueError:
        print("Tsk tsk, that's not a real number... ")
    else:
        while guess != answer:
            number_of_attempts += 1
            if guess > answer:
                guess = int(input("Too high. Guess again.: "))
            elif guess < answer:
                guess = int(input("Too low. Guess again.: "))
        print("YOU DID IT!! It only took you {} tries".format(number_of_attempts))
        
        while True:
            play_again = input("Would you like to play again? (y/n): ")
            if play_again.lower()=="y":
                start_game()
            elif play_again.lower()=="n":
                sys.exit("Till next time, Goodbye")
            else:
                print("Type y or n, pretty please.")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
