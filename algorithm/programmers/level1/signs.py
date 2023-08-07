def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] else -absolutes[i] for i in range(len(signs))])


absolutes = [4, 7 ,12]
signs = [True, False, True]
print(solution(absolutes, signs))