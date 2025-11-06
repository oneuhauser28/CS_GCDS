a = '9'
b = '11' 
c = '1'

d = 'run'
e = 'ignore'

f = 'annoy'
g = 'stay silent'

h = 'attack'
i = 'flee'
print('You and your friends are out for Halloween.')


while True:
    user_answer = input('Choose: Do you come back at 9, 11, or 1? ')
    if user_answer == a:
        print('You got home safe! You are a smart cookie...')
        break
    elif user_answer == b:
        print ('You think there is a car following you...')
        user = input('Do you run or ignore? ').lower()
        if user == d: 
            print ('You made it home safe... barely!')
            break
        elif user == e:
            print('The person in the car bribes you with candy...you get in the car.')
            choice = input('Do you annoy the kidnapper or stay silent? ').lower()
            if choice == f:
                print('The kidnapper gets annoyed and kicks you out of the car. Interesting strategy, but functional!')
                break
            elif choice == g:
                print('The kidnapper drives you...home? It was a test from your parents, and they are never letting you out again.')
    if user_answer == c:
        print('You see a clown. You think it is just a halloween costume, then he pulls out a knife.')
        dumb = input('Do you attack or flee? ').lower()
        if dumb == h:
            print('The clown tries to stab someone. You realize it is a fake knife. You feel bad for the clown. You give him your candy.')
            print('You go home.')
            break
        if dumb == i:
            print('The clown yells: I was just trying to give you candy!')
            print('Your mom is not home... your dad says she was dressed as a clown.')
            break

