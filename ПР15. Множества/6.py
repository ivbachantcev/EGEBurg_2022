s = input()
d = set()
for i in s:
    if i not in d:
        print(i, end='')
        d.add(i)