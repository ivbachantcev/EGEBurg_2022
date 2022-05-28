def simple_numb(n):
    for i in range(2, round(n**.5) + 1):
        if n % i == 0:
            return False
    return True


count = 3
n = 9_999_997
while count != 0:
    if simple_numb(n):
        print(10_000_000 - n, n)
        count -= 1
    n -= 1
n = 10_000_001
while count != 3:
    if simple_numb(n):
        print(n - 10_000_000, n)
        count += 1
    n += 1

