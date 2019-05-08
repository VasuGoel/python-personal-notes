matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f'matrix[2][0]: {matrix[2][0]}')
print(f'matrix[0][2] (before): {matrix[0][2]}')
matrix[0][2] = 33
print(f'matrix[0][2] (after): {matrix[0][2]}\n')

# Iterating over the entire matrix
i = 0
j = 0
for rows in matrix:
    for columns in rows:
        print(f'matrix[{i}][{j}]: {columns}')
        j += 1
    i += 1
    j = 0
