"""
1. 조합 발음은 가능
2. 연속 발음 불가능

가능한 발음을 숫자로 변경
숫자만 되어있는 경우 발음 가능 단, 연속 숫자인 경우 발음 불가
문자가 포함되어 있는 경우 발음 불가
"""


def solution(babbling):
    answer = 0
    dictionary = ['aya', 'ye', 'woo', 'ma']

    for word in babbling:
        for index, value in enumerate(dictionary):
            word = word.replace(value, str(index))
        if word.isdigit() and check_serialize(word):
            answer += 1

    return answer


def check_serialize(digit):
    for i in range(len(digit) - 1):
        if digit[i] == digit[i + 1]:
            return False
        
    return True


babbling = ["aya", "yee", "u", "maa"]
print(solution(babbling))