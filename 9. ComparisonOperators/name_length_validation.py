name = input('Enter your name - ')

if len(name) < 3:
    print('Name must be at least 3 characters long')
elif len(name) > 50:
    print('Name must be maximum 50 characters')
else:
    print('Name looks good!')
