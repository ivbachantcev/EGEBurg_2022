with open('24-191.txt') as f:
    s = f.readline()
    c = ''
    count = 0
    flagA = 0
    for i in range(len(s)):
        if s[i] not in 'AB':
            c += s[i]
        elif s[i] == 'B':
            if flagA:
                c += s[i]
                flagA = 0
                if len(c) >= 20 and c.count('F') == 2:
                    count += 1
            else:
                c = ''
        else:
            c = 'A'
            flagA = 1
    print(count)
