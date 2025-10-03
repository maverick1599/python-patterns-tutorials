import random

# Number Guessing Game with Limited Attempts

number_to_guess = random.randint(1, 100)
attempts_left = 10

print("Welcome to the Number Guessing Game!")
print(f"You have {attempts_left} attempts to guess the number between 1 and 100.")

while attempts_left > 0:
    guess = int(input(f"Guess the number (Attempt {11 - attempts_left}/10): "))
    
    if guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Correct! You've guessed the number!")
        break
    
    attempts_left -= 1

if attempts_left == 0:
    print(f"Sorry, you're out of attempts! The correct number was {number_to_guess}.")
