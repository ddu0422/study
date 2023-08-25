"""
마지막 레이싱을 제외한 나머지 레이싱 모두 종료
F7의 우승자는 각 레이싱을 통해서 얻은 점수의 합이 가장 높은 사람이 우승 (동점인 경우 전부 우승자)
마지막 레이싱에서 1등을 한 사람은 N점을 얻고 2등은 N-1... N등은 1점을 얻는다.

각 레이싱에서 두 드라이버의 등수가 같은 경우는 없다.
우승할 가능성이 있는 사람의 수를 구하시오.

8  4 = 12
9  3 = 12
10 2 = 12
8 1  = 9

12 5  = 17
14 4  = 18
14 3  = 17
15 2  = 17
15 1  = 16

1. 나                  => 1등을 한 경우 (2~3 점수보다 크거나 같으면 우승할 수 있다.)
2. 나를 제외한 가장 작은 수 => 2등하는 경우
3. 나를 제외한 가장 큰 수  => (동일 점수 인 경우 위로 올라가는 내용 고려)꼴지하는 경우
"""
import sys

n = int(sys.stdin.readline().rstrip())
racer = []
for _ in range(n):
    racer.append(int(sys.stdin.readline().rstrip()))


def solution(racer):
    n = len(racer)
    answer = 1
    racer = sorted(racer, reverse=True)
    score = racer[-1] + 1
    for i in range(1, n):
        if racer[i] + n >= score:
            answer += 1
        # 같은 점수가 연속으로 나오는 경우 점수가 증가한다.
        score = max(score, racer[i] + (i + 1))
    
    return answer


print(solution(racer))
