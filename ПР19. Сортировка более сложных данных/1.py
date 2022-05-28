f = open('26-79.txt')
N, K = map(int, f.readline().split())
forest = {}
for i in range(N):
    row, col = map(int, f.readline().split())
    if row in forest:
        forest[row].append(col)
    else:
        forest[row] = [col]

max_row = 0
min_three = 0
for row in forest:
    if len(forest[row]) != 1:
        forest[row].sort()
        for i in range(1, len(forest[row])):
            if forest[row][i] - forest[row][i - 1] - 1 == K:
                if max_row < row:
                    min_three = forest[row][i - 1] + 1
                    max_row = row
                break
print(max_row, min_three)