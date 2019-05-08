def calc_cost(cost, shipping_charges, discount_amount):
    print(f'Total cost: ${float(cost + shipping_charges - discount_amount)}')

calc_cost(discount_amount=2, cost=50, shipping_charges=5)       # Unlike postitional arguments the order doesn't matter with keyword arguments

# Above is an exampke of keyword arguments, which is different from positional argument in a way that the latter doesn't require any keywords like cost, shipping_charges, discount_amount but their position or order in which those numbers are passed is important while in keyword arguments the position doesn't matter
# We use keyword arguments to improve the readability of our code.
# For most part, we should use positional arguments but if we're dealing with functions that take multiple numerical values we could use keyword arguments to improve the readability of code.

# Note: If we're passing both keyword and positonal arguments then make sure to use the keyword arguments after the positional arguments
