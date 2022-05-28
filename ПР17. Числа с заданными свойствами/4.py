def div3(n):
    div = []
    another_div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            if 1000 > i > 100 and i % 10 == 3:
                div.append(i)

            if n // i != i and 1000 > n // i > 100 and (n // i) % 10 == 3:
                div.append(n // i)
    if len(div) == 3:
        return min(div)
    return 0


count = 0
N = 97**3 + 1
while count != 5:
    w = div3(N)
    if w != 0:
        print(N, w)
        count += 1
    N += 1