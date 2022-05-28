d = dict()
s = input().split()
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    print(i, d[i])
