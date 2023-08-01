"""
1번 지표: R / T
2번 지표: C / F
3번 지표: J / M
4번 지표: A / N

=> 총 16개 MBTI

n개의 질문지 / 7개의 선택지
점수표를 이용한 점수 제공
단, 모르겠음 => 0점

더 높은 점수를 받은 성격 유형이 검사자의 성격 유형
예외) 점수가 같은 경우 사전 순으로 빠른 성격 유형이 검사자의 성격 유형

== example ==
choices [5, 3, 2, 7, 5]

AN: 5 / N: 1
CF: 3 / C: 1
MJ: 2 / M: 2
RT: 7 / T: 3
NA: 5 / A: 1

=> TCMA

고려해야할 점
1. 성격 유형 검사 표 2묶음씩 나누는 방법
2. 예외처리 고려
   - 예외) 점수가 같은 경우 사전 순으로 빠른 성격 유형이 검사자의 성격 유형
"""


def solution(survey, choices):
    answer = ''

    # 초기화
    alpha = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    maps = {}

    for value in alpha:
        maps.update({value: 0})

    # 점수 계산
    for index, value in enumerate(survey):
        score = abs(4 - choices[index])
        
        if choices[index] > 4:
            maps[value[1]] += score
        else:
            maps[value[0]] += score

    # MBTI 결정
    for i in range(0, len(alpha), 2):
        mbti = dict(list(maps.items())[i:i+2])
        answer += max(mbti, key=mbti.get)

    return answer



survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]
print(solution(survey, choices))