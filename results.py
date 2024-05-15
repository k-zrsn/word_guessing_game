### module for game_results function


import time
import pandas as pd

def game_results(word, scoreboard):
    """
    Docstring:
    A function that prints the results of the game
    """
    print(f"\nThe word was: {word}\n")
    time.sleep(2)

    name = list(scoreboard.keys())
    guess_number = list(scoreboard.values())
    player_data = {"Players:" : name,
                "Guesses:" : guess_number}
    player_dataframe = pd.DataFrame(data = player_data) 
    print(player_dataframe.to_string(index = False))
    time.sleep(2)

    print("\n\nThanks for playing!\n\n\n")
    time.sleep(1)

    quit()