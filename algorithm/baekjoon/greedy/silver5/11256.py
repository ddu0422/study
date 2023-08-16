"""
J개의 사탕 상자에 포장
크기가 다른 상자 N개 / 최소한의 상자만 사용 (박스를 다 채울 필요는 없다.)

T: 테스트 케이스 개수
j: 사탕의 개수
n: 상자의 개수
r: 세로 길이, c: 가로 길이
"""
t = int(input())


def solution(j, boxes):
    answer = 0
    boxes = sorted([a * b for a, b in boxes], reverse=True)

    total = 0
    for box in boxes:
        if j <= total:
            break
        total += box
        answer += 1
    
    return answer


for _ in range(t):
    j, n = map(int, input().split())
    boxes = []
    for _ in range(n):
        a, b = map(int, input().split())
        boxes.append((a, b))

    print(solution(j, boxes))
