with open('../файлы/4.txt') as f:
    s = f.readline()
    count = 1
    max_count = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 1
    print(max_count)