def count_del(n):
    d = []
    for i in range(2, round(n**.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n // i)
    if len(d) == 4:
        d.sort()
        return d[-1], d[-2]
    else:
        return 0, 0


for i in range(157898, 157990 + 1):
    w = count_del(i)
    if w[0] != 0:
        print(w[0], w[1])