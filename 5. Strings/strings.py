# NOTE - Python string index starts from 0 to (length of string - 1)

string = "This is a test string"

# Prints out the entire string
print('string -',string)

# Prints out the first character of string
print(string[0])

# Prints out last character and second to last character
print('Last character -', string[-1], '& Second Last character -', string[-2])

# Prints out sequence of characters form starting index to end index excluding the end index
print(string[0:3])     # Prints out Thi
                       # <index>    012

# Prints out entire string since default "end index" value is equal to "length of the string"
print(string[0:])

# Prints out string from default "start index" i.e. 0 to end index
print(string[:5])




# Copy string to another variable
# another_string = string
another_string = string[:]      # another way

print('another_string -', another_string)

# Prints out string from first character to last character excluding it
print(another_string[1:-1])
