d = dict()
n = int(input())
for _ in range(n):
    s = input().split()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
print(max(d.items(), key=lambda x: x[1]))
