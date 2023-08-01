"""
삼총사: 학생 3명의 정수 번호를 더했을 때 0이 되는 경우

<예시>
-2, 3, 0, 2, -5

case 1) 1, 3, 4
case 2) 2, 4, 5
"""
import itertools


def solution(number):
    answer = 0

    for subset in itertools.combinations(number, 3):
        if sum(subset) == 0:
            answer += 1

    return answer


number = [-3, -2, -1, 0, 1, 2, 3]
print(solution(number))