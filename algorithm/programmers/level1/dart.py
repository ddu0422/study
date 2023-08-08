"""
1. 3번의 기회
2. 0~10점
3. SDT (1제곱, 2제곱, 3제곱)
4. * (해당 점수와 바로 전에 얻은 점수를 2배) / # (마이너스)
5. * 첫 번째에서도 나올 수 있음
6. *는 중첩 가능
7. #과 *도 중첩 가능
8. SDT 점수마다 하나씩 존재
9. *, #은 점수마다 하나만 존재하거나 존재 x
"""
import re


def solution(dartResult):
    answer = []
    squares = {'S': 1, 'D': 2, 'T': 3}

    m = re.findall(r'([0-9]{1,})(S|D|T)(\*|#){0,1}', dartResult)
    
    for index, value in enumerate(m):
        number, square, option = value
        score = int(number) ** squares[square]

        if option == '#':
            score = -score

        if option == '*':
            score *= 2
            if index > 0:
                answer[index - 1] *= 2 

        answer.append(score)

    return sum(answer)


dartResult = "1D2S3T*"
print(solution(dartResult))