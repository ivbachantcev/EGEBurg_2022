with open('../файлы/5.txt') as f:
    s = f.readline()
    count = 0
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'L':
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    print(max_count)