import json
import random
import time
import gameoverboard
from googletrans import Translator

translator = Translator()

correct_count = 0
error_count = 0
asked_countries = []

def translate_to_english(text):
    try:
        translation = translator.translate(text, dest='en')
        return translation.text
    except Exception as e:
        print(f"Übersetzungsfehler: {e}")
        return text # Originaltext zurückgeben, falls ein Fehler auftritt

def question(countries_capitals, playername):
    global correct_count, error_count, asked_countries
    available_countries = list(countries_capitals.keys())

    if len(asked_countries) == len(available_countries):
        asked_countries.clear()

    while True:
        random_country = random.choice(available_countries)
        if random_country not in asked_countries:
            break

    correct_capital = countries_capitals[random_country]

    wrong_capitals = []
    available_capitals = list(countries_capitals.values())
    while len(wrong_capitals) < 3:
        random_capital = random.choice(available_capitals)
        if random_capital != correct_capital and random_capital not in wrong_capitals:
            wrong_capitals.append(random_capital)
    choices = wrong_capitals + [correct_capital]
    random.shuffle(choices)

    # Ländernamen und Stadtnamen übersetzen
    translated_country = translate_to_english(random_country)
    translated_choices = [translate_to_english(choice) for choice in choices]

    print(f"What is the capital of {translated_country}?")
    for i, choice in enumerate(translated_choices):
        print(f"{i + 1}. {choice}")

    while True: # Neue Schleife zur Validierung der Eingabe
        user_answer = input("Answer: ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            break # Gültige Eingabe, Schleife verlassen
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

    try:
        if translated_choices[int(user_answer) - 1] == translate_to_english(correct_capital):
            print("Correct!")
            correct_count += 1
            update_scoreboard(playername)
            time.sleep(1)
            asked_countries.append(random_country)
            question(countries_capitals,playername)
        else:
            print(f"Wrong! The capital of {translated_country} is {translate_to_english(correct_capital)}.")
            error_count += 1
            time.sleep(1)
            if error_count == 3:
                gameoverboard.game_over(playername, correct_count)
                return
            else:
                asked_countries.append(random_country)
                question(countries_capitals, playername)
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number from the list.")

def update_scoreboard(playername):
    try:
        with open("scoreboard.json", "r") as f:
            scoreboard = json.load(f)
    except FileNotFoundError:
        scoreboard = {}
    except json.JSONDecodeError:
        scoreboard = {}

    if playername in scoreboard:
        if correct_count > scoreboard[playername]:
            scoreboard[playername] = correct_count
            with open("scoreboard.json", "w") as f:
                json.dump(scoreboard, f, indent=4)