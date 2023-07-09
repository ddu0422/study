def solution(wallpaper):
    # 초기화
    n, m = len(wallpaper), len(wallpaper[0])
    map = [list(row) for row in wallpaper]
    x = []
    y = []

    # 문제풀이
    for i in range(n):
        for j in range(m):
            if map[i][j] == '#':
                x.append(i)
                y.append(j)

    return [min(x), min(y), max(x) + 1, max(y) + 1]


wallpaper = [
    "..........",
    ".....#....",
    "......##..",
    "...##.....",
    "....#....."
]
print(solution(wallpaper))