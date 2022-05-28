def simple_numb(n):
    for i in range(2, round(n**.5)+1):
        if n % i == 0:
            return False
    return True


def count_div(n):
    div = []
    for i in range(2, round(n**.5) + 1):
        if n % i == 0:
            div.append(i)
            if n // i != i:
                div.append(n // i)
    if len(div) == 2:
        if simple_numb(div[0]) and simple_numb(div[1]) and div[0] % 10 == div[1] % 10:
            return True
    return False


sum_numb = 0
count_numb = 0
for i in range(264871, 322989 + 1):
    if count_div(i):
        sum_numb += i
        count_numb += 1
print(count_numb, int(sum_numb / count_numb))