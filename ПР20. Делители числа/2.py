def criteria(n):
    sum_d = 0
    mul_d = 1
    while n != 0:
        t = n % 10
        sum_d += t
        mul_d *= t
        n //= 10
    if sum_d % 14 == 0 and mul_d % 18 == 0 and mul_d != 0:
        return sum_d, mul_d
    else:
        return 0, 0

result = []
for i in range(87921, 88187 + 1):
    w = criteria(i)
    if w[0] != 0:
        result.append(w)
result.sort(key=lambda x: x[1])
print(*result, sep='\n')
