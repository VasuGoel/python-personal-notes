dict = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
}

output = ''
number = input('> ')
for char in number:
    output += dict.get(char, '!') + ' '

print(f'>> {output}')
