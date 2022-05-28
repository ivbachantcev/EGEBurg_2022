with open('../файлы/6.txt') as f:
    s = f.readline()
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'L' and count % 3 == 0 or s[i] == 'D' and count % 3 == 1 or s[i] == 'R' and count % 3 == 2:
            count += 1
        elif s[i] == 'L':
            count = 1
        else:
            max_count = max(max_count, count)
            count = 0
    print(max_count)