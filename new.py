# Testing Linting

import random


def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please enter a number within the range of 1 to 100.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You guessed {secret_number} "
                    f"in {attempts} attempts."
                )
                break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    number_guessing_game()
