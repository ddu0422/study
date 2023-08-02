"""
1. 한 번의 한 명의 유저를 신고
  - 신고 횟수 제한 없음
  - 서로 다른 유저를 계속 신고 가능
2. k번 이상 신고된 유저는 게시판 이용이 정지
   해당 유저를 신고한 유저에게 정지 사실을 메일로 발송

== example ==
전체 유자: muzi, frodo, apeach, neo
k(신고 횟수): 2번
유저ID 신고ID
muzi frodo
apeach frodo
frodo neo
muzi nedo
apeach muzi

frodo / neo 2번 신고

## 결과 ##
유저ID   / 신고ID       / 정지ID
muzi    / frodo, nedo / frodo, neo (2)
frodo   / neo         / neo        (1)
apeach  / muzi, frodo / frodo      (1)
neo     / x           / x

각 유저별로 처리 결과 메일을 받은 횟수: [2, 1, 1, 0]
"""

def solution(id_list, report, k):
    answer = []
    
    # 초기화
    reports = {}
    reports_history = {}

    for id in id_list:
        reports.setdefault(id, 0)
        reports_history.setdefault(id, [])

    # 신고
    for data in report:
        reporter, reported = data.split()
        # 이미 신고를 진행한 경우 다시 신고할 수 없음
        if reported in reports_history[reporter]:
            continue
        reports[reported] += 1
        reports_history[reporter].append(reported)

    # 정지 대상자
    block_list = []
    for data in reports.items():
        if data[1] >= k:
            block_list.append(data[0])

    # 신고 대상자 확인
    for data in reports_history.values():
        result = 0
        for reported in data:
            if reported in block_list:
                result += 1
        answer.append(result)

    return answer


def solution_refactoring(id_list, report, k):
    # 이미 신고를 진행한 경우 다시 신고할 수 없음
    report = set(report)
    
    # 초기화
    reports = {id: 0 for id in id_list}
    reports_history = {id: [] for id in id_list}

    # 신고
    for data in report:
        reporter, reported = data.split()
        reports[reported] += 1
        reports_history[reporter].append(reported)

    # 정지 대상자
    block_list = [data[0] for data in reports.items() if data[1] >= k]

    # 신고 대상자 확인
    return [len(set(data) & set(block_list)) for data in reports_history.values()]


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))
print(solution_refactoring(id_list, report, k))