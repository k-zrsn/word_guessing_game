#daniel lane
### word guessing game 

import random
import time

player_list = []
correct_letters = []
incorrect_letters = []

def choose_word():
    word_bank = ["great", "trace", "watch", "train", "phone", "blank", "short", "stamp", "magic", "smart"]
    return random.choice(word_bank)


def create_scoreboard(player_count):
    scoreboard = {}
    for i in range(1, player_count + 1):
        player_name = input(f"\nEnter name for Player {i}: ").upper()
        scoreboard[player_name] = 0
        player_list.append(player_name)
    return scoreboard


def next_turn(player_name):
    letter_guesses = 0
    print(f"\n\nIt's {player_name}'s turn.")
    return letter_guesses + 1


def play():
    play_loop = True
    while play_loop:
        incorrect_guess = {player : 3 for player in player_list}
        while incorrect_guess != -1:
            for player in player_list: 
                if incorrect_guess[player] == 0: 
                    print(f"\n\nThat was your last guess. You lost!")
                    print(f"\nThe word was: {word}")
            
                    print("\nNumber of guesses:")
                    for player, letter_guesses in scoreboard.items():
                        print(f"{player}: {letter_guesses}")
                    play_loop = False
                    quit()

                take_turn = next_turn(player)
                scoreboard[player] += take_turn

                print(f"\nCorrect letters guessed so far: {correct_letters}")
                print(f"\nIncorrect letters guessed so far: {incorrect_letters}")
                
                if correct_letters != []:
                    time.sleep(1)
                    guess_word = input("\n\nWould you like to guess the word? (y/n): ").lower()

                    if guess_word == "y":
                        word_guess = input("\n\nAlright then! What is the word? ").upper()
                        if word_guess == word:
                            time.sleep(2)
                            print(f"\n\n\nCongratulations! {player} won!")
                            print(f"\nThe word was: {word}")
                            print("\nNumber of guesses:")
                            for player, letter_guesses in scoreboard.items():
                                print(f"{player}: {letter_guesses}")
                            quit()
                        else:
                            time.sleep(2)
                            print("\n\nSorry, that is not the word.")
                            incorrect_guess[player] -= 1
                            print(f"\n{player} has {incorrect_guess[player]} mistake(s) left\n\n")

                    time.sleep(1)
                
                guess = input("\n\nGuess a letter: ").upper()

                if guess in correct_letters or guess in incorrect_letters:
                    print("\n\nThat letter has already been guessed!\n\n")
                    time.sleep(2)
                    continue

                if guess in word:
                    print("\n\nYou guessed a letter!")
                    letter_count = word.count(guess)
                    time.sleep(1)
                    print(f"\nThe letter: {guess} appears in the word {letter_count} time(s).\n")
                    correct_letters.append(guess)
                    correct_letters.sort()
                    time.sleep(2)
                else:
                    print("\nSorry, that letter is not in the word.\n\n")
                    incorrect_letters.append(guess)
                    incorrect_letters.sort()
                    time.sleep(2)
                
                ### prints scoreboard
                print("\nNumber of guesses:")
                for player, letter_guesses in scoreboard.items():
                    print(f"{player}: {letter_guesses}")

                if letter_guesses == 10:
                    give_up = input("\n\nWould you like to give up? (y/n): ").lower()
                    if give_up == "y":
                        time.sleep(1)
                        print(f"\n\nThe word was: {word}")
                        print("\nNumber of guesses:")
                        for player, letter_guesses in scoreboard.items():
                            print(f"{player}: {letter_guesses}\n")
                        quit()


word = choose_word().upper()
player_count = int(input("\n\nEnter the number of players: "))
scoreboard = create_scoreboard(player_count)

time.sleep(1)
print("\n\nThe scoreboard is set!")

time.sleep(0.5)
### prints scoreboard
print("\nNumber of guesses:")
for player, letter_guesses in scoreboard.items():
    print(f"{player}: {letter_guesses}")

time.sleep(0.5)
print("\nWhoever has the least number of guesses wins...")

time.sleep(1)
print("\nBut whoever guesses the word first wins!\n")

time.sleep(2)
play()
