"""
스크린 N칸, 바구니 M칸 (M < N)
왼쪽 / 오른쪽 이동 가능
바구니(M)은 스크린(N)을 넘어갈 수 없음

가장 처음 바구니는 스크린의 왼쪽 M칸을 차지

사과는 하나씩 떨어진다.

바구니가 사과가 떨어지는 칸을 차지하고 있다면 바구니는 사과가 바닥에 닿을 때 사과를 담을 수 있다.
사과를 모두 담기 위한 바구니의 이동 거리 최솟값은?

=== example ===
5 1
3
1
5
3

3: 사과 개수
1: 0칸 이동
5: 오른쪽으로 4칸 이동
3: 왼쪽으로 2칸 이동
"""
n, m = map(int, input().split())
j =  int(input())
apples = [int(input()) for _ in range(j)]


def solution(n, m, apples):
    answer = 0
    left = 1
    right = m
    
    for apple in apples:
        # 바구니 안쪽에 있는 사과일 경우
        if left <= apple and apple <= right:
            continue
        
        # 바구니보다 왼쪽에 있는 사과일 경우
        if apple < left:
            distance = left - apple
            left -= distance
            right -= distance

        # 바구니보다 오른쪽에 있는 사과일 경우
        if apple > right:
            distance = apple - right
            left += distance
            right += distance
        
        answer += distance
    
    return answer


print(solution(n, m, apples))
