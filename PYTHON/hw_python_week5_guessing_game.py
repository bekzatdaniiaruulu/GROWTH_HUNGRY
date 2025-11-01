import random
def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    seсret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess > seсret_number:
            print("Your guess is too high!.")   
        elif user_guess < seсret_number:
            print("Your guess is too low!.")
        else:
            print(f"Congratulations! You've guessed the number {seсret_number} in {attempts} attempts.")
            break   
if __name__ == "__main__":
    guessing_game()
