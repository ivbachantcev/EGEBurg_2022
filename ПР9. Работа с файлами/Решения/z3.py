f = open('../3.txt')
w = [int(s) for s in f.readlines()]
countP = 0
maxS = -1
for i in range(1,len(w)):
    q = w[i] + w[i-1]
    if (w[i] % 3 == 0 or w[i-1] % 3 == 0) and q % 5 == 0:
        countP += 1
        if q > maxS:
            maxS = q
print(countP, maxS)
f.close()
