import sys

INF = 1e9

n = int(sys.stdin.readline().rstrip())
distance = [[INF] * 26 for _ in range(26)]

for _ in range(n):
    x, y = sys.stdin.readline().rstrip().split(' is ')
    # 단방향
    distance[ord(x) - ord('a')][ord(y) - ord('a')] = 1

m = int(sys.stdin.readline().rstrip())
results = []

for _ in range(m):
    x, y = sys.stdin.readline().rstrip().split(' is ')
    results.append((x, y))


for k in range(26):
    for i in range(26):
        for j in range(26):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for x, y in results:
    print('T' if distance[ord(x) - ord('a')][ord(y) - ord('a')] != INF else 'F')
