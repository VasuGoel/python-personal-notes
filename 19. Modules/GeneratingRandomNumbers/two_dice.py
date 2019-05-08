import random

class Dice:
    def roll(self):
        # Returning tuple containing two random numbers between 1-6 (both inclusive)
        # numbers = (random.randint(1, 6), random.randint(1, 6))
        # return numbers

        # Returning tuple directly
        # return (random.randint(1, 6), random.randint(1, 6))

        # Python shortcut to return a tuple
        return random.randint(1, 6), random.randint(1, 6)



dice = Dice()
print('Tossing 2 unbiased dice...')
a, b = dice.roll()      # Unpacking tuple to 2 variables a, b

print(f'Result: ({a}, {b})')
