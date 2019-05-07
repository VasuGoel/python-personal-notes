# 'cartoons' is a list. Lists have similar properties to strings
cartoons = ['Mickey', 'Charlie', 'Donald', 'Johnny', 'Shaggy']

# Prints out the entire list
print('list -',cartoons)

# Prints out the first item of list
print(cartoons[0])

# Prints out last item and second to last item
print('Last item -', cartoons[-1], '& Second Last item -', cartoons[-2])

# Prints out elements from starting index to end index excluding the end index
print(cartoons[0:3])

# Prints out entire list since default "end index" value is equal to "length of the list"
print(cartoons[0:])

# Prints out elements of list from default "start index" i.e. 0 to end index
print(cartoons[:5])

# Changing elements of list
cartoons[4] = 'Mini'
print(cartoons)



# Copy list to another list
# another_cartoons = cartoons
another_cartoons = cartoons[:]      # another way

print('another_cartoons -', another_cartoons)

# Prints out elements of list from first element to last element excluding it
print(another_cartoons[1:-1])
