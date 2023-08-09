def solution(s: str):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)


s = "1234"
print(solution(s))