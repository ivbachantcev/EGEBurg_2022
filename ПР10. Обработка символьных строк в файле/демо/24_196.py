with open('24-196.txt') as f:
    s = f.readline()
    maximum = 0
    c = s[0]
    count = 0
    for i in range(1,len(s)):
        if len(c) > 0 and (s[i] in 'XY' and c[-1] == 'Z' or s[i] == 'Z' and c[-1] in 'XY'):
            c += s[i]
            count += 1
            maximum = max(maximum, count // 2)
        elif s[i] == 'Z':
            c = 'Z'
            count = 1
        else:
            count = 0
    print(maximum)
    