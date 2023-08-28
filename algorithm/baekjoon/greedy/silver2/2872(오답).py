"""
책을 탑처럼 쌓아놓고 있다.
책을 알파벳 순서대로 정렬하려고 한다.
사전 순으로 앞에 있는 책은 가장 위에 놓고 가장 뒤에 있는 책은 가장 밑에 놓아야한다.

- 책을 정렬할 때 사용할 수 있는 방법은 책 하나를 뺀 다음, 가장 위에 놓는 것이다.

1
3
4
2
5

2
3
4
1
5

2
3
4
5
1

1
3
2
5
6
4
"""
import sys
n = int(sys.stdin.readline().rstrip())
books = []
for _ in range(n):
    books.append(int(sys.stdin.readline().rstrip()))


def solution(books):
    max_book = max(books)
    index = books.index(max_book)
    # 가장 큰 숫자의 책보다 오른쪽에 있는 책의 개수
    answer = len(books) - 1 - index

    # 가장 큰 숫자부터 작은 숫자로 갈 때까지 1차이가 나지 않는 책들을 구하기
    for book in books[:index][::-1]:
        if book == max_book - 1:
            max_book = book
        else:
            answer += 1
    
    return answer


print(solution(books))
