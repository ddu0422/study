"""
1. +1MHz
2. -1MHz
3. N개의 버튼: 즐겨찾기

A: 현재 주파수
B: 듣고 싶은 주파수
A -> B로 갈 때 눌러야 하는 가장 적은 버튼 수

=== example ===
Input
100 15 => A, B
1      => N
15     => 즐겨찾기 주파수 채널


Output
15

주파수 단위는 신경쓰지 않아도 됨.
"""

a, b = map(int, input().split())
n = int(input())
bookmarks = [int(input()) for _ in range(n)]

def solution(a, b, bookmarks):
    # 현재 주파수에서 1단계씩 올려 원하는 주파수로 가는 경우
    answer = abs(b - a)

    # 각 즐겨찾기로 이동 후 1단계식 올려 원하는 주파수로 가는 경우
    counts = [abs(bookmark - b) + 1 for bookmark in bookmarks]

    return min(answer, min(counts))


print(solution(a, b, bookmarks))
