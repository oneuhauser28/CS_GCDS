import random                                                               #imports the random library
import time 

def prechorus():                                                            #new function called prechorus
    '''
    Prechorus of a song to reduce lines needed for a song
    Args: 
        No parameters
    Return/Print: 
    prechorus(str): The lyrics written for the prechorus are printed when the function is called
    Raises: 
        None
    '''
    time.sleep(0.5)
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
        None
    '''
    time.sleep(0.5)
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
        None
    '''
    time.sleep(0.5)
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
    time.sleep(0.5)
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
    time.sleep(0.5)
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
    time.sleep(0.5)
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
        None
    '''
    print(a + b)                                                            #prints the value of two given numbers combined

def print_list(alist):
    '''
    Function which takes a list and prints every element in that list individually 
    Args:
        alist(list): List provided by user
    Return/Print:
        item(str): Prints each element in the provided list
    Raises: 
        None
    '''
    for item in alist:
        print(item)

def in_list(alist, element):
    '''
    Function which checks whether or not a given element is in a given list
    Args:
        alist(list): list provided by user
        element(str): element provided by user
    Return/Print: 
        element in alist(bool): returns True or False based on whether or not provided element is in the list
    Raises: 
        Checks whether or not the element is in the list
    '''
    return element in alist
    

def is_integer(value):
    '''
    A function that checks whether an inputted value is a valid integer 
    Args: 
        value(int): value to be checked 
    Return/Print:
        value(bool): returns True or False based on whether or not the input is an integer
    Raises:
        ValueError: if the value given is not an integer, it returns False
    '''
    try:
        int(value)
        return True
    except ValueError:
        return False

def get_integer(prompt):
    '''
    Function which takes and stores a given value as long as it is an integer
    Args: 
        prompt(str): the question asked to the user to get the value that will be checked
    Return/Print:
        number(int): if the input is an integer, returns the input
        prints "Please enter a whole number" if the input is not an integer(str)
    Raises:
        ValueError: if the user does not provide a whole number value, they will be informed
    '''
    while True: 
        val = input(prompt)
        number = float(val)
        if number.is_integer():
            return int(number)  
        else:
            print("Please enter a whole number. ")


 
def get_random():
    '''
    Function that displays a random number between two given numbers inputted by the user
    Args:
        None
    Return/Print:
        Prints random number between the smallest and largest value given(str)
    Raises: 
        None
    '''
    n1 = get_integer("Enter first number: ")
    n2 = get_integer("Enter second number: ")
    if n1 < n2:
        result = random.randint(n1, n2)
        print(f"Random number between {n1} and {n2}: {result}")
    else: 
        result = random.randint(n2, n1)
        print(f"Random number between {n2} and {n1}: {result}")


def count_vowels(string):
    '''
    Function to count the amount of vowels in a word inputted by the user
    Args: 
        string(str): the word given by the user
    Return/Print:
        count(int): returns amount of vowels in given word
    Raises: 
        None
    '''
    vowels = ["a", "e", "i", "o", "u"]           
    count = 0                                           

    for character in string:
        if character in vowels: 
            count +=1 
    
    return count
    

def reverse_string(string):
    '''
    Function to reverse the letters in a word inputted by the user
    Args: 
        string(str): the word given by the user
    Return/Print:
        string[::-1](str): returns the given word reversed
    Raises: 
        None
    '''
    return(string[::-1])


def is_palindrome(): 
    '''
    Function that checks whether a word inputted by the user is a palindrome (same backwards as forward)
    Args:  
        None
    Return/Print:
        prints confirmation of whether or not the word is a palindrome(str)
        return True(bool): if word is palindrome returns true
        return False(bool): if word is not palindrome returns false
    Raises: 
        None
    '''
    word = input("Please enter the word you would like to check: ").lower()
    if word == reverse_string(word):
        print(f"Yes, {word} is a palindrome. ")
        return True
    else: 
        print(f"No, {word} is not a palindrome.")
        return False


def get_initials(): 
    '''
    A function which takes a name and returns the initials of the name
    Args: 
        None
    Return/Print:
        first_initial.last_initial(str): returns initials of given name
    Raises: 
        None
    '''
    full_name = input("Please enter your first and last name separated by spaces: ") #asks user for first and last name separated by spaces

    names = full_name.split(" ")                  #splits submitted name into separate items in a list based on the space between them
    first_initial = names[0][0].upper()           #variable first_initial takes first letter of first word in name, turns uppercase
    last_initial = names[1][0].upper()            #variable last_initial takes first letter of second word in name, turns uppercase

    return(f"{first_initial}.{last_initial}.")     #stores the capitalized initals with a period between them


def replace_character(word, old_letter, new_letter):
    '''
    A function which takes a string, an old character and a new character, and replaces every instance of the old character in the string of the old character with the new.
    Args: 
        word(str): word to go through and replace characters in
        old_letter(str): letter which will be replaced
        new_letter(str): letter which will replace all instances of old_letter
    Return/Print:
        result(str): prints the result of replaceing all of a certain letter in a given word with a different letter
    Raises: 
        None
    '''
    result = ""

    for letter in word: 
        if letter == old_letter:
            result += new_letter
        
        else:
            result += letter

    print(result)

def main(): 
    '''
    Main function with a menu for user to call any of the previous functions
    Args: 
        None
    Return/Print: 
        depending on what choice the user makes, uses choice of function
    Raises: 
        ValueError: If user makes a selection that is not on the list, they will be informed and returned to the menu. 
    '''
    while True: 
        time.sleep(2)
        print("\n---Options---")
        print("1. Sing song (Skateaway - Dire Straits)")
        print("2. Add two numbers together")
        print("3. Display a list you provide")
        print("4. Check whether an element is in a list you provide")
        print("5. Check whether a given input is an integer")
        print("6. Check whether a given input is an integer and store it")
        print("7. Display a random number between two given numbers")
        print("8. Count the number of vowels in a given word")
        print("9. Reverse a given word")
        print("10. Check whether a given word is a palindrome")
        print("11. Return the initials of a given name")
        print("12. Replace all instances of a certain letter in a given word with a different letter")
        choice = input("Enter your selection(1-12): ")

        if choice == "1":
            sing_song()

        elif choice == "2":
            first = int(input("Enter your first number: "))
            second = int(input("Enter your second number: "))
            add(first, second)

        elif choice == "3": 
            mylist = input("Please enter a list separated by spaces: ").split(" ")
            print_list(mylist)

        elif choice == "4": 
            mlist = input("Please enter a list separated by spaces: ").split(" ")
            myelement = input("Please enter element to be checked: ")
            print(in_list(mlist, myelement))

        elif choice == "5": 
            check = input("Please enter value to be checked: ")
            print(is_integer(check))

        elif choice == "6": 
            result = get_integer("Please enter value to be checked and stored: ")
            print(f"Stored value: {result}")

        elif choice == "7":
            get_random() 

        elif choice == "8": 
            vowels = input("Please enter a word for the vowels to be counted: ")
            print(count_vowels(vowels))

        elif choice == "9":
            reverse = input("Please enter word you would like reversed: ").lower()
            print(reverse_string(reverse))

        elif choice == "10":
            is_palindrome()
        
        elif choice == "11":
            print(get_initials())

        elif choice == "12":
            alter = input("Please enter word or phrase you would like to alter: ")
            replace = input("Please enter character you would like to replace: ")
            new = input("Please enter new character you would like to use to replace the old character: ")
            replace_character(alter, replace, new)

        else: 
            print("Please enter a valid input (any number from 1-12).")
            continue

main()

            