def count_div(n):
    count = 2
    for i in range(2, round(n**.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count


n = 700_000 + 1
while True:
    n1 = count_div(n)
    n2 = count_div(n + 1)
    n3 = count_div(n + 2)
    n4 = count_div(n + 3)
    n5 = count_div(n + 4)
    if n1 < n2 < n3 < n4 < n5:
        print(n, n1)
        print(n + 1, n2)
        print(n + 2, n3)
        print(n + 3, n4)
        print(n + 4, n5)
        break
    n += 1