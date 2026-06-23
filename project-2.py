import random

secret_number = random.randint(1, 100)
guess = 0
max_attempts = 10
attempts = 0

print("Welcome to the Number Guessing Game!")
print(
    f" You have {max_attempts} attempts to guess the secret number between 1 and 100.")

while guess != secret_number and attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > secret_number:
        print("Too high!")

    elif guess < secret_number:
        print("Too low")

    else:
        print(f"Congratulations! You got it in {attempts} attempts.")

if guess != secret_number:
    print("Game Over")
    print(f"The secret number was {secret_number}.")
