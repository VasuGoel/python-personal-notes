# Logical and: All conditions have to be True
has_good_income = True
has_good_credits = True

if has_good_income and has_good_credits:
    print('Eligible for loan')
else:
    print('Not eligible for loan')


# Logical or: At least one condition has to be True
age = 17
gender = 'male'

if age >= 18 or gender == 'female':
    print('Entry')
else:
    print('No entry')


# Logical not operator simply inverses the boolean value
has_good_credits = True
has_criminal_record = False

if has_good_credits and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan')
