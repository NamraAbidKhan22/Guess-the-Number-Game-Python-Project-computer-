import random  # Import the random module to generate random numbers
import sys     # Import the sys module to allow exiting the game

def guess_the_number():
    # Welcome message and instructions for the player
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0  # Initialize the number of attempts made by the player

    while True:  # Start an infinite loop to allow multiple guesses
        try:
            # Get user input and convert it to an integer
            guess = int(input("Enter your guess (or type 'exit' to quit): "))
            attempts += 1  # Increment the attempt counter

            # Check the player's guess against the number to guess
            if guess < number_to_guess:
                print("Too low! Try again.")  # Provide feedback if the guess is too low
            elif guess > number_to_guess:
                print("Too high! Try again.")  # Provide feedback if the guess is too high
            else:
                # If the guess is correct, congratulate the player and display attempts
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                break  # Exit the loop since the game is over
        except ValueError:
            # Handle the case where the input is not a valid integer
            if input("Type 'exit' to quit or press Enter to continue: ").lower() == 'exit':
                print("Thanks for playing! Goodbye!")  # Thank the player and exit
                sys.exit()  # Exit the program
            else:
                print("Please enter a valid number.")  # Prompt for valid input

# Start the game
if __name__ == "__main__":
    guess_the_number()  # Call the function to start the game