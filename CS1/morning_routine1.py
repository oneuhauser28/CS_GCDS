a = 'snooze'
b = 'wake up'






print ('Good morning! Your alarm is going off.')
while True:
    user_wake = input('Do you snooze or wake up? ').lower()
    if user_wake == a:
        print('You go back to sleep')
        print('Your alarm is going off again.')
    if user_wake == b:
        print('You get up.')
        next_step = input('What is the temperature outside? ').lower()
        if next_step < 50:
            print('Put on a coat.')
        elif next_step >= 50:
            print('You put on a t-shirt.')

    
