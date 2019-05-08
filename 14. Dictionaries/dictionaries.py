# Dictionaries in Python are a way to store "key": "value" pair. In a dictionary, their can be no duplicate keys, in other words, each key in a dictionary is unique

customer = {
    "name": "John Smith",    # it can also be 'name': 'John Smith'
    "age": 30,
    "is_verified": True
}

print(type(customer))       # Prints <class 'dict'>

# Note the "key" in the customer["key"] should match the "key" in the dictonary i.e. customer["name"] is valid for dictionary above but customer["Name"] is not valid.
print(f'customer["name"]: {customer["name"]}')
print(f'customer["age"]: {customer["age"]}')
print(f'customer["is_verified"]: {customer["is_verified"]}')

# Updating "value" of any "key"
customer["name"] = "Jack Sparrow"
print(f'After updating, customer["name"]: {customer["name"]}')

# Adding new "key": "value" pair
customer["birth_place"] = "Palo Alto"
print(f'customer[birth_place]: {customer["birth_place"]}')

# Printing the entire dictonary object
print(f'\ncustomer: {customer}\n')



# To avoid getting error at runtime, for passing an invalid key in customer["key"], we can use the get() method which returns the "value" for the "key" passed in get("key") else returns 'None' for invalid keys and doesn't give an error instead
print(f'customer.get("age"): {customer.get("age")}')
print(f'customer.get("birth_date"): {customer.get("birth_date")}')      # Prints None

# We can pass a default value with get("key", "value") method, which will return the "value" passed if the "key" is not present in dictonary
print(f'customer.get("birth_date") with default value: {customer.get("birth_date", "Dec 7, 1980")}')
print(f'customer.get("age"): {customer.get("age", "100")}')     # Still prints 30 as "age" key is present in the dictionary

# NOTE: print(customer["birth_date"])    still gives error since the get("key", "value") return the "value" passed if the "key" is not present and doesn't actually change or add new "key": "value" pair
