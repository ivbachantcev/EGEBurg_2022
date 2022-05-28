with open('5.txt') as f:
    s = f.readlines()
    count = 0
    for i in s:
        if i.count('E') > i.count('A'):
            count += 1
    print(count)
