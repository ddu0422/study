"""
친구 N명에레 롤케이크 1개씩
롤케이크 길이 A1, A2, ..., An
길이가 10인 롤케이크만 먹는다.

롤케이크를 잘라서 길이가 10인 롤케이크를 최대한 많이 만든다.

1. 자를 롤케이크를 하나 고른다. 길이가 1보다 큰 롤케이크만 자를 수 있다. 이때, 고른 롤케이크의 길이를 x라고 한다.
2. 0보다 크고, x보다 작은 자연수 y를 고른다.
3. 롤케이크를 잘라 길이가 y, x-y인 롤케이크 두 개로 만든다.

롤케이크를 최대 M번 자를 수 있다.
이때, 만들 수 있는 길이가 10인 롤케이크의 개수의 최댓값은?

5 7
10
20 -> 10 10 (1)
30 -> 10 10 10 (2)
40 -> 10 10 10 10 (3)
50 -> 10 40 (1)

5 8
12 -> 10 2 (1)
23 -> 10 10 3 (2)
34 -> 10 10 10 4 (3)
45 -> 10 10 25 (2)

# Greedy
# 10의 배수부터 잘라야 더 많은 10의 빵을 얻을 수 있다.
# 횟수가 남는 경우 횟수 + 1 개의 빵을 얻을 수 있다.
# 횟수가 부족한 경우 횟수개의 빵을 얻을 수 있다.

# 10의 배수가 아니지만 m이 남은 경우
# 횟수가 남는 경우 횟수개의 빵을 얻을 수 있다.
# 횟수가 부족한 경우에도 횟수개의 빵을 얻을 수 있다.
"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
cakes = list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(m, cakes):
    answer = 0

    # 10의 배수인 경우 몫 - 1회 만큼 자르기
    for value in sorted(list(filter(lambda x: not x % 10, cakes))):
        if m - (value // 10 - 1) >= 0:
            m -= (value // 10 - 1) # 30을 2회 자라서
            answer += value // 10  # 10을 3개를 만들 수 있다.
        else:
            answer += m            # 전부 자를 수 없는 경우 남은 횟수만큼 10을 만들 수 있다.
            m = 0
            break

    # 10의 배수가 아닌 경우 몫만큼 자르기
    for value in sorted(list(filter(lambda x: x % 10, cakes))):
        if m - (value // 10) >= 0:
            m -= (value // 10)
            answer += (value // 10)
        else:
            answer += m
            break
    
    return answer


print(solution(m, cakes))
