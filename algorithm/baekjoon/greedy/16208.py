"""
n개의 쇠막대
a1 + a2 + a3 + ... + an 하나의 쇠막대
x+y인 막대를 길이 x,y인 두 개의 막대로 자를 때에는 두 막대의 길이의 곱인 xy의 비용이 든다.
최소 비용은?

=== example ===
4
3 5 4 2 => 총 14

5 9 = 45
4 5 = 20
3 2 = 6

"""
n = int(input())
rods = list(map(int, input().split()))[:n]


def solution(rods):
    answer = 0
    total = sum(rods)

    for rod in sorted(rods, reverse=True)[:-1]:
        answer += rod * (total - rod)
        total -= rod
    
    return answer


print(solution(rods))
