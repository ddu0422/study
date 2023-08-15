"""
체육복 문제와 동일
"""
n, s, r = map(int, input().split())
damaged = list(map(int, input().split()))[:s]
spares = list(map(int, input().split()))[:r]


def solution(n, damaged, spares):
    teams = ['O'] * n

    # 카약이 손상된 팀
    for value in damaged:
        teams[value - 1] = 'X'

    # 여분을 가져왔지만 카약이 손상된 팀
    for spare in list(set(spares) & set(damaged)):
        teams[spare - 1] = 'O'

    # 카약 여분이 있는 팀
    for sapre in list(set(spares) - set(damaged)):
        teams[sapre - 1] = 'S'

    # 카약을 주고 받은 팀
    for i in range(n - 1):
        if [teams[i], teams[i + 1]] in (['S', 'X'], ['X', 'S']):
            teams[i], teams[i + 1] = 'O', 'O'
    
    return teams.count('X')


print(solution(n, damaged, spares))
