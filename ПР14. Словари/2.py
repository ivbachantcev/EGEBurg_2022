d = dict()
n = int(input())
for _ in range(n):
    w1, w2 = input().split()
    d[w1] = w2
    d[w2] = w1
print(d[input()])