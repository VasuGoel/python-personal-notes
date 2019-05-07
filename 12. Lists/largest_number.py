array = [23, 53, 23, 76, 9]
largest_yet = None
for x in array:
    if largest_yet is None:
        largest_yet = x
    elif x > largest_yet:
        largest_yet = x

print(f'Largest number in list: {largest_yet}')
