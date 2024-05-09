### module for game_results function


import time

def game_results(word, scoreboard):
    """
    Docstring:
    A function that prints the results of the game
    """
    print(f"\nThe word was: {word}")
    time.sleep(1)
    ### print scoreboard
    print("\nNumber of guesses:")
    for player, letter_guesses in scoreboard.items():
        print(f"{player}: {letter_guesses}")
    print("\n\nThanks for playing!\n\n\n")
    quit()