import random
import os
import time

def read_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return random.choice(lines).strip()  # Choose a random word from the file

def clear_screen():
     os.system('cls' if os.name == 'nt' else 'clear')

def hangman():
    # Clear the terminal before starting a new game
    clear_screen()

    # Choose a random word
    word = read_random_line('Dictionary.txt')

    # Initialize game state
    guessed_letters = set()
    all_guessed_letters = set()
    attempts = 6  # Number of attempts allowed
    correct_guesses = 0

    print("Welcome to Hangman!")
    print("Try to guess the word. You have", attempts, "attempts.")

    # Main game loop
    while attempts > 0 and correct_guesses < len(set(word)):
        # Display the current state of the word
        display_word = ''
        for letter in word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += '_ '
        print("Word:", display_word)
        
        # Prompt the player to guess a letter
        guess = input("Guess a letter: ").lower()
        if guess.isalpha():
            all_guessed_letters.add(guess)
        else: 
            print("Invalid input. Please enter a letter.")
            continue  # Skip the rest of the loop iteration if input is invalid

        # Check if the guessed letter is in the word
        if guess in word:
            print("Correct guess!")
            guessed_letters.add(guess)
            correct_guesses += 1
            print("\n\n")
            print("Attempts Left:", attempts)
            print("Guessed letters:", ', '.join(sorted(guessed_letters)))
            
        else:
            print("Incorrect guess!")
            attempts -= 1
            print("\n\n")
            print("Attempts left:", attempts)
            guessed_letters.add(guess)
            print("Guessed letters:", ', '.join(sorted(guessed_letters)))
            
    # Game outcome
    if correct_guesses == len(set(word)):
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you ran out of attempts. The word was:", word)

    input("Press Enter to clear the screen...")
    clear_screen()

    
# Call the hangman function to start the game
while True:
    hangman()
