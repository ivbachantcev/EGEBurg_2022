def count_div(n):
    count = 2
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    return count


count_5 = 1
N = 700_001
prev_count_div = count_div(700_000)
print(700_000, prev_count_div)
while count_5 != 5:
    w = count_div(N)
    if w > prev_count_div:
        print(N, w)
        prev_count_div = w
        count_5 += 1
    N += 1
