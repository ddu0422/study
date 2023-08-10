from datetime import datetime


def solution(a, b):
    return ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'][int(datetime(2016, a, b).date().strftime('%w'))]


a, b = 5, 24
print(solution(a, b))