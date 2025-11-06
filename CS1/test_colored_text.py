def print_colored_text(text, color_name):
        
    colors = {                
        'red': '\033[31m',      # Red text color
        'green': '\033[32m',    # Green text color
        'white': '\033[37m',    # White text color
        'reset': '\033[0m',     # Reset text color to default
    }
    
    color_code = colors.get(color_name.lower(), '\033[37m') 
    print(f"{color_code}{text}\033[0m")                    

print_colored_text('hello', 'green')