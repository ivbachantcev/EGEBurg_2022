f = open('26-71.txt')
N, S = map(int, f.readline().split())
products = {}
for _ in range(N):
    cod, weight = map(int, f.readline().split())
    if cod in products:
        products[cod].append(weight)
    else:
        products[cod] = [weight]
count_stay_product = 0
max_code_product = 0
max_count_product = 0
for code in products:
    cur_count = 0
    cur_weight = 0
    products[code].sort()
    for i in range(len(products[code])):
        if cur_weight + products[code][i] <= S:
            cur_weight += products[code][i]
            cur_count += 1
        else:
            break
    count_stay_product += len(products[code]) - cur_count
    cur_sum = sum(products[code][cur_count:])
    if cur_sum > max_count_product:
        max_count_product = cur_sum
        max_code_product = code
print(count_stay_product, max_code_product)
