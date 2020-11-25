import sys
sys.stdin = open("20055_input.txt")

# 로봇은 올라가는 위치에만 땅에서 올라가고,
# 내려가는 위치에서만 땅으로 내려갈 수 있다.
# 내려가는 위치에 로봇이 있는 경우 로봇은 반드시 땅으로 내려가야 한다.

from collections import deque
N, K = map(int, input().split())
belt = list(map(int, input().split()))
check = [0] * (2 * N)

robot = deque()
zeroCnt = 0
time = 0
while True:
    time += 1
    belt = belt[-1:] + belt[:-1]
    check = check[-1:] + check[:-1]
    if check[N - 1]:
        check[N - 1] = 0
    qlen = len(robot)
    for _ in range(qlen):
        rx = robot.popleft()
        rx += 1
        if rx == (N-1):
            continue
        nx = rx + 1
        if not check[nx] and belt[nx] > 0:
            if nx == (N-1):
                check[rx] = 0
            else:
                robot.append(nx)
                check[rx] = 0
                check[nx] = 1
            belt[nx] -= 1
            if belt[nx] == 0:
                zeroCnt += 1
        else:
            robot.append(rx)
    if belt[0] > 0 and not check[0]:
        robot.append(0)
        check[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            zeroCnt += 1
    if zeroCnt >= K:
        print(time)
        break