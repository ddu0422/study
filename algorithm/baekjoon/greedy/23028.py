"""
총: 130학점 이상 수강
전공: 66학점 이상 수강

N학기 수강 완료
현재 전공 학점: A
현재 전체 학점: B

n학기별 전공과목 xn, 비전공과목yn
n학기당 최대 6과목 수강 가능
1과목당 3학점 (최대 18학점)

!8학기 안에 졸업!
"""
n, a, b = map(int, input().split())
semester = []
for _ in range(10):
    x, y = map(int, input().split())
    semester.append((x,  y))


def solution(n, a, b, semester):
    # 남은 학기
    rest_semester = 8 - n
    
    # 남은 전공 학점
    rest_major = 66 - a
    rest_credit = 130 - b

    # 학점을 채운 경우
    if a <= 0 and b <= 0:
        return True
    
    for major, minor in semester:
        rest_semester -= 1

        major_credit = major * 3
        minor_credit = min(minor, (6 - major)) * 3

        rest_major -= major_credit
        rest_credit -= (major_credit + minor_credit)

        # 남은 기간동안 전공과 총 학점을 채운 경우
        if rest_semester >= 0 and rest_major <= 0 and rest_credit <= 0:
            return True
        
    return False


print('Nice' if solution(n, a, b, semester) else 'Nae ga wae')
