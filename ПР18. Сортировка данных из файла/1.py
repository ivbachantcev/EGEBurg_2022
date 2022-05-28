f = open('26-k1.txt')
N, K = map(int, f.readline().split())
products = [int(f.readline()) for _ in range(N)]
products.sort(reverse=True)
sum_sales = sum(products[:K])*.2
max_product = products[K]
print(max_product, int(sum_sales))