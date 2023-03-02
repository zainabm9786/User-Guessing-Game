#guessing game
import random
def guess(x):
    random_number= random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess<random_number:
            print("Your guess is TOO LOW. Guess again! ")
        elif guess>random_number:
            print('Your guess in TOO HIGH. Guess again! ')
    print(f'You guessed it correctly. The correct number was: {random_number}. CONGRATS!! ')

guess(10)

