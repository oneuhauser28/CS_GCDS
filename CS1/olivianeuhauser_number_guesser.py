
import random

number = random.randint(1,10)
max_attempts = 5

while max_attempts > 0:
        guess = input ('Pick a number between 1 and 10. ')
        
        if not guess.isdigit():
            print('Please pick a valid number.')
            continue

        guess = int(guess)

        if guess < number:
            print(f'Too low! You have {max_attempts-1} guesses left.')
        elif guess > number:
            print(f'Too high! You have {max_attempts-1} guesses left.')
        else:
            print(f'Congratulations! You guessed it in {6-max_attempts} tries.')
            break
        max_attempts -= 1