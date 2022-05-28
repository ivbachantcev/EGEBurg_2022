f = open('26-2k.txt')
N, K = map(int, f.readline().split())
m = [int(f.readline()) for _ in range(N)]
m.sort()
mid = sum(m[K:N-K])
max_d = m[N-K-1]
print(max_d, mid // (N - 2 * K))
