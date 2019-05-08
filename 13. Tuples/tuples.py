# Tuples are immutable list i.e it is similar to list except we can't change the tuple once defined. Operations like numbers[0] = "something", insert(), pop() etc. won't work on tupples
# Useful when you wanna create a list of items that doesn't change throughout the program

tuple = (1, 2, 3)
print(type(tuple))      # Prints <class 'tuple'>

# tuple[0] = 4    illegal operation sinse 'tuple' object doesn't support item assignment
print(f'tuple[2]: {tuple[2]}')

# count() and index() are the few methods that work on 'tuples' object since they just provide info about the tuple not change it
print(f'tuple.count(2): {tuple.count(2)}')

print(f'tuple.index(3): {tuple.index(3)}')
