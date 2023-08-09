def solution(s, n):
    answer = ''

    for alpha in s:
        if alpha.islower():
            answer += chr((ord(alpha) - ord('a') + n) % 26 + ord('a'))

        if alpha.isupper():
            answer += chr((ord(alpha) - ord('A') + n) % 26 + ord('A'))
        
        if alpha == ' ':
            answer += ' '

    return answer


s = "a B z"
n = 4
print(solution(s, n))