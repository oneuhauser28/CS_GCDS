import random

user = input('What is your name? ')
print(f'Good luck, {user}!')

words = ['coding',
         'python',
         'notebook',
         'school',
         'classroom', 
         'computer',
         'windows',
         'whiteboard',
         'glasses',
         'random'
         ]
games = 0
wins = 0


while True:
    comp = random.choice(words)
    scramble = list(comp)
    random.shuffle(scramble)
    display = ''.join(scramble)
    turns = 5

    while turns > 0:
        guess = input(f'Guess the real word for {display}: ')

        if guess == comp:
            print('You got it!')
            wins += 1 
            break
        else:
            while True:
                re = input('Incorrect, would you like to re-scramble (y/n)? ')

                if re == 'n':
                    break
                elif re == 'y':
                    random.shuffle(scramble)
                    display = ''.join(scramble)
                    break 
                else:
                    print('Invalid response.')
                    
        turns -= 1

    print(f'The word was {comp}.')
    games += 1

    while True:
        again = input(f'You have played {games} game/s and won {wins}. Would you like to play again (y/n)? ')

        if again == 'n':
            quit()

        elif again == 'y':
            break

        else:
            print('Invalid response. Please limit to y or n.')
            
        quit()