"""
동전의 종류: N
적절히 사용해서 가치의 합을 K로
동전 개수의 최솟값은?
"""
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))


def soltuion(coins, k):
    answer = 0
    coins = sorted(coins, reverse=True)

    for coin in coins:
        if coin > k:
            continue
        
        answer += k // coin
        k %= coin
        

    return answer


print(soltuion(coins, k))
