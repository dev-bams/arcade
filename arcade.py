"""
blah blah
"""
import argparse
import guess_number
import rps


def display_menu(name):
    """
    blah blah
    """
    print(f"{name}, welcome to the Arcade!")
    print("Please choose a game: ")
    print("1. Rock Paper Scissors")
    print("2. Guess the number")


def get_player_choice():
    """
    blah blah
    """
    player_choice = input("Choice: ")
    return int(player_choice)


def start_game(name, player_choice):
    """
    blah blah
    """
    if player_choice == 1:
        rps.play()
    else:
        guess_number.play_game(name)


def start(name):
    """
    blah blah
    """
    display_menu(name)
    player_choice = get_player_choice()
    start_game(name, player_choice)


parser = argparse.ArgumentParser(
    description="Play fun games at the arcade"
)
parser.add_argument(
    "-n", "--name", metavar="name", required=True, help="Enter your name"
)
args = parser.parse_args()

start(args.name)
