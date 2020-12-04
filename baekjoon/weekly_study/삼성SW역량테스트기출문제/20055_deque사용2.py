import sys
sys.stdin = open("20055_input.txt")

# 내가 놓친 조건. 조건 하나로 답이 틀릴 수 있으니 문제 항상 잘 읽기
# 로봇은 올라가는 위치에만 땅에서 올라가고,
# 내려가는 위치에서만 땅으로 내려갈 수 있다.
# 내려가는 위치에 로봇이 있는 경우 로봇은 반드시 땅으로 내려가야 한다.

from collections import deque

N, K = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque([0] * (2 * N))

zeroCnt = 0
time = 0
while True:
    # 1
    belt.rotate(1)
    robot.rotate(1)
    robot[N-1] = 0  # 내려가는 위치에 로봇 삭제

    # 2. 로봇 이동할 수 있을 경우 이동
    for i in range(N-2, -1, -1):
        # 이동할 위치의 내구도가 1 이상, 로봇 없을 경우
        if robot[i]:
            if belt[i+1] > 0 and robot[i+1] == 0:
                belt[i+1] -= 1
                robot[i+1] = 1
                robot[i] = 0
                if belt[i+1] == 0:
                    zeroCnt += 1
    robot[N-1] = 0

    # 3. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if robot[0] == 0 and belt[0] > 0:
        belt[0] -= 1
        robot[0] = 1
        if belt[0] == 0:
            zeroCnt += 1
    # print(time, belt, robot)
    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 종료
    time += 1
    if zeroCnt >= K:
        print(time)
        break