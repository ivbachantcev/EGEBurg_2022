with open('2.txt') as f:
    maximum = 0
    count = 0
    s = f.readline()
    for i in range(len(s)):
        if s[i] == 'X':
            count += 1
            maximum = max(maximum, count)
        else:
            count = 0
    print(maximum)
# print(max(map(len, open('24_demo.txt').readline().replace('Z', ' ').replace('Y', ' ').split())))
