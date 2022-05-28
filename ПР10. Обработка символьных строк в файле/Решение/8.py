with open('../файлы/8.txt') as f:
    s = f.readline()
count = 0
max_count = 0
for i in range(len(s)):
    if s[i] == 'C' and count % 2 == 0 or s[i] == 'A' and count % 2 == 1:
        count += 1
    else:
        max_count = max(count, max_count)
        if s[i] == 'C':
            count = 1
        else:
            count = 0
print(max_count)