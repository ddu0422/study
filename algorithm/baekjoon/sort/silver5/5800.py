import sys

k = int(sys.stdin.readline().rstrip())
classes = []
for _ in range(k):
    classes.append(list(map(int, sys.stdin.readline().rstrip().split())))


def solution(classes):
    for index, value in enumerate(classes):
        value = sorted(value[1:], reverse=True)
        max_gap = 0
        for i in range(len(value) - 1):
            max_gap = max(max_gap, value[i] - value[i + 1])

        print('Class {}'.format(index + 1))
        print('Max {}, Min {}, Largest gap {}'.format(value[0], value[-1], max_gap))


solution(classes)
