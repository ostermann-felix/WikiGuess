import json

def show_scoreboard(sorted_scores):
    print("\n#SCOREBOARD")
    print("==========================================")

    places = ["Gold", "Silver", "Bronze", "Copper", "Iron", "Wood"]

    sorted_items = list(sorted_scores.items())

    for i, place in enumerate(places):
        if i < len(sorted_items):
            player, score = sorted_items[i]
            print(f"{place}: {player} - {score}")
        else:
            print(f"{place}: ")

    input("\n# Main menu: Press Enter\n")

def sort_scores():
    try:
        with open("scoreboard.json", "r") as f:
            scoreboard_data = json.load(f)
    except FileNotFoundError:
        print("Error: File 'scoreboard.json' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in 'scoreboard.json'.")
        return None

    sorted_scores = dict(sorted(scoreboard_data.items(), key=lambda item: item[1], reverse=True))
    return sorted_scores