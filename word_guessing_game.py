#daniel lane
### word guessing game 

import random
import time


### function that picks a random word from the word bank
def choose_word():
    word_bank = ["great", "trace", "watch", "train", "phone", "blank", "short", "stamp", "magic", "smart", "floccinaucinihilipilification"]
    return random.choice(word_bank)


def create_player(name):
    return {'Player': name, 'Score': 0}


### game loop
def game():
    word = choose_word().upper()
    correct_letters = []
    incorrect_letters = []
    mistakes = 3
    
    while mistakes > 0:
        print(f"\n\nCorrect letters guessed so far: {correct_letters}")
        print(f"\nIncorrect letters guessed so far: {incorrect_letters}")
        print(f"\nYou have {mistakes} mistakes remaining.")

        guess = input("\n\nGuess a letter: ").upper()
        
        if guess in word:
            print("\nYou guessed a letter!\n\n")
            #for guess in word:
            letter_count = word.count(guess)
            print(f"That letter: {guess} appears in the word {letter_count} time(s).")
            correct_letters.append(guess)
            correct_letters.sort()
            guess_word = input("\nWould you like to guess the word? (y/n): ")

            if guess_word == "y":
                word_guess = input("\nAlright then! What is the word? ")
                if word_guess == word:
                    print("\n\nCongratulations! You won!")
                    print(f"\nThe word was: {word}\n\n")
                else:
                    print("\n\nSorry, that is not the word.")

            time.sleep(2)
        else:
            print("\nSorry, that letter is not in the word.\n\n")
            incorrect_letters.append(guess)
            incorrect_letters.sort()
            mistakes -= 1
            time.sleep(2)

    print(f"\nYou lose. The word was: {word}\n\n")





print("\n\nLet's play a game of word guessing!")
print("\nThe program will choose a word from a list containing 10 words.")
print("\nHint: All words are 5 letters long!")

player_count = int(input("\n\nHow many players are playing? "))
players = []

for i in range(player_count):
    player_name = input("\n\nEnter player name: ")
    player_name = player_name.upper()
    players.append(create_player(player_name))

time.sleep(1)
print("\n\nThe scoreboard is set!")
print(players)
time.sleep(3)
print("\n\nGet ready to play!\n")
time.sleep(2)


game()
replay = input("\nWould you like to play again? (y/n):")
if replay == "y":
    time.sleep(1)
    game()
    replay = input("\nWould you like to play again? (y/n): ")
    if replay == "y":
        time.sleep(1)
        game()
        print("\n\nThanks for playing!\n")
    else:
        print("\n\nThanks for playing!\n")
else:
    print("\n\nThanks for playing!\n")

