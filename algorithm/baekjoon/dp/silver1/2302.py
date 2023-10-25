from functools import reduce


n = int(input())
m = int(input())
vips = []
for _ in range(m):
    vips.append(int(input()))

d = [0] * 41


def solution(n, vips, d):
    result = []

    d[0] = d[1] = 1
    for i in range(2, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    
    current_vip = 0

    for vip in vips:
        result.append(d[vip - current_vip - 1])
        current_vip = vip

    if current_vip < n:
        result.append(d[n - current_vip])

    return reduce(lambda x, y: x * y, result)


print(solution(n, vips, d))
