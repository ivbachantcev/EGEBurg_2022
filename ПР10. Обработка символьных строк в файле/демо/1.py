with open('1.txt') as f:
    s = f.readline()
    count = 1
    maximum = 0
    for i in range(1,len(s)):
        if s[i] != s[i-1]:
            count += 1
            maximum = max(maximum, count)
        else:
            count = 1
    print(maximum)
