import sys

n, s, m = map(int, sys.stdin.readline().rstrip().split())
v = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
d = [[0] * (m + 1) for _ in range(n + 1)]


# 현재 볼륨 = 직전 볼륨 ± 조절할 수 있는 볼륨의 크기
# 변수는 2개가 있다.
# 1. index
# 2. 볼륨 조절(+, -)

def solution(s, n, m, v, d):
    # 현재 시작값 볼륨
    d[0][s] = 1

    # 다음으로 조절할 수 있는 볼륨값부터
    for i in range(1, n + 1):
        # 현재 볼륨을 조절할 수 있는 값 구하기
        for j in range(m + 1):
            if d[i - 1][j]:
                plus = j + v[i]
                minus = j - v[i]

                # 볼륨을 더했을 때, 볼륨 조절이 가능한 지 확인
                if 0 <= plus <= m:
                    d[i][plus] = 1
                
                # 볼륨일 뺐을 때, 볼륨 조절이 가능한 지 확인
                if 0 <= minus <= m:
                    d[i][minus] = 1


    # 가능한 볼륨 중 가장 큰 값 찾기
    answer = - 1

    for j in range(m + 1):
        if d[n][j]:
            answer = j

    return answer


print(solution(s, n, m, v, d))
