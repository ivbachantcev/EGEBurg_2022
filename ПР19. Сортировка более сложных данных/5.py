f = open('26-73.txt')
N = int(f.readline())
matrix = [[0 for _ in range(480)] for _ in range(640)]
for _ in range(N):
    row, col = map(int, f.readline().split())
    matrix[row - 1][col - 1] = 1
min_row = 650
max_len_light = 0
for i in range(640):
    count_light = 0
    max_count = 0
    for j in range(480):
        if matrix[i][j] == 1:
            count_light += 1
        else:
            max_count = max(max_count, count_light)
            count_light = 0
    if max_count >= max_len_light:
        max_len_light = max_count
        min_row = i + 1
print(max_len_light, min_row)