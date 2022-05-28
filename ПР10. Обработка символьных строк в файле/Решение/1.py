with open('../файлы/1.txt') as f:
    s = f.readline()
    count = 1
    max_count = 0
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1
    print(max_count)