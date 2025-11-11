while True:                                                                             #forever loop

    import random                                                                       #imports the random module, a built-in library for random numbers
    import time                                                                         #imports the time module, a built-in library for time related operations
    
    responses = [                                                                       #list all possible responses
        'Sure',                                                                 
        'No',                                                                   
        'Maybe',                                                                
        'Ask again later',                                                      
        'Yes, definitely',                                                         
        'Do not count on it',                                                   
        'Outlook is good',                                                      
        'Certainly not',                                                        
        'Absolutely',                                                           
        'Doubtful',                                                             
        'Undoubtedly'                                                           
    ]                                                                                   #end list 

    
    questions = [                                                                       #list question words
        'do',
        'does',
        'did',
        'should',
        'will',
        'would',
        'can',
        'have',
        'is',
        'were',
        'are',
        'has',
        'have',
        'am'
    ]                                                                                   #end list              
    
    user = input('Ask the Magic 8 Ball a question (press enter to quit): ').lower()     #set user as the response to the statement 'Ask the Magic 8 Ball a question (press enter to quit):, turn response lowercase
    print('Shaking the 8 Ball...')                                                      #display 'Shaking the 8 Ball...'
    time.sleep(1)                                                                       #delay the random response by 1 second

    if user == '':                                                                      #if user presses enter without any text
        print('Stopping the game.')                                                     #display 'Stopping the game.'
        break                                                                           #end loop

    elif '?' not in user:                                                               #otherwise if a question mark is not in user
        print('Please enter a valid question. ')                                        #display 'Please enter a valid question. '
        continue                                                                        #continue with the loop

    elif not any(item in user for item in questions):                                   #if no word in the user response matches a word in the question word list
        print('Please enter a valid question.')                                         #display 'Please enter a valid question'
        continue                                                                        #continue with the loop 
    
    else:                                                                               #if none of those conditions apply
        print('The Magic 8 Ball says: ', random.choice(responses))                      #display 'The Magic 8 Ball says:' followed by a random choice from the list of possible responses        