"""
blah blah
"""
import argparse
from random import randint


def generate_computer_guess():
    """
    blah blah
    """
    computer_guess = randint(1, 3)
    return computer_guess


def get_player_guess(name):
    """
    blah blah
    """
    player_guess = input(
        f"{name} guess which number I'm thinking of... 1, 2, or 3\n")
    return int(player_guess)


def compare_guesses(name, computer_guess, player_guess):
    """
    blah blah
    """
    print(f"{name}, you chose {player_guess}, I was thinking of the number {computer_guess}")
    return "win" if computer_guess == player_guess else "lose"


def calculate_scores(game_count, result, computer_score, player_score):
    """
    blah blah
    """
    if result == "win":
        player_score += 1
    else:
        computer_score += 1
    winning_percentage = (player_score/game_count) * 100
    return player_score, computer_score, winning_percentage


def display_score(name, result, computer_score, player_score, winning_percentage):
    """
    blah blah
    """
    print(f"{name}, you {result}!")
    print(f"computer's score: {computer_score}")
    print(f"{name}'s score: {player_score}")
    print(f"your winning percentage: {winning_percentage:.2f}%")


def play_game(name):
    """
    blah blah
    """
    game_count = 1
    computer_score = 0
    player_score = 0
    while True:
        computer_guess = generate_computer_guess()
        player_guess = get_player_guess(name)
        result = compare_guesses(name, computer_guess, player_guess)
        player_score, computer_score, winning_percentage = calculate_scores(
            game_count, result, computer_score, player_score)
        display_score(name, result, computer_score,
                      player_score, winning_percentage)
        game_count += 1
        play_again = input("Game on? (Yes(Y), No(N)): ").lower()
        print("".center(60, "="))
        if play_again not in ["yes", "y"]:
            print("Thank you for playing!")
            print(f"Bye {name}!")
            break


# parser = argparse.ArgumentParser(
#     description="Play a fun game of guess the number")

# parser.add_argument(
#     "-n", "--name", metavar="name", required=True, help="Enter your name"
# )

# args = parser.parse_args()

# if __name__ == "__main__":
#     play_game(name)
