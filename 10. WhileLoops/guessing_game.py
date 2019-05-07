secretKey = 7
message = f'''
{'*' * 42}
Welcome to the guessing game !
Rules - Guess the correct number to win.
Hint - It can be any number between 1 - 20
{'*' * 42}
'''

print(message)

turn = 1
while turn <= 3:
    if turn == 1:
        guess = int(input('First guess... '))
    elif turn == 2:
        guess = int(input('Another guess...? '))
    else:
        guess = int(input('Last guess... '))

    if guess == secretKey:
        print('Yay! You won.\n')
        break;
    turn += 1

if turn == 4:
    print('Noooo! You lost.\n')
