import sys
sys.stdin = open('14891_input.txt')

from collections import deque

# 양쪽 톱니바퀴만 생각해서 동작하는 dfs로 구현
# deque의 rotate 명령어로 회전 구현

def dfs(pos, dir):
    turn[pos] = 1
    if pos < 3:
        if gears[pos][2] != gears[pos+1][6] and not turn[pos+1]:
            dfs(pos+1, -dir)
    if (pos > 0):
        if gears[pos][6] != gears[pos-1][2] and not turn[pos-1]:
            dfs(pos-1, -dir)
      # 1: 시계방향, -1: 반시계방향
    if dir == 1:
        gears[pos].rotate()
    else:
        gears[pos].rotate(-1)

# main
gears = [deque(input()) for _ in range(4)]
K = int(input())
rotation = [list(map(int, input().split())) for _ in range(K)]

for num, dir in rotation:
    turn = [0] * 4
    dfs(num-1, dir)

score = 0
for i in range(4):
    if gears[i][0] == '1':
        score += 1 << i
# score = int(gears[0][0]) * 1 + int(gears[1][0]) * 2 + int(gears[2][0]) * 4 + int(gears[3][0]) * 8
print(score)