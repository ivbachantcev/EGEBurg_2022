with open('6.txt') as f:
    s = f.readline()
    count = 0
    c = s[0]
    maximum = 0
    for i in range(1, len(s)):
        if len(c) > 0 and (s[i] == 'X' and c[-1] in 'YZ' or s[i] == 'Y' and c[-1] in 'ZX' or s[i] == 'Z' and c[-1] in 'YX'):
            c += s[i]
            count += 1
            maximum = max(maximum, count // 3)
        elif s[i] == 'Z':
            c = 'Z'
            count = 1
        else:
            c = ''
            count = 0
    print(maximum)
    