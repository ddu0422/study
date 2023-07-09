def solution(s, skip, index):
    answer = ''

    for alpha in s:
        origin = ord(alpha)
        
        for _ in range(1, index + 1):
            origin += 1

            if origin > ord('z'):
                origin -= 26

            while chr(origin) in skip:
                origin += 1

                if origin > ord('z'):
                    origin -= 26

        answer += chr(origin)

    return answer

s = "aukksz"
# s = "az"
skip = "wbqd"
index = 5

print(solution(s, skip, index))