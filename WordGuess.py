import random

def word_guessing_game():
    # Dictionary of words and their explanations
    words_and_explanations = {
        "python": "A high-level programming language known for its readability and simplicity.",
        "giraffe": "A long-necked mammal native to Africa, known for its distinctive spotted coat.",
        "oxygen": "A chemical element essential for the survival of most living organisms.",
        "guitar": "A musical instrument with strings, typically played by strumming or plucking.",
        "moon": "Earth's natural satellite that orbits the planet.",
        # Add more words and explanations as needed
    }

    # Select a random word and its explanation
    word = random.choice(list(words_and_explanations.keys()))
    explanation = words_and_explanations[word]

    print("Welcome to the Word Guessing Game!")
    print("Here's a short explanation of the word:")
    print(explanation)

    attempts = 0

    while True:
        # Get the player's guess
        guess = input("Enter your guess: ").lower()
        attempts += 1

        # Check if the guess is correct
        if guess == word:
            print(f"Congratulations! You guessed the correct word '{word}' in {attempts} attempts.")
            break
        else:
            print("Incorrect guess. Try again.")

if __name__ == "__main__":
    word_guessing_game()
