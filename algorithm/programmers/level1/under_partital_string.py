def solution(t, p):
    answer = 0

    # p의 길이가 더 긴 경우 예외
    if len(p) > len(t):
        return 1

    # 처음부터 마지막 뒤까지 잘라서 비교
    for i in range(0, len(t) - len(p) + 1):
        number = int(t[i:i + len(p)])
        if int(p) >= number:
            answer += 1

    return answer


# 배열 split 시 t 길이만큼 진행

t = "10203"
p = "15"

print(solution(t, p))
