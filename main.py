# Python Day - 7 -- hangman
# 11/03/2023
# Loops, conditions, built-in methods, input validation, sets, lists..
# ------------------------------------------

import random
from replit import clear
from art import logo, stages
from words import word_list

print(logo + '\n')

# Randomly choosing a word from the word list
chosen_word = random.choice(word_list)

# For debugging
print(f"Answer is : {chosen_word}")

# Generating blanks
display = []

for _ in chosen_word:
    display.append('_')

# Setting the number of lives
lives = 6

# A list to keep track of the guesses
guesses = set()

print(display)

word_len = len(chosen_word)

# Condition for playing again
is_finished = False
while not is_finished:

    # Condition for ending the game
    end_game = False
    while not end_game:

        # Asking the user for an input
        guess_letter = input("\nGuess a letter: ").lower()

        while guess_letter.isspace() or guess_letter == '':
            print('Please type a letter!')
            guess_letter = input("\nGuess a letter: ").lower()

        # Clearing the screen
        clear()
        print(logo + '\n')

        #checking if the use has already guessed the letter
        if guess_letter in guesses:
            print(
                f"\nYou have already guessed '{guess_letter}', no lives lost\nGuess again!\n"
            )
            # if lives < 6:
            #     print(f"Remaing lives: {lives}\n")
            #     print(stages[lives])

        # Checking if the user has guessed the wrong letter
        elif guess_letter not in chosen_word and guess_letter not in guesses:
            lives -= 1
            print(
                f"\nYou guessed '{guess_letter}' not in the word, you lose a life\nRemaining lives: {lives}"
            )
            print(stages[lives])

        # Checking the user input..
        for position in range(word_len):
            # getting the position of the letter in the chosen_word
            letter = chosen_word[position]
            if letter == guess_letter:
                display[position] = letter

        # adding the guess to the guesses list
        guesses.add(guess_letter)

        # Displaying what the use has guessed so far
        print(display)

        # CHecknig whether or not the game should end (win or lose)
        user_word = ''.join(display)  # Another approch
        if user_word == chosen_word:  # if '_' not in display:
            end_game = True  #   end_game = True
            clear()
            print(logo + '\n')
            print('\nYou won!\n')  #   print("You won!")
            print(f"The word is: '{chosen_word}'")

        elif lives == 0:
            end_game = True
            clear()
            print(logo + '\n')
            print('\nYou are out of lives, You lose!\n')
            print(f"The word is: '{chosen_word}'")
            print(stages[lives])

    play_again = input("\nWould like to play again? Type 'Y' or 'N'\n").lower()

    if play_again == 'y':
        end_game = False
        lives = 6
        guesses.clear()
        clear()
        print(logo + '\n')

    elif play_again == 'n':
        is_finished = True
        print('Goodbye!')