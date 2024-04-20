#daniel lane
### word guessing game 

import random
import time

players = []
correct_letters = []
incorrect_letters = []
mistakes = 3

def choose_word():
    word_bank = ["great", "trace", "watch", "train", "phone", "blank", "short", "stamp", "magic", "smart", "floccinaucinihilipilification"]
    return random.choice(word_bank)


def create_scoreboard(player_count):
    scoreboard = {}
    for i in range(1, player_count + 1):
        player_name = input(f"\nEnter name for Player {i}: ").upper()
        scoreboard[player_name] = 0
        players.append(player_name)
    return scoreboard


def create_mistake_board(player_count):
    mistake_board = {}
    for i in range(1, player_count + 1):
        player_name = input(f"\nEnter name for Player {i}: ").upper()
        mistake_board[player_name] = 0
        players.append(player_name)
    return mistake_board


def next_turn(player_name):
    attempts = 0
    print(f"\n\nIt's {player_name}'s turn.")
    return attempts + 1


def make_mistake(player_name):

    print(f"{player_name} has {mistakes} mistakes remaining.")
    return mistakes - 1


def play():
    #mistakes = 3
    play_loop = True
    while play_loop:
        for player in players:
            take_turn = next_turn(player)
            scoreboard[player] += take_turn


            print(f"\n\nCorrect letters guessed so far: {correct_letters}")
            print(f"\nIncorrect letters guessed so far: {incorrect_letters}")
            guess = input("\n\nGuess a letter: ").upper()

            if guess in word:
                print("\nYou guessed a letter!\n\n")
                #for guess in word:
                letter_count = word.count(guess)
                print(f"That letter: {guess} appears in the word {letter_count} time(s).")
                correct_letters.append(guess)
                correct_letters.sort()

                guess_word = input("\nWould you like to guess the word? (y/n): ").lower()

                if guess_word == "y":
                    word_guess = input("\nAlright then! What is the word? ").upper()
                    if word_guess == word:
                        print(f"\n\nCongratulations! {player} won!")
                        print(f"\nThe word was: {word}\n\n")
                        print("\nAttempts:")
                        for player, attempts in scoreboard.items():
                            print(f"{player}: {attempts}")
                        play_loop = False
                        break
                        
                    else:
                        print("\n\nSorry, that is not the word.")

                time.sleep(2)
            else:
                print("\nSorry, that letter is not in the word.\n\n")
                incorrect_letters.append(guess)
                incorrect_letters.sort()
                mistake_made = make_mistake(player)
                #mistake_board[player] += mistake_made

                time.sleep(2)


            ### prints scoreboard
            print("\nAttempts:")
            for player, attempts in scoreboard.items():
                print(f"{player}: {attempts}")



word = choose_word().upper()
player_count = int(input("\n\nEnter the number of players: "))

'''
for i in range(1, player_count + 1):
    player_name = input(f"\nEnter name for Player {i}: ").upper()

    scoreboard = create_scoreboard(player_count)
mistake_board = create_mistake_board(player_count)
'''
scoreboard = create_scoreboard(player_count)



time.sleep(1)
print("\n\nThe scoreboard is set!")
time.sleep(0.5)
### prints scoreboard
print("\nAttempts:")
for player, attempts in scoreboard.items():
    print(f"{player}: {attempts}")
time.sleep(0.5)
print("\nWhoever has the least attempts wins...")
time.sleep(1)
print("\nBut whoever guesses the word first wins!")
time.sleep(2)

play()

