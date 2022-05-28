f = open('../5.txt')
w = [int(s) for s in f.readlines()]
countT = 0
maxS = 0
for i in range(2,len(w)):
    q = w[i - 2] + w[i - 1] + w[i]
    c = max(w[i-2], w[i-1], w[i])
    a = min(w[i-2], w[i-1], w[i])
    b = q - a - c
    if c*c == a*a + b*b:
        countT += 1
        if q > maxS:
            maxS = q
print(countT, maxS)
f.close()