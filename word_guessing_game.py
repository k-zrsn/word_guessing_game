#daniel lane
### word guessing game 

import random
import time

print("\n\nLet's play a game of word guessing!")


### a word bank containing 10 different words
word_bank = ["great", "trace", "watch", "train", "phone", "blank", "short", "stamp", "magic", "smart"]


### pick a random word from the word bank
chosen_word = random.choice(word_bank)
print("\nThe program will choose a word from a list containing 10 words.")
print("\nHint: All words are 5 letters long!")


### get player count
player_count = int(input("\nHow many players are playing? "))

guessed_letters = [] #sort in alphabetical order?

print("\n\nGet ready to play!")
time.sleep(3)

turns = 0
turns += 1
print(f"\n\nTurn {turns} of 3 for Player 1")
print(f"\nLetters guessed so far: {guessed_letters}")

this_guess = input("\nGuess a letter: ")

if this_guess in chosen_word:
    print("\nYou guessed a letter!")
else:
    print("\nSorry, that letter is not in the word.")

guessed_letters.append(this_guess)

guess_word = input("\nWould you like to guess the word? (y/n): ")

if guess_word == "y":
    word = input("\nAlright then! What is the word? ")
    if word == chosen_word:
        print("\n\nCongratulations! You won!")
        print(f"\nThe word was: {chosen_word}\n\n")
    else:
        print("\n\nSorry, that is not the word.")

turns += 1
print(f"\n\nTurn {turns} of 3 for Player 2")











