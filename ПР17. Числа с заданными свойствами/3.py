def P(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            div.append(i)
            if n // i != i:
                div.append(n // i)
    if len(div) < 5:
        return 0, 0
    div.sort()
    return div[0]*div[1]*div[2]*div[3]*div[4], div[4]


count = 0
N = 500_000_001
while count != 5:
    w = P(N)
    if w[0] != 0 and w[0] % 100 == 91 and w[0] <= N:
        print(w[0], w[1])
        count += 1
    N += 1