"""
자신의 위치에서 거리가 K이하인 햄버거를 먹을 수 있다.

N: 식탁의 길이
K: 햄버거를 선택할 수 있는 거리

햄버거를 먹을 수 있는 사람의 최대 수?
HHPPP HPHPHPHP
PHPPP
"""
n, m = map(int, input().split())
table = list(input())[:n]


def solution(m, table):
    # 사람을 위치로 고정했을 경우 왼쪽에 있는 햄버거를 먹어야 다음 사람이 나올때 더 많은 햄버거를 먹을 수 있다.
    for i in range(len(table)):
        if table[i] == 'P':
            for j in range(i - m, i + m + 1):
                # 범위를 벗어나면 안되므로 확인한다.
                if 0 <= j < len(table) and table[j] == 'H':
                    table[j] = 'E'
                    break
                
    return table.count('E')
        

print(solution(m, table))
