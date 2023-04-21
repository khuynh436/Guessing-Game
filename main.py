import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Game loop
while True:
    # Get user's guess
    guess = int(input("Guess the secret number (between 1 and 100): "))
    attempts += 1

    # Compare the guess with the secret number
    if guess < secret_number:
        print("Higher!")
    elif guess > secret_number:
        print("Lower!")
    else:
        print("Congratulations! You guessed the secret number in", attempts, "attempts!")
        break

    # Check if the user has reached the maximum number of attempts
    if attempts == 5:
        print("Out of attempts! The secret number was", secret_number)
        break
