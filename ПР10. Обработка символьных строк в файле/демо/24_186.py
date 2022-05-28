with open('24-186.txt') as f:
    s = f.readline()
    count = 0
    numb = ''
    for i in range(len(s)):
        if s[i].isdigit():
            numb += s[i]

        else:
            if len(numb) == 11 and numb[0] == '7' and (int(numb[0])+int(numb[1])) == (int(numb[-2])+int(numb[-1])):
                count += 1
            numb = ''
    print(count)