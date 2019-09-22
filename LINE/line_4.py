# https://line-codingtest.channel.io
# 가지치기 해야하나?

import sys
sys.stdin = open('line_4.txt')

N = int(input())
L = list(map(int, input().strip().split(' ')))
MAX = 0
count = 0

for i in range(len(L)):
    if L[i]:
        count = 0
    else:
        count += 1

    if count:
        if count > MAX:
            MAX = count

print(MAX//2+1)