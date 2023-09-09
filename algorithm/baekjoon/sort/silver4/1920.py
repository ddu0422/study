import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
b = list(map(int, sys.stdin.readline().rstrip().split()))


def solution(a, b):
    result = []
    a = sorted(a)

    for value in b:
        if binary_search(a, value, 0, len(a) - 1) != None:
            result.append(1)
        else:
            result.append(0)

    return result


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    


print(*solution(a, b), sep="\n")
