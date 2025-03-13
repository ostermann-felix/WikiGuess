import json

def introduction_of_game():
    print("WIKIGUESS")
    print("---------------------------------------------------")
    playername = get_playername()
    is_returning = check_playername_exists(playername)
    return playername, is_returning

def get_playername():
    playername = input("Playername: ")
    return playername

def check_playername_exists(playername):
    try:
        with open("scoreboard.json", "r") as f:
            scoreboard = json.load(f)
    except FileNotFoundError:
        scoreboard = {}
    except json.JSONDecodeError:
        scoreboard = {}

    if playername in scoreboard:
        confirmation = input(f"Have you played under the name: {playername}? (y/n)").lower()
        if confirmation == "y":
            print(f"Welcome back, {playername}!")
            return True
        elif confirmation == "n":
            new_playername = input("Please enter a different name: ")
            return check_playername_exists(new_playername)
        else:
            print("Please enter 'y' or 'n'.")
            return check_playername_exists(playername)
    else:
        scoreboard[playername] = 0
        with open("scoreboard.json", "w") as f:
            json.dump(scoreboard, f, indent=4)
        return False