# from 11:13 to 12:05
# 52m
# 사소하게 변수 헷갈리지 말자! 변수 실수 아니었으면 30분 컷..

import sys
sys.stdin = open("14891_input.txt")
input = sys.stdin.readline

gears = [list(input().rstrip()) for _ in range(4)]
K = int(input())
for _ in range(K):
    num, dir = map(int, input().split())    # num : 톱니바퀴 번호, dir : 회전 방향(1: 시계, -1: 반시계)
    current = num-1
    temp = [0] * 4      # 돌아가야 할 톱니바퀴 표시
    temp[current] = dir

    # 오른쪽 방향 회전시킬 톱니바퀴 살피기
    for r in range(current+1, 4):
        if gears[r][6] != gears[r-1][2]:
            temp[r] = temp[r-1] * -1
        else:
            break
    # 왼쪽 방향 회전시킬 톱니바퀴 살피기
    for l in range(current-1, -1, -1):
        if gears[l][2] != gears[l+1][6]:
            temp[l] = temp[l+1] * -1
        else:
            break
    # 회전
    for i in range(4):
        if temp[i] == 1:
            gears[i] = [gears[i][-1]] + gears[i][:-1]
        elif temp[i] == -1:
            gears[i] = gears[i][1:] + [gears[i][0]]
ans = 0
for n in range(4):
    ans += int(gears[n][0]) << 1 * n
print(ans)