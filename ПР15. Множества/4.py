n = input().split()
d = set()
for i in n:
    if i not in d:
        print('NO')
        d.add(i)
    else:
        print('YES')