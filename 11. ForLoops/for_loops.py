# 'char' holds a character in the string 'Version Control' in each iteration progressively
for char in 'Version Control':
    print(char)

# 'num' holds a number in collection of numbers in each iteration
for num in [1, 2, 3, 4, 5]:
    print(num)

# 'name' holds an element in collection in each iteration
for name in ['Vasu', 'Sara', 'Emily']:
    print(name)



# range() function creates an object, it's not a list but a special kind of object that we can iterate over

# Prints numbers from 0 to 9
for i in range(10):
    print(i)
print()     # For newline '\n'

# Prints numbers form 5 to 9
for i in range(5, 10):
    print(i)
print()     # For newline '\n'

# Prints numbers from 5 to 9 with a step of 2 ,i.e. 5, 7, 9
for i in range(5, 10, 2):
    print(i)
print()     # For newline '\n'
