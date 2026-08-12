import random

words = ["python", "computer", "programming", "keyboard", "developer"]

secret_word = random.choice(words)

hidden_word = ["_"] * len(secret_word)

incorrect_guesses = 0
guessed_letters = []

print(" ".join(hidden_word))

while True:
    guess = input("Guess a letter: ").lower().strip()

    # Check that the user entered exactly one letter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # Check if the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    correct_guess = False

    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            hidden_word[i] = guess
            correct_guess = True

    if correct_guess == False:
        incorrect_guesses += 1
        print("Wrong guess!")

    print("Incorrect guesses:", incorrect_guesses)
    print("Guesses remaining:", 6 - incorrect_guesses)

    print(" ".join(hidden_word))

    # Check if the player has won
    if "_" not in hidden_word:
        print("Congratulations! You guessed the word!")
        break

    # Check if the player has lost
    if incorrect_guesses == 6:
        print("Game Over!")
        print("The word was:", secret_word)
        break