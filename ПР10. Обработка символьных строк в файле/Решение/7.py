with open('../файлы/7.txt') as f:
    s = f.readline()
count = 0
max_count = 0
for i in range(len(s)):
    if s[i] == 'B' and count % 4 == 0 or s[i] == 'A' and count % 4 == 1 or s[i] == 'F' and count % 4 == 2 or s[i] == 'E' and count % 4 == 3:
        count += 1
    else:
        max_count = max(count, max_count)
        if s[i] == 'B':
            count = 1
        else:
            count = 0
print(max_count)