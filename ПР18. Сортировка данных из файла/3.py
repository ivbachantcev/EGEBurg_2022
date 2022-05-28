f = open('26-3k.txt')
N, K, M = map(int, f.readline().split())
m = [int(f.readline()) for _ in range(N)]
m.sort(reverse=True)
min_winner = min(m[:K])
min_prizewinner = min(m[K:K+M])
print(min_prizewinner, min_winner)