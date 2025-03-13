from question import question
from manual import manual
from scoreboard import show_scoreboard
from scoreboard import sort_scores
import time
import sys

def main_menu(playername, countries_capitals, is_returning):
    while True:
        if not is_returning:
            print(f"Welcome {playername}\n")
        print("1. Start Game")
        print("2. Exit Game\n")
        print("3. Game Manual")
        print("4. Scoreboard")
        user_input = input("Please select your option: ")

        match user_input:
            case "1":
                question(countries_capitals, playername)
            case "2":
                sys.exit()
            case "3":
                manual(playername)
            case "4":
                show_scoreboard(sort_scores())
            case "5":
                playername, is_returning = change_playername()
                return playername, is_returning
            case _:
                print("Invalid selection, please enter a number between 1 and 5.")
                time.sleep(1)

def change_playername():
    playername = input("Please enter your new playername: ")
    is_returning = False
    return playername, is_returning