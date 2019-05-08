try:
    age = int(input('Age: '))       # Exception is ValueError, raised if input id not a number
    reciprocal = 1 / age            # Exception is ZeroDivisionError, raised if age is 0
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero.')
except ValueError:
    print('Invalid age.')


# We can simply write except: to catch all exceptions in the program
