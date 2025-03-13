from intro import introduction_of_game
from main_menu import main_menu
from wikimedia_fetch import european_countries_and_capitals

playername, is_returning = introduction_of_game()
countries_capitals = european_countries_and_capitals()
while True: #
    playername, is_returning = main_menu(playername, countries_capitals, is_returning)