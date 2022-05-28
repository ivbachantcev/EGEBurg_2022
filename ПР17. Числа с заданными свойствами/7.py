def simple_numb(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


def F(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            if simple_numb(i):
                div.append(i)
            if n // i != i and simple_numb(n // i):
                div.append(n // i)
    if div:
        return sum(div) // len(div)
    return 0


count = 0
N = 650_000 + 1
while count != 4:
    w = F(N)
    if w and w % 37 == 23:
        print(N, w)
        count += 1
    N += 1