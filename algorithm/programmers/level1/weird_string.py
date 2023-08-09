"""
1. 짝수번째 알파벳은 대문자
2. 홀수번째 알파벳은 소문자

주의)
1. 짝/홀은 index가 아니라 단어별로 짝/홀수 인덱스를 판단
2. 공백 개수는 한 개 이상
"""


def solution(s):
    answer = []
    index = 0

    for alpha in list(s):
        if alpha == ' ':
            index = 0
            answer.append(alpha)
            continue
        
        answer.append(alpha.upper() if index % 2 == 0 else alpha.lower())
        index += 1
    
    return ''.join(answer)


s = "try hello world"
print(solution(s))