def digit_two(n):
    while n % 11 != 0:
        if n % 11 == 2:
            return True
        n //= 11
    return False


max_numb = 0
for i in range(2031, 14312 + 1):
    if not digit_two(i):
        max_numb = max(max_numb, i)
print(max_numb)