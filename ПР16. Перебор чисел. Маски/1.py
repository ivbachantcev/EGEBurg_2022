def simple_numb(n):
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            return False
    return True


def all_simple_div(n):
    div = []
    for i in range(2, int(n**.5) + 1):
        if n % i == 0:
            if simple_numb(i):
                div.append(i)
            if n // i != i and simple_numb(n // i):
                div.append(n // i)
    if div:
        return sorted(div)
    return div


count = 0
N = 2_352_000 + 1
while count != 5:
    w = all_simple_div(N)
    if w:
        s = ''.join([str(i) for i in w])
        if len(s) > 3 and s[:2] == '10' and s[-2:] == '29':
            print(N, max(w))
            count += 1
    N += 1
