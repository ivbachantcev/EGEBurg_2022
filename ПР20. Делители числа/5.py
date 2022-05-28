for i in range(100_000_000, 300_000_000 + 1):
    N = i
    n = 0
    m = 0
    while N % 2 == 0:
        m += 1
        N //= 2
    while N % 7 == 0:
        n += 1
        N //= 7
    if N == 1:
        if m % 2 == 1 and n % 2 == 0:
            print(i, m+n)
            