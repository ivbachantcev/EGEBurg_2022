f = open('../1.txt')
countPar = 0
maxSum = -100000
posled = [int(i) for i in f.readlines()]
for i in range(1,len(posled)):
    if posled[i] % 3 == 0 or posled[i-1] % 3 == 0:
        countPar += 1
        q = posled[i] + posled[i-1]
        if q > maxSum:
            maxSum = q
print(countPar, maxSum)
f.close()
