def simple_numb(n):
    for i in range(2, round(n**.5)+1):
        if n % i == 0:
            return False
    return True


for i in range(105_000_000, 115_000_000 + 1):
    n = i
    while n % 2 == 0:
        n //= 2
    w = round((n**.5)**.5)
    if simple_numb(w) and w**4 == n:
        print(i, n)
