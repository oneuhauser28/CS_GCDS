color = "red"

while True:
    user_color = input('Enter any color ').lower()
    if user_color == color:
        print('Well done!')
        break
    else:
        print('Try again...')

