matrix = []
s = input()
while s != 'end':
    s = s.split()
    matrix.append([int(i) for i in s])
    s = input()
# print(*matrix, sep='\n')
row = len(matrix)
column = len(matrix[0])
new_matrix = [[0 for _ in range(column)] for _ in range(row)]
for i in range(row):
    for j in range(column):
        new_matrix[i][j] = matrix[i-1][j] + matrix[(i+1) % row][j] + matrix[i][j - 1] + matrix[i][(j + 1) % column]
    print(*new_matrix[i])