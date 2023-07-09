DAY = 28

def solution(today, terms, privacies):
    answer = []

    # 현재 날짜를 일로 변경
    currentDays = calcuateToDays(today)

    # 각 약관 종류 별 만료일자
    expiredDays = {}

    for term in terms:
        termType, expirationPeriod = term.split()
        expiredDays[termType] = int(expirationPeriod) * DAY
        
    # 각 개인정보 수집 일자 만료 확인
    for i in range(len(privacies)):
        date, termType = privacies[i].split()
        privacyDays = calcuateToDays(date)

        if privacyDays + expiredDays[termType] - 1 < currentDays:
            answer.append(i + 1)

    return answer


def calcuateToDays(date: str):
    year, month, day = map(int, date.split("."))

    return year * 12 * DAY + month * DAY + day



today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]


today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

print(solution(today, terms, privacies))
