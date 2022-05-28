with open('../файлы/3.txt') as f:
    s = f.readline()
    c = ''
    max_count = 0
    for i in range(len(s)):
        if s[i] == 'A':
            c += 'A'
        else:
            max_count = max(len(c), max_count)
            c = ''
    print(max_count)
