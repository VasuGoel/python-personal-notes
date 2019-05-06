string = 'This is a test string'

# len() is a general purpose function to count the number of characters in string or items in list
print('Length -', len(string))


# When a function belongs to a specific object we refer to it as method
# There are several string methods

# Convert string to uppercase (returns new string and does not harm original string)
print('Uppercase -', string.upper())

# Convert string to lowercase (returns new string and does not harm original string)
print('Lowercase -', string.lower())

# Convert string to Title string i.e every word in string starts with uppercase (returns new string and does not harm original string)
print('Title -', string.title())

# Return index of first occurrence of a character/string in string else returns -1 if not found
print('First occurrence of character s -', string.find('s'))             # Returns 3
print('First occurrence of string "test" -', string.find('test'))        # Returns 10

# Replace character or sub-string inside a string (returns new string and does not harm original string)
print('Replaced string -', string.replace('test', 'non-sensical test'))


# Check the existence of sub-string inside a string
# Different from find() method in a regard that find() return index whereas 'in' operator return boolean True or False
print('test' in string)
