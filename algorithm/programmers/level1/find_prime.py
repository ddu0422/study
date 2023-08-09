def solution(n):
    maps = [True] * (n + 1)
    # 0과 1은 소수가 아님
    maps[0] = maps[1] = False

    for i in range(2, int(n**(1/2) + 1)):
        if maps[i]:
            j = 2
            while i * j <= n:
                maps[i * j] = False
                j += 1
        
    return maps.count(True)


n = 5
print(solution(n))