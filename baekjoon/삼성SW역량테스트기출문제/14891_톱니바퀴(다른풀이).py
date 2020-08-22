import sys
sys.stdin = open('14891_input.txt')

# 직관적으로 현 위치 기준으로 오른쪽, 왼쪽을 나누어
# 회전하는 바퀴와 방향을 기록하는 direction 변수를 만듦
# 리스트 슬라이싱을 이용하여 회전 구현
# 비트 연산 활용하여 합계 점수 구하기

# main
gears = [list(input()) for _ in range(4)]
K = int(input())
rotation = [list(map(int, input().split())) for _ in range(K)]

for num, dir in rotation:
    direction = [0] * 4
    direction[num-1] = dir
    # 오른쪽 방향
    for i in range(num-1, 3):
        if gears[i][2] != gears[i+1][6]:
            direction[i+1] = -direction[i]
    # 왼쪽 방향
    for i in range(num-1, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            direction[i-1] = -direction[i]
    # print(direction)

    # 회전
    for i in range(4):
        # 시계방향
        if direction[i] == 1:
            gears[i] = [gears[i][-1]] + gears[i][:-1]
        # 반시계방향
        elif direction[i] == -1:
            gears[i] = gears[i][1:] + [gears[i][0]]
# print(gears)

score = 0
for i in range(4):
    if gears[i][0] == '1':
        score += (1 << i)
print(score)