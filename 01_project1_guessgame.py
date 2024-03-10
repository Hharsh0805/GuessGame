import random
import os
import getpass
import sys

def play_guessing_game(num_players):
    num = random.randint(1, 100)
    attempts = [0] * num_players
    names = []

    for i in range(num_players):
        name = input(f"Enter player {i + 1}'s username: ")
        names.append(name)

    print("Welcome to the guessing game!")
    print("Try to guess the number between 1 and 100.")

    while True:
        for i in range(num_players):
            print(f"{names[i]}, enter your guess: ", end="", flush=True)
            player_guess = getpass.getpass("", stream=sys.stderr)
            if not player_guess.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            player_guess = int(player_guess)
            attempts[i] += 1

            if player_guess == num:
                print(f"Congratulations, {names[i]}! You guessed the number in {attempts[i]} attempts.")
                return

            elif player_guess < num:
                print("Too low! Try again.")

            else:
                print("Too high! Try again.")

if __name__ == "__main__":
    num_players = int(input("Enter the number of players: "))
    if num_players < 1:
        print("Invalid number of players. Please enter at least 1 player.")
    else:
        play_guessing_game(num_players)
