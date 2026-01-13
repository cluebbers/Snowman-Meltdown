import random
from colorama import Fore, Style

from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    # For now, display the initial game state.
    while mistakes < len(STAGES) - 1 and set(secret_word) != guessed_letters:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Prompt user for one guess (logic to be enhanced later)
        guess = input(Fore.YELLOW + "Guess a letter: " + Style.RESET_ALL).lower()
        if len(guess) != 1 or not guess.isalpha():
            print(
                Fore.RED
                + "Please enter a single alphabetical character."
                + Style.RESET_ALL
            )
            continue
        if guess in secret_word:
            guessed_letters.add(guess)
        else:
            mistakes += 1
    if set(secret_word) == guessed_letters:
        print(Fore.GREEN + "Congratulations! You saved the snowman!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Game Over! The word was:" + secret_word + Style.RESET_ALL)
