def solution(s):
    answer = 0

    same = 1
    diff = 0
    index = 1

    while index < len(s):
        first_letter = s[0]

        if first_letter == s[index]:
            same += 1
        else:
            diff += 1

        if same == diff:
            s = s[index + 1:]
            same = 1
            diff = 0
            index = 1
            answer += 1
            continue
        
        index += 1

    if len(s) >= 1:
        answer += 1

    return answer


s = "abracadabra"

print(solution(s))