f = open('26-4k.txt')
N, K = map(int, f.readline().split())
m = [int(f.readline()) for _ in range(N)]
m.sort(reverse=True)
min_winner = sum(m[:K]) // K
min_prizewinner = sum(m[K:K+K]) // K
print(min_prizewinner, min_winner)