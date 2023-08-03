"""
명함 지갑
=> 가로 x 세로 다양한 명함을 담을 수 있는 지갑을 만들 예정
가로 x 세로를 90도로 돌려 명함을 넣을 수 있다면 효율적인 명함 지갑을 만들 수 있음
"""

def solution(sizes):
    horizontal = []
    vertical = []

    for size in sizes:
        if size[0] > size[1]:
            horizontal.append(size[0])
            vertical.append(size[1])
        else:
            horizontal.append(size[1])
            vertical.append(size[0])

    return max(horizontal) * max(vertical)

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes))