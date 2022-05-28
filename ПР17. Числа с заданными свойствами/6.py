def simple_numb(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


def S(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            if not simple_numb(i):
                div.append(i)
            if n // i != i and not simple_numb(n // i):
                div.append(n // i)
    if div:
        return sum(div)
    return 0


count = 0
N = 912_673 - 2
while count != 5:
    w = S(N)
    if w and N % w == 0:
        print(N, w)
        count += 1
    N -= 2