def solution(keymap, targets):    
    # 초기화
    answer = []
    letters = [0] * 26

    # 문제 풀이
    # 각 문자별 최소 자판 횟수
    for key in keymap:
        for i in range(len(key)):
            index = ord(key[i]) - ord('A')
            if letters[index] == 0 or letters[index] > i + 1:
                letters[index] = i + 1

    # target을 완성하기 위한 최소 자판 횟수
    for target in targets:
        sum = 0
        for alphabet in target:
            index = ord(alphabet) - ord('A')
            if letters[index] != 0:
                sum += letters[index]
            else:
                sum = -1
                break
        answer.append(sum)

    return answer

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]

print(solution(keymap, targets))

keymap = ["AABC"]
targets = ["AABC", "A"]

print(solution(keymap, targets))