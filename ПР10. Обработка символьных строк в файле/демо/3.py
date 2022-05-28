with open('3.txt') as f:
    s = f.readline()
    maximum = 0
    count = 0
    c = ''
    for i in range(len(s)):
        if s[i] == 'X' and count % 3 == 0 or s[i] == 'Y' and count % 3 == 1 or s[i] == 'Z' and count % 3 == 2:
            count += 1
            maximum = max(maximum, count)
        elif s[i] == 'X':
            count = 1
        else:
            count = 0
    print(maximum)
