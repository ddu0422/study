"""
입력
00011000

출력
1
"""
str = input()
current = str[0]

zero_count = 0
one_count = 0

for s in str[1:]:
  if current != s:
    if current == '0':
      zero_count += 1
    elif current == '1':
      one_count += 1

  current = s

if current == '0':
  zero_count += 1
elif current == '1':
  one_count += 1

print(min(zero_count, one_count))