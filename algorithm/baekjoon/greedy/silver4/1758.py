"""
8시가 될 때까지 대기

8시가 되는 순간 입구에서 커피를 받고 자리로 이동
"강호"는 커피를 하나씩 주는 역할
"손님"은 "강호"에게 팁을 줌

팁: 커피를 몇 번째 받는지에 따라 정해짐 (원래 주려고 했던 돈 -  받은 등수 + 1)
단, 음수인 경우 받을 수 없음

=== example ===
민호: 3원
재필: 2원
주현: 1원

민호 => 3 - 1 + 1 = 3
재필 => 2 - 2 + 1 = 1
주현 => 1 - 3 + 1 = -1 (팁 x)

순서를 적절히 바꿨을 때 팁의 최댓값은?
(팁을 많이 주는 인원을 앞으로 배치)
"""
import sys

n = int(input())
tips = []
for _ in range(n):
    tips.append(int(sys.stdin.readline().rstrip()))


def solution(tips):
    return sum(
        filter(
            lambda x: x > 0,
            [value - index for index, value in enumerate(sorted(tips, reverse=True))]
        )
    )


print(solution(tips))
