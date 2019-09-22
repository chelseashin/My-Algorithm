# https://line-codingtest.channel.io

import sys
sys.stdin = open('line_3.txt')

N = int(input())

total = 1
L = []
for n in range(N):
    go, turn = map(int, input().strip().split(' '))
    # print(go, turn)

    flag = 0
    for i in range(go, turn):
        if i not in L:
            L.append(i)
        else:
            flag = 1
            L.append(i)
    if flag == 1:
        total += 1

print('total', total)
