import random

secret_number = random.randint(1, 15)
max_attempts = 3

print("Welcome to the Number Guessing Game!")
print("Guess a number from 1 to 15. You have 3 attempts.")

for attempt in range(1, max_attempts + 1):
    try:
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    if guess == secret_number:
        print(
            f"Correct! You guessed the number {secret_number} in {attempt} attempts.")
        break
    elif guess < secret_number:
        print("Hint: Too low! Try a higher number.")
    else:
        print("Hint: Too high! Try a lower number.")
else:
    print(f"Sorry, you ran out of attempts. The number was {secret_number}.")
