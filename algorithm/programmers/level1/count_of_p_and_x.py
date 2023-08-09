def solution(s: str):
    s = s.lower()

    return s.count('p') == s.count('y')


s = "pPoooyY"
print(solution(s))
