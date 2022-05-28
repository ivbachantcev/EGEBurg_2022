f = open('../4.txt')
w = [int(s) for s in f.readlines()]
countT = 0
maxS = 0
for i in range(2,len(w)):
    a = max(w[i],w[i-1],w[i-2])
    b = min(w[i],w[i-1],w[i-2])
    c = w[i] + w[i-1] + w[i-2] - a - b
    if a*a < b*b + c*c:
        q = w[i] + w[i-1] + w[i-2]
        countT += 1
        if q > maxS:
            maxS = q
print(countT, maxS)
f.close()