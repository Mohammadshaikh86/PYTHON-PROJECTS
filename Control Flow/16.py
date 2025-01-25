import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100.")

while True:
    # Prompt the user to guess
    guess = int(input("What's your guess? "))
    
    # Give hints
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number}!")
        break
