#daniel lane
### word guessing game 

import random
import time

######


############ MAKE LETTER REPEAT CHECK AND WORK ON MISTAKE COUNTER ###########


####

players = []
correct_letters = []
incorrect_letters = []

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


def next_turn(player_name):
    attempts = 0
    print(f"\nIt's {player_name}'s turn.")
    return attempts + 1


def play():
    play_loop = True
    while play_loop:
        mistakes = {player : 3 for player in players}
        print (mistakes)
        while mistakes != -1:
            for player in players: 
                if mistakes[player] == 0: 
                    print(f"\n\nThat was your last guess. You lost!")
                    print(f"\nThe word was: {word}")
                
                    print("\nAttempts:")
                    for player, attempts in scoreboard.items():
                        print(f"{player}: {attempts}")
                    play_loop = False
                    quit()

                take_turn = next_turn(player)
                scoreboard[player] += take_turn

                print(f"\nCorrect letters guessed so far: {correct_letters}")
                print(f"\nIncorrect letters guessed so far: {incorrect_letters}")
                
                guess = input("\n\nGuess a letter: ").upper()

                if guess in correct_letters or guess in incorrect_letters:
                    print("\n\nYou already guessed that letter!")
                    time.sleep(2)
                    continue

                if guess in word:
                    print("\n\nYou guessed a letter!")
                    #for guess in word:
                    letter_count = word.count(guess)
                    print(f"\nThe letter: {guess} appears in the word {letter_count} time(s).")
                    correct_letters.append(guess)
                    correct_letters.sort()

                    guess_word = input("\n\nWould you like to guess the word? (y/n): ").lower()

                    if guess_word == "y":
                        word_guess = input("\n\nAlright then! What is the word? ").upper()
                        if word_guess == word:
                            time.sleep(2)
                            print(f"\n\n\nCongratulations! {player} won!")
                            print(f"\nThe word was: {word}")
                            print("\nAttempts:")
                            for player, attempts in scoreboard.items():
                                print(f"{player}: {attempts}")
                            quit()
                            
                        else:
                            time.sleep(2)
                            print("\n\nSorry, that is not the word.")
                            mistakes[player] -= 1
                            print(f"\n{player} has {mistakes[player]} mistake(s) left\n\n")

                    time.sleep(2)
                else:
                    print("\nSorry, that letter is not in the word.\n\n")
                    incorrect_letters.append(guess)
                    incorrect_letters.sort()


                    time.sleep(2)
                


                ### prints scoreboard
                print("\nAttempts:")
                for player, attempts in scoreboard.items():
                    print(f"{player}: {attempts}")


word = choose_word().upper()
player_count = int(input("\n\nEnter the number of players: "))
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
print("\nBut whoever guesses the word first wins!\n")

time.sleep(2)
play()
