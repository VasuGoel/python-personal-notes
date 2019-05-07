list = [5, 2, 5, 2, 2]

for i in list:
    output = ''
    for j in range(i):
        output += '*'
    print(output)


# Alternative - short-cut in python (most other languages don't support this string multiplication)
# for i in list:
#     print('*' * i)
