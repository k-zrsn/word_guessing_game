### word guessing game 

import random
import time
import pandas as pd
import turn
import results
#import hints

def word_hint(word):
    """
    Docstring:
    A function that returns a hint 
    based on the word.
    """
    if word == "iribe":
        hint = "\n\nHint: Glass building"

    elif word == "eppley":
        hint = "\n\nHint: Rec center"

    elif word == "mckeldin" or word == "hornbake":
        hint = "\n\nHint: Good place to study"

    elif word == "tawes":
        hint = "\n\nHint: Writing center"

    elif word == "armory":
        hint = "\n\nHint: ROTC"

    elif word == "atlantic":
        hint = "\n\nHint: Shares name with an ocean"

    elif word == "stamp":
        hint = "\n\nHint: Terpzone"

    elif word == "shoemaker":
        hint = "\n\nHint: Shoes"

    elif word == "jimenez":
        hint = "\n\nHint: Professor of Spanish language and literature"


    return hint











### create necessary lists
player_list = []
correct_letters = []
incorrect_letters = []
word_bank = ["iribe", "eppley", "mckeldin", "hornbake", "tawes", "armory", "atlantic", "stamp", "shoemaker", "jimenez"]


### choose random word from word_bank
word = random.choice(word_bank).upper()


### welcome message
print("\n\nLet's play a word guessing game!")
print("\nThe theme of the words are UNIVERSITY OF MARYLAND BUILDINGS")


### get player count
getting_count = True
while getting_count:
    try:
        player_count = int(input("\n\nEnter the number of players: "))
        getting_count = False
    except ValueError:
        print("\nInvalid input, please enter a number.")


### create and print the scoreboard
scoreboard = {}
for i in range(1, player_count + 1):
    player_name = input(f"\nEnter name for Player {i}: ").upper()
    scoreboard[player_name] = 0
    player_list.append(player_name)
time.sleep(1)
print("\n\nThe scoreboard is set!\n")
time.sleep(1)
name = list(scoreboard.keys())
guess_number = list(scoreboard.values())

player_data = {"Player:" : name,
               "Guesses:" : guess_number}

player_dataframe = pd.DataFrame(data = player_data) 
print(player_dataframe.to_string(index = False))


### print rules for the game
if player_count > 1:
    time.sleep(1.5)
    print("\nRULES:\nEach player tries to guess a LETTER of the word\nand has 3 attempts to guess the WHOLE word.\nWhoever has the least number of guesses wins...")

    time.sleep(3)
    print("\nBut whoever guesses the word first wins!\n")
else:
    time.sleep(1.5)
    print("\nRULES:\nTry to guess each LETTER of the word\nYou have 3 attempts to guess the WHOLE word\n\nGood luck!\n")


### start game
time.sleep(2.5)
play_loop = True
while play_loop:

    ### establish number of mistakes remaining each player has
    incorrect_guess = {player : 3 for player in player_list}
    while incorrect_guess != -1:
        for player in player_list: 

            ### cycles through players
            take_turn = turn.next_turn(player)
            scoreboard[player] += take_turn

            print(f"\nCorrect letters guessed so far: {correct_letters}")
            print(f"\nIncorrect letters guessed so far: {incorrect_letters}")

            ### allows player to guess the word
            if correct_letters != []:
                time.sleep(1)
                guess_word = input("\n\nWould you like to guess the word? (y/n): ").lower()

                ### asks player for word
                if guess_word == "y":
                    word_guess = input("\n\nAlright then! What is the word? ").upper()

                    ### win game
                    if word_guess == word:
                        time.sleep(2)
                        print(f"\n\n\nCongratulations! {player} won!")
                        
                        ### print results
                        results.game_results(word, scoreboard)

                    ### wrong word, keep playing
                    else:
                        time.sleep(2)
                        print("\n\nSorry, that is not the word.")
                        incorrect_guess[player] -= 1
                        time.sleep(1)
                        print(f"\n{player} has {incorrect_guess[player]} mistake(s) left.\n\n \nIt's still {player}'s turn.")

                        ### lose game when player has no more mistakes remaining
                        if incorrect_guess[player] == 0: 
                            print(f"\n\nThat was {player}'s last guess. {player} lost!")

                            ### print results
                            results.game_results(word, scoreboard)
                            play_loop = False
                time.sleep(1)
            
            ### get player's letter guess
            guess = input("\nGuess a letter: ").upper()
            time.sleep(1)

            ### already guessed letter
            if guess in correct_letters or guess in incorrect_letters:
                print("\n\nThat letter has already been guessed!\n")
                time.sleep(2)
                continue

            ### add correct letter to list
            if guess in word:
                print("\n\nYou guessed a letter!")
                letter_count = word.count(guess)
                time.sleep(1)
                print(f"\nThe letter: {guess} appears in the word {letter_count} time(s).\n")
                correct_letters.append(guess)
                correct_letters.sort()
                time.sleep(2)

            ### add incorrect letter to list
            else:
                print("\n\nSorry, that letter is not in the word.\n")
                incorrect_letters.append(guess)
                incorrect_letters.sort()
                time.sleep(2)

            ### print scoreboard
            print("\nNumber of guesses:")
            for player, letter_guesses in scoreboard.items():
                print(f"{player}: {letter_guesses}")

            ### option to give up after 10 attempts
            if letter_guesses == 2:
                give_up = input("\n\nWould you like to give up?\nTo give up, type 'g'\nFor a hint, type 'h'\nTo continue playing, type 'c'\n\n").lower()

                if give_up == "g":
                    time.sleep(1)

                    ### print results
                    results.game_results(word, scoreboard)

                elif give_up == "h":
                    word_hint(word)

                else:
                    continue