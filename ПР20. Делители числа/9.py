def count_div(n):
    count = 0
    for d in range(2, round(n**.5) + 1):
        if n % d == 0:
            count += 1
            if d != n // d:
                count += 1
    return count


def sum_digit(n):
    s = 0
    while n != 0:
        if n % 10 >= 3:
            return False, 0
        s += n % 10
        n //= 10
    return True, s


numbers = []
for i in range(1_000_000, 1_300_000 + 1):
    w = sum_digit(i)
    if w[0] and w[1] % 10 == 0:
        numbers.append([i, count_div(i)])
for i in range(9, len(numbers), 10):
    print(numbers[i])
