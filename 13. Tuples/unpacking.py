coordinates = (1, 2, 3)     # 'tuple' object

# Say we wish to use the coordinates in the tuple as x, y, z then instead of doing something like,
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

# We can use a Python feature 'Unpacking' to achieve the same result like,
x, y, z = coordinates       # Unpacking the tuple into 3 variables
print(f'P(x, y, z): ({x}, {y}, {z})')


# Python 'lists' also support unpacking
numbers = [4, 5, 6]     # 'list' object
a, b, c = numbers
print(f'numbers[a, b, c] = [{a}, {b}, {c}]')
