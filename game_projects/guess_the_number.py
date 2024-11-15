# Guess the Number Game (1-20) - 5 Strikes You're Out!

# import modules
import random
import time 
# Random number generator
generated_num = random.randint(1, 20)

# Game instructions in time increments
print("Welcome to Guess the Number!")
time.sleep(1.5)
print("I'm thinking of a number between 1 and 20.")
time.sleep(1.5)
print("5 Strikes and You're Out! Here We Go!")
time.sleep(1.5)

# Define maximum attempts
max_attempts = 5
attempts = 0  # Variable to track the number of attempts

# While loop for the guesses
while attempts < max_attempts:
    try:
        # Get the user's guess
        guess = int(input("Enter your guess: "))
        attempts += 1  # Increment the attempt count
        time.sleep(0.5)

        # Check if the player has run out of attempts
        if attempts == max_attempts and guess != generated_num:
            print(f"That's 5 Strikes! Game over! The correct number was {generated_num}.")
            break # Exit the loop when max attempts is reached
      
      # Compare the guess to the random number (give hints)
        if guess < generated_num:
            print("Too low! Try again.")
            time.sleep(0.5)
        elif guess > generated_num:
            print("Too high! Try again.")
            time.sleep(0.5)
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempt(s).")
            time.sleep(1)
            break  # Exit the loop if guessed correctly

        
    except ValueError:
        print("Please enter a valid number.")

print("Thanks for playing!")
