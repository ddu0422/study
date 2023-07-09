directions = {
    'N': (-1, 0),
    'W': (0, -1),
    'S': (1, 0),
    'E': (0, 1)
}

def solution(park, routes):
    # 초기화
    n, m = len(park), len(park[0])
    x, y = 0, 0
    maps = []

    for i in range(n):
        temp = []
        for j in range(m):
            if park[i][j] == 'S':
                x, y = (i, j)
            temp.append(park[i][j])
        maps.append(temp)

    # 문제풀이
    for data in routes:
        # 명령어
        direction, distance = data.split(" ")

        # 방향 지정
        dx, dy = directions[direction]

        # 한 칸씩 이동
        for i in range(int(distance)):
            nx = x + dx
            ny = y + dy

            # 조건 1: 공원을 벗어나는 경우 명령어 무시
            if not (0 <= nx < n and 0 <= ny < m):
                x -= dx * i
                y -= dy * i
                break
            
            # 조건 2: 장애물인 경우 명령어 무시
            if maps[nx][ny] == 'X':
                x -= dx * i
                y -= dy * i
                break
            
            x, y = nx, ny
          
    return [x, y]

        


# park = ["SOO","OOO","OOO"] 
park = ["SOO","OXX","OOO"]
# park = ["OSO","OOO","OXO","OOO"]
# routes = ["E 2","S 2","W 1"]
routes = ["E 2","S 2","W 1"]
# routes = ["E 2","S 3","W 1"]

print(solution(park, routes))