def D(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            if i % 2:
                div.append(i)
            if i != n // i and (n // i) % 2:
                div.append(n // i)
    if len(div) < 6:
        return 0, 0
    div.sort(reverse=True)
    return div[5], len(div)


count = 0
N = 200_000_001
while count != 5:
    w = D(N)
    if w[0] != 0:
        print(w[0], w[1])
        count += 1
    N += 1