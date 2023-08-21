"""
뉴클레오티드: A,T,G,C

TAACTGCCGAT
=> AGCAT / GGAAT

1, 3번째가 다르므로
Hamming Distance = 2
s1 ~ sn까지 Hamming Distance의 합이 가장 작은 새 DNA s를 구하시오.
=> s1 ~ sn 중 각 자리마다 가장 많이 나온 알파벳을 찾으면 됨.

=== example === 
TATGATAC
TAAGCTAC
AAAGATCC
TGAGATAC
TAAGATGT

0: T(4)
1: A(4)
2: A(4)
3: G(5)
4: A(4)
5: T(5)
6: A(3)
7: C(4)
=> TAAGATAC

TAAGATAC와 각 DNA의 Hemming Distance
[1, 1, 1, 0, 1, 0, 2, 1] => 7

즉, n번째 index에 어떤 DNA(alpha)가 몇 개(count) 씩 나왔는지 찾아야한다.
"""
import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().rstrip().split())
text = []
for _ in range(n):
    text.append(sys.stdin.readline().rstrip())


def solution(text):
    dna = ''
    answer = 0
    
    for i in range(len(text[0])):
        temp = []
        for j in range(len(text)):
            temp.append(text[j][i])
        alpha, count = sorted(Counter(temp).items(), key=lambda x: (-x[1], x[0]))[0]

        dna += alpha
        answer += (len(text) - count)
    
    return [dna, answer]

dna, answer = solution(text)
print(dna, answer, sep="\n")
