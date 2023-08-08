def solution(participant, completion):
    attendees = {name: 0 for name in participant}

    for name in participant:
        attendees[name] += 1
    
    for name in completion:
        attendees[name] -= 1

    return next(index for index, value in attendees.items() if value == 1)


from collections import Counter

def solution_refactor(participant, completion):
    return list((Counter(participant) - Counter(completion)).elements())[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))
print(solution_refactor(participant, completion))