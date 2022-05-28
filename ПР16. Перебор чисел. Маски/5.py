def seven(n):
    result = 0
    power_digit = 0
    while n != 0:
        d = n % 7
        result += d*(10**power_digit)
        n //= 7
        power_digit += 1
    return result


def check(n):
    return n == n[::-1]


def print_result(n):
    seven_numb = seven(int(n))
    if check(str(seven_numb)):
        print(n, sum([int(k) for k in str(seven_numb)]))


for i in range(10):
    for j in range(10000):
        numb = '1' + str(j) + '586' + str(i) + '6'
        print_result(numb)
    numb = '1586' + str(i) + '6'
    print_result(numb)
