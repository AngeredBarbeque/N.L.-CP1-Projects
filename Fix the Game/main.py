import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        #You were taking guess as a string and trying to compare it to an integer. This is a runtime error.
        guess = (input("Enter your guess: "))
        #If you entered anything but a number, the game would crash. This is a runtime error. You didn't include a exception handler.
        try:
            guess = int(guess)
        except:
            print("Sorry, you entered something wrong. Try again.")
            continue
        #You didn't increase the number of attempts. This is a logic error and it allows the user to guess infinitely.
        attempts += 1
        #The game would tell you you ran out of attempts and you guessed correctly if you guessed correctly and ran out of attempts on the same guess. This is a logic error and it was because you placed attempts>= max_attempts before if guess == number to guess and made them seperate if statements.
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
        elif guess < number_to_guess:
            print("Too low! Try again.")
        continue
    print("Game Over. Thanks for playing!")
start_game()