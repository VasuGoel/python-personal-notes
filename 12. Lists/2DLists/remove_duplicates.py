numbers = [12, 34, 12, 28, 87, 28, 34, 87, 90, 12]

# Returning a new list that doesn't contain duplicates
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(f'New list without duplicates: {uniques}')
