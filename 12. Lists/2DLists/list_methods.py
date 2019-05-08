numbers = [2, 4, 6, 9, 5]
print(f'Original list: {numbers}')

# Add new item to the end of the list
numbers.append(20)
print(f'numbers.append(20): {numbers}')

# Add new item at a specific index in list
numbers.insert(1, 3)    # '1' is the index in which the number '3' is added in the list
print(f'numbers.insert(1, 3): {numbers}')

# Remove item form the list
numbers.remove(20)
print(f'numbers.remove(20): {numbers}')

# Pop the last element in the list
numbers.pop()
print(f'numbers.pop(): {numbers}')

# Return the index of first occurence of an element in the list
print(f'numbers.index(6): {numbers.index(6)}')

# NOTE: Above index() method generates an error if an element is not present in list that's why it's safer to use the 'in' operator which simply returns True or False
# Return boolean True or False if an element exists in a list or not
print(f'4 in numbers: {4 in numbers}')

# Count the number of occurences of an element in the list
print(f'numbers.count(9): {numbers.count(9)}')

# Sort the entire list in ascending order
numbers.sort()
print(f'numbers.sort(): {numbers}')

# Sort the entire list in descending order (first call sort() method to sort the list in ascending order then call reverse() method to return the descending order)
numbers.reverse()
print(f'numbers.reverse(): {numbers}')

# Copy the entire list to another list
numbers2 = numbers      # Stores the reference of list 'numbers' to another list 'numbers2' and any operations performed on 'numbers' will affect 'numbers2'
print(f'\nnumbers2: {numbers2}')

# Clear the entire list 'numbers'
numbers.clear()
print(f'numbers.clear() -> numbers: {numbers}')
print(f'numbers2: {numbers2}\n')



numbers = [2, 4, 6, 9, 5]
# Create a seperate copy of list 'numbers' and store it to another list 'numbers3', that way operations performed on 'numbers' wont affect 'numbers3'
numbers3 = numbers.copy()
print(f'numbers3: {numbers3}')

numbers.clear()
print(f'numbers.clear() -> numbers: {numbers}')
print(f'numbers3: {numbers3}')
