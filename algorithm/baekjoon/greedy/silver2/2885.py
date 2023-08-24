"""
막대는 정사각형 N개
초콜릿의 크기는 항상 2의 제곱 형태 (1, 2, 4, 8, 16 ...)

K개 정사각형을 먹어야함.
나머지 초콜릿은 선영이를 준다.

항상 가운데로만 쪼개진다.
D개 있는 막대는 D/2개 막대 두 조각으로 쪼개진다.

K개 정사각형을 만들기 위해서 몇 번의 초콜릿을 쪼개야 하는지와 사야하는 가장 작은 초콜릿의 크기는?
"""
k = int(input())


def solution(k):
    binary = bin(k)[2:][::-1]
    # 2의 거듭제곱인 경우 쪼갤 필요가 없다.
    if binary.count('1') == 1:
        return [k, 0]
    
    return [2**len(binary), len(binary) - binary.find('1')]


print(*solution(k))
