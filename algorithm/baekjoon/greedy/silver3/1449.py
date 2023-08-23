"""
가장 왼쪽에서 정수만큼 떨어진 거리만 물이 샌다.
길이가 L인 테이프를 가지고 있다.

물을 막을 때, 그 위치와 좌우 0.5만큼 간격을 줘야 물이 새지 않는다.
물이 새는 곳의 위치와, 테이프의 길이가 주어졌을 때 필요한 테이프의 최소 개수를 구하시오.

테이프를 자를 수 없고, 겹쳐서 붙이는 것도 가능한다.

4 3
1 2 4 5

2
"""
n, l = map(int, input().split())
pipes = list(map(int, input().split()))[:n]


def solution(l, pipes):
    if l == 1:
        return len(pipes)
    
    answer = 0
    total = 0
    pipes.sort()

    for i in range(len(pipes) - 1):
        distance = pipes[i + 1] - pipes[i]
        if total + distance <= l - 1:
            total += distance
        else:
            total = 0
            answer += 1
    
    return answer + 1


print(solution(l, pipes))
