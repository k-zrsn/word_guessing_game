### module for next_turn function


def next_turn(player_name):
    """
    Docstring:
    A function that keeps track the number of guesses
    and lets user know who's turn it is
    """
    letter_guesses = 0
    print(f"\n\nIt's {player_name}'s turn.")
    return letter_guesses + 1