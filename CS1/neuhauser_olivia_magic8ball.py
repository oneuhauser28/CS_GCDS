while True:

    import random
    import time
    
    responses = [
        'Sure',
        'No',
        'Maybe',
        'Ask again later',
        'Yes, definitely',
        'Do not count on it',
        'Outlook is good',
        'Certainly not',
        'Absolutely'
    ]
    
    user = input('Ask the Magic 8 Ball a question (press enter to quit): ')
    print('Shaking the 8 Ball...')
    time.sleep(1)

    if user == '':
        print('Stopping the game.')
        break

    elif '?' not in user:
        print('Please enter a valid question. ')
        continue

    else:
        print('The Magic 8 Ball says: ', random.choice(responses))