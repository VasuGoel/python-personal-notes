import utils


list = []

n = int(input('Enter the size of list: '))
print(f'Enter the {n} elements:')
for i in range(n):
    list.append(int(input('> ')))

print(f'utils.find_max(list): {utils.find_max(list)}')
