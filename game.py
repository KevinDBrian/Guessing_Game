# Guessing Game

# import 
import random
import time

# define wait
def wait(i):
    time.sleep(i)

# player intro to game
print("\nHello!")
wait(1)

# player name
player_name = input("\nWhat's your name?: ")

# instructions
print(f"\nWelcome to the Guessing Game, {player_name}!")
wait(2.5)
print("\nIn this game I will pick a number between 1 and 10.")
wait(3.5)
print("\nYou need to figure out which number I'm thinking of.")
wait(3.5)
print("\nHowever, you only get 3 attempts to guess.")
wait(2.75)
print("\nDon't worry though!")
wait(1.75)
print("\nIf you guess wrong, I'll let you know if your guess was too high or too low.")
wait(3.75)
print("\nLet's begin!")
wait(2.75)

# while True restarts the game without the going through the intro again
while True:

    # computer picks a number
    number = random.randint(1, 10)
    print("\nAlright... I have a number.")
    wait(2)
    print(f"\nMake your guess, {player_name}!")

    # attempt counter within current loop
    attempts = 0

    # guessing conditions while loop
    while attempts < 3:
        player_guess = int(input("\nWhat's your guess?: "))
        attempts += 1
        if player_guess > number:
            print(f"\nNope, {player_guess} is too high. Guess Again!")
        if player_guess < number:
            print(f"\nNope, {player_guess} is too low. Guess Again!")
        if player_guess == number:
            break
    if player_guess == number:
            print(f"\nCorrect, the number was {number}! You guessed the number in {attempts} attempt(s)!")
    else:
        print(f"\nSorry, you were not able to guess the number. The number I was thinking of was {number}.")
    
    # player restart/end game
    start = input(f"\nDo you want to play again, {player_name}? (y/n): ")
    if start != "y":
        print("\nThanks for playing!")
        break
