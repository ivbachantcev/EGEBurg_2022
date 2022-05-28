def S(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            div.append(i)
            if n // i != i:
                div.append(n // i)
    if len(div) < 3:
        return 0
    div.sort(reverse=True)
    return sum(div[:3])


def f(n):
    prev = n % 10
    while n != 0:
        if n % 10 < prev:
            return False
        prev = n % 10
        n //= 10
    return True


count = 0
N = 10_000_001
while count != 5:
    w = S(N)
    if w != 0 and f(w):
        print(w)
        count += 1
    N += 1