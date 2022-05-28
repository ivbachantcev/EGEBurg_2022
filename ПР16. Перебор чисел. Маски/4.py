def nine(n):
    result = 0
    power_digit = 0
    while n != 0:
        d = n % 9
        result += d*(10**power_digit)
        n //= 9
        power_digit += 1
    return result


def check(n):
    for r in range(len(n) - 1):
        if n[r] < n[r + 1]:
            return False
    return True


def print_result(n):
    nine_numb = nine(int(n))
    if check(str(nine_numb)):
        print(n, sum([int(k) for k in str(nine_numb)]))


for i in range(10):
    for j in range(1000):
        numb = '3' + str(i) + '458' + str(j) + '3'
        print_result(numb)
    numb = '3' + str(i) + '4583'
    print_result(numb)
