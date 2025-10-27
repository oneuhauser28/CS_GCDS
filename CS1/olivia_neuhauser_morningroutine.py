
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

print('Your plane crashes and you are stranded on an island.')

user_welcome = input('Choose: Do you collect resources, take a nap, or try to find others? ').lower()

if 'resources' in user_welcome:
        print_colored_text('You collect food and materials.','cyan')
        collect = input('Do you build a shelter or a fire first? ').lower()

        if 'shelter' in collect:
            print_colored_text('You are safe in your shelter by the time night falls.','cyan')
            next_day = input('Do you go into the woods or stay on the beach the next day? ').lower()

            if 'woods' in next_day:
                print_colored_text('You do not see the boat that could have saved you. You are eaten by a hungry bear.','red')
                
            elif 'beach' in next_day: 
                print_colored_text('You see a fishing boat nearby.','cyan')
                fishing = input('Do you wave or yell? ').lower()

                if 'wave' in fishing:
                    print_colored_text('The driver does not see you and steers away. You lay down on the beach and accept your fate.','red')
                    
                elif 'yell' in fishing:
                    print_colored_text('The person on the boat sees you and comes over. You are rescued!','green')
                    
        elif 'fire' in collect:
            print_colored_text('You attract a bunch of bugs at night.','cyan')
            bites = input('Do you ignore the bites or find aloe vera to put on it? ').lower()

            if 'ignore' in bites:
                print_colored_text('The bugs were carrying a deadly disesase.','red')
                
            elif 'aloe' in bites:
                print_colored_text('You heal quickly.','cyan')
                final = input('Now, do you build a hut or explore the island? ').lower()

                if 'hut' in final:
                    print_colored_text('A plane sees your shelter and rescues you!','green')
                    
                elif 'explore' in final: 
                    print_colored_text('You sink into quicksand.','red')

                elif 'island' in final:
                     print_colored_text('You sink into quicksand.','red')
elif 'nap' in user_welcome:
            print_colored_text('A hungry bear eats you, because you slept so deeply it thought you were dead.', 'red')

elif 'others' in user_welcome:
        print_colored_text('You find someone else from the flight.','cyan')
        friend = input ('Do you work together or separate? ').lower()

        while True:
            if 'together' in friend:
                print_colored_text('You survive together for a week, then see a plane in the distance...','cyan')
                saved = input('Do you wave your arms or start a fire? ').lower()

                if 'wave' in saved:
                    print_colored_text('You have to wait for the next plane, this one did not see you.','cyan')
                elif 'fire' in saved:
                    print_colored_text('The plane sees you, you get rescued!','green')
                    break
            elif 'separate' in friend:
                print_colored_text('You forget you are not supposed to drink saltwater, and die of thirst.','red')
                break
                

