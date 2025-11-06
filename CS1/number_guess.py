def print_colored_text(text, color_name):
        
    colors = {                
        'red': '\033[31m',      # Red text color
        'green': '\033[32m',    # Green text color
        'cyan': '\033[36m',     # Cyan text color
        'white': '\033[37m',    # White text color
        'reset': '\033[0m',     # Reset text color to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m') 
    print(f"{color_code}{text}\033[0m")   


import random

number = random.randint(1,100)
attempts = 0

while True:
    guess = input('Pick a number between 1 and 100. ')
    if not guess.isdigit():
        print('Please pick a valid number.')
        continue
    guess = int(guess)
    attempts += 1

    if guess < number:
        print_colored_text('Too low! Try again...','red')
    elif guess > number:
        print_colored_text('Too high! Try again...','cyan')
    
    else:
        print_colored_text(f'Congratulations! You guessed it in {attempts} tries.','green')
        break
    