with open('4.txt') as f:
    count = 0
    maximum = 0
    s = f.readline()
    for i in range(len(s)):
        if s[i] == 'A' and count % 2 == 0 or s[i] == 'B' and count % 2 == 1:
            count += 1
            maximum = max(maximum, count)
        elif s[i] == 'A':
            count = 1
        else:
            count = 0
    print(maximum)