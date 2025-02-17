import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of tries
attempts = 0

print("Welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess it?")

while True:
    try:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        
        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too Low! Try again.")
        else:
            print("Too High! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")

# End of the game
print("Thanks for playing!")
