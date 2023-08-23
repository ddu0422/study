"""
병든 나이트가 N x M 크기 체스판의 가장 왼쪽 아래 위치

병든 나이트 이동 범위
1. 2칸 위로 1칸 오른쪽
2. 1칸 위로 2칸 오른쪽
3. 1칸 아래로 2칸 오른쪽
4. 2칸 아래로 1칸 오른쪽

방문한 칸의 수 최대
이동 횟수가 4번보다 많다면, 이동 방법을 모두 한 번씩 사용
이동 횟수가 4번보다 많지 않다면, 제약 사항 x
"""
n, m = map(int, input().split())


def solution(n, m):
    # 나이트는 첫 칸을 차지하고 있음
    answer = 1

    # 위로 움직일 수 없는 경우
    if n == 1:
        return answer
    
    # 오른쪽 2칸만을 사용한 경우 
    if n == 2:
        answer += min((m - 1) // 2, 3)
        return answer
    
    # 오른쪽 1칸만을 사용한 경우
    if m < 7:
        answer += min(m - 1, 3)
        return answer
    
    # 4번 이상으로 이동하는 경우
    # 최소 위로 3칸 오른쪽으로 7칸 필요
    # 1번 방법과 4번 방법으로만 이동해야 최대한 많이 이동 가능
    answer += 4 + (m - 7)
    
    return answer


print(solution(n, m))
