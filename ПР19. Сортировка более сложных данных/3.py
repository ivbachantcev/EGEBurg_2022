f = open('26-76.txt')
L, M, N = map(int, f.readline().split())
details = [list(map(int, f.readline().split())) for _ in range(N)]
details.sort()
count_stay = 0
max_stay = 0
for i in range(N - 1):
    t = details[i + 1][0] - details[i][1]
    if t >= M:
        count_stay += 1
        max_stay = max(max_stay, t)
print(count_stay, max_stay)