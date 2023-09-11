import sys


def solution(note1, note2):
    note1 = sorted(note1)
    result = []

    for target in note2:
        if binary_search(note1, target, 0, len(note1) - 1) != None:
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



t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    note1 = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    note2 = list(map(int, sys.stdin.readline().rstrip().split()))
    print(*solution(note1, note2), sep='\n')
