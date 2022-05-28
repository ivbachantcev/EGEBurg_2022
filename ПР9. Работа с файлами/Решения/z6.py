f = open('../6.txt')
w = [int(s) for s in f.readlines()]
countT = 0
maxS = -1000000
for i in range(2, len(w)):
    if (w[i-1] % 10 == 9 and w[i-1] > 0) and not (w[i] % 10 == 9 and w[i] > 0) and not (w[i-2] % 10 == 9 and w[i-2] > 0):
        countT += 1
        q = w[i] + w[i-1] + w[i-2]
        if q > maxS:
            maxS = q
print(countT, maxS)
f.close()

