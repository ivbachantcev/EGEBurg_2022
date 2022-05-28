n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]
count = 1
way = 'right'
row = 0
column = 0
while count <= n*n:
    if way == 'right':
        while matrix[row][column] == 0:
            matrix[row][column] = count
            count += 1
            column += 1
            if column == n:
                break
        way = 'down'
        row += 1
        column -= 1
    elif way == 'down':
        while matrix[row][column] == 0:
            matrix[row][column] = count
            count += 1
            row += 1
            if row == n:
                break
        way = 'left'
        row -= 1
        column -= 1
    elif way == 'left':
        while matrix[row][column] == 0:
            matrix[row][column] = count
            count += 1
            column -= 1
        row -= 1
        column += 1
        way = 'top'
    elif way == 'top':
        while matrix[row][column] == 0:
            matrix[row][column] = count
            count += 1
            row -= 1
        row += 1
        column += 1
        way = 'right'
for i in matrix:
    print(*i, sep='\t')