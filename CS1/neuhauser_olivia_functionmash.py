import random                                                               #imports the random library

def prechorus():                                                            #new function called prechorus
    '''
    Prechorus of a song to reduce lines needed for a song
    Args: 
        No parameters
    
    Return/Print: 
    prechorus(str): The lyrics written for the prechorus are printed when the function is called

    Raises: 
        No error detection
    '''

    print("""                                                            
No fears alone at night, she's sailing through the crowd
In her ears the phones are tight and the music's playing loud
          """)                                                              #prints prechorus when called


    
def chorus():                                                               #new function called chorus
    '''
    Chorus of a song to reduce lines needed for a song
    Args: 
        No parameters

    Return/Print: 
    chorus(str): The lyrics written for the chorus are printed when the function is called

    Raises: 
        No error detection
    '''
    print("""
She gets rock n' roll, on a rock n roll station
And a rock n roll dream
She's making movies on location
She don't know what it means
And the music make her wanna be the story
And the story was whatever was the song what it was
Roller girl, don't worry
DJ, play the movies 
All night long (all night long)
          """)                                                              #prints chorus when called


def sing_song():                                                            #new function called sing_song
    '''
    Function which uses previous function prechorus and chorus to reduce lines needed to print the lyrics of a song
    Args: 
        No parameters
    
    Return/Print: 
        song(str): The lyrics of the entire song using functions prechorus and chorus

    Raises: 
        No error detection
    '''
    print("""
I seen a girl on a one way corridor
Stealing down a wrong way street
For all the world like an urban toreador
She had wheels on, on her feet
Well, the cars do the usual dances
Same old cruise and the curbside crawl
But the roller girl she's taking chances
They just love to see her take them all
          """ )                                                             #prints first part of song lyrics
    prechorus()                                                             #calls prechorus function
    print("""
Hallelujah, here she comes
Queen roller ball
And Enchanté, what can I say?
Don't care at all
You know, she used to have to wait around
She used to be the lonely one
But now that she can skate around town
She's the only, only one 
          """)                                                              #prints next part of song lyrics
    prechorus()                                                             #calls prechorus function
    chorus()                                                                #calls chorus function
    print("""
She tortures taxi drivers just for fun
She likes to read their lips
Says, "Toro toro taxi, see ya tomorrow, my son"
I swear she let a big truck grease her hip
She got her own world in the city
You can't intrude on her, no-no, no-no
She got her own world in the city
The city's been so rude to her
          """)                                                              #prints next part of song lyrics 
    prechorus()                                                             #calls prechorus function
    chorus()                                                                #calls chorus function
    print("""
Slipping and sliding
Yeah, life's roller ball
Slipping and a sliding
Skate away, that's all
Skate away
Skate away
She's going singing, 'Shala shalay, hey hey'
Skate away
          """)                                                              #prints final part of song 
    

def add(a,b):                                                               #new function called add 
    '''
    Function which adds two numbers together

    Args: 
        a(int): First number given
        b(int): Second number given

    Return/Print: 
        a+b(int): Prints the value of the numbers combined

    Raises: 
        No error detection
    '''
    print(a + b)                                                            #prints the value of two given numbers combined

def print_list(alist):
    for item in alist:
        print(item)

def in_list(alist, element):
    return element in alist

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def get_integer(prompt):
    while True: 
        user_input = input(prompt)
        try: 
            number = float(user_input)
            if number.is_integer():
                return int(number)  
            else:
                print("Please enter a whole number. ")
        except ValueError: 
            print("Invalid input, please enter a number. ")

 
def get_random():
    n1 = get_integer("Enter first number: ")
    n2 = get_integer("Enter second number: ")
    if n1 < n2:
        result = random.randint(n1, n2)
        print(f"Random number between {n1} and {n2}: {result}")
    else: 
        result = random.randint(n2, n1)
        print(f"Random number between {n2} and {n1}: {result}")


def count_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]           
    count = 0                                           

    for character in string:
        if character in vowels: 
            count +=1 
    
    return count

def reverse_string():
    original = input("Please enter word you would like reversed: ")
    print(original[::-1])


def is_palindrome(): 
    word = input("Please enter the word you would like to check: ")
    return
    #check if word and reverse are equal
    #if yes, return true
    #if no, return false
    #print is this a palindrome? yes/no


def get_initials(name): 
    name = input("Please enter your first and last name separated by spaces: ").split(" ")
    #take index 1 of each word
    #print or return index one with f"initials are: {}"

def replace_character(character):
    ''''''
            


def main():
    sing_song()
    add(5,5)
    user_list = input("Enter list using spaces to separate items ").split(" ")
    print_list(user_list)
    element = input("Enter check: ")
    in_list(user_list, element)
    alist = input("Please enter a list of items separated by spaces: ").split(" ")
    print_list(alist)





