f = open('../2.txt')
w = [int(s) for s in f.readlines()]
d = 160
p = 7
countP = 0
maxS = 0
for i in range(10000):
    for j in range(i+1,10000):
        if w[i] % d != w[j] % d and (w[i] % p == 0 or w[j] % p == 0):
            countP += 1
            q = w[i] + w[j]
            if q > maxS:
                maxS = q
print(countP, maxS)
f.close()