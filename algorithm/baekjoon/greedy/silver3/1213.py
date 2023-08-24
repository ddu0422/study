"""
팰린드롬: 대칭 문자열

1. 전부 짝수인 경우
2. 홀수 1개 / 나머지 짝수인 경우
<=> 홀수 2개인 경우
"""
text = input()


def solution(text):
    alpha = [0] * 26

    for value in text:
        alpha[ord(value) - ord('A')] += 1

    if len(list(filter(lambda x: x & 1, alpha))) > 1:
        return "I'm Sorry Hansoo"
    
    answer = ''
    middle = ''

    for index, value in enumerate(alpha):
        character = chr(index + ord('A'))
        answer += character * (value // 2)
        
        if value & 1:
            middle = character
    
    return answer + middle + answer[::-1]


print(solution(text))
