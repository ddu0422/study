"""
1차 서류심사 / 2차 면접시험
다른 모든 지원자와 비교했을 때 서류심사 성적과 면접시험 성적 중 적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
선발할 수 있는 신입사원의 최대 인원수

5
3 2
1 4
4 1
2 3
5 5

===
4
1 4, 2 3, 3 2, 4 1, 5 5

---
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1

===
3
o 1 4
x 2 5
x 3 6
o 4 2
x 5 7
o 6 1
x 7 3
"""
import sys
t = int(sys.stdin.readline().rstrip())


def solution(scores):
    # 서류심사 성적으로 정렬한다.
    scores = sorted(scores, key=lambda x: x[0])

    # 서류심사 성적이 1등인 경우 절대 떨어질 수 없다.
    answer = 1
    max_interview_score = scores[0][1]

    # 서류심사 성적이 낮지만 면접 성적이 높은 면접자들이 합격한다.
    # 면접 성적은 점점 높아지므로 값을 갱신해야한다.
    for value in scores[1:]:
        interview_score = value[1]
        if max_interview_score > interview_score:
            max_interview_score = interview_score
            answer += 1

    return answer


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    scores = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        scores.append((a, b))
    sys.stdout.write(str(solution(scores)) + "\n")
