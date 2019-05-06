first_name = 'John'
last_name = 'Smith'

# Suppose we wanna print out John [Smith] is a coder


# Naive approach (harder to visualize the string)
message = first_name + ' [' + last_name + ']' + ' is a coder'
print(message)

# Way better approach is to use formatted strings in python (easier to visualize the string)
# f'' is a way to denote formatted string in python, {variable_name} are placeholders waiting to be filled in by python
msg = f'{first_name} [{last_name}] is a coder'
print(msg)
 
