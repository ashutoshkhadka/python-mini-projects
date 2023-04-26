from art import logo
import random

MAGIC_NUMBER = random.randint(1, 100)
ATTEMPTS_HARD = 5
ATTEMPTS_EASY = 10


def set_attempts(difficulty_level):
    if difficulty_level == 'e':
        return ATTEMPTS_EASY
    else:
        return ATTEMPTS_HARD


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty_level = input("Choose a difficulty level: 'E'asy or 'H'ard: \n").lower()
    attempts_left = set_attempts(difficulty_level)
    while attempts_left > 0:
        print(f"You have {attempts_left} attempts left to guess the number")
        guess = int(input("Make a guess: "))

        if guess > MAGIC_NUMBER:
            print("too high")
            attempts_left -= 1
        elif guess < MAGIC_NUMBER:
            print("too low")
            attempts_left -= 1
        else:
            print("Wohooo..you win")
            return

        if attempts_left == 0:
            print("Sorry, you've run out of attempts")
        elif guess != MAGIC_NUMBER:
            print("Guess again")


play_game()
