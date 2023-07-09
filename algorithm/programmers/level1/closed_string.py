def solution(s):
    answer = []
    dictionary = {}

    for i in range(len(s)):
        alpha = s[i]

        # 처음 나오는 문자인 경우 결과에 -1을 저장합니다.
        # 현재 문자열의 index를 문서에 저장합니다.
        if dictionary.get(alpha) == None:
            answer.append(-1)
            dictionary.setdefault(alpha, i)
        # 2번 이상 나온 문자인 경우 결과 몇 번째만에 나왔는지 확인합니다. (현재 index - 기존 index)
        # 몇 번째만에 해당 문자가 나왔는지 계산하여 결과에 저장합니다.
        # 현재 문자열의 index를 문서에 저장합니다.
        else:
            count = i - dictionary[alpha]
            answer.append(count)
            dictionary[alpha] = i

    return answer

s = "banana"

print(solution(s))