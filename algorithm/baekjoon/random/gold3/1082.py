import sys

n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))[:n]
m = int(sys.stdin.readline().rstrip())

d = [0] * (m + 1)

# 큰 값을 구해야하므로, 큰 값부터 넣는다.
for i in range(n - 1, -1, -1):
    # 숫자의 가격부터 의미가 있으므로 p[i]로 설정한다.
    for j in range(p[i], m + 1):
        # 현재 숫자의 가격이전의 숫자에서 현재 숫자를 더한다. (0-9 까지이므로 가능)
        d[j] = max(d[j], d[j - p[i]] * 10 + i)


print(d[m], sep='\n')
