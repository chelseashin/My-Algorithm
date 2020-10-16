import sys
sys.stdin = open('2383_input.txt')

def stairDown(waiting):
    global result
    time = 0
    cnt = 0     # 계단 완전히 내려간 인원
    down = [[], []]
    while True:
        if time >= result:
            return
        for i in range(2):  # 계단별로 작업 처리
            for s in range(len(down[i])-1, -1, -1):
                if time == down[i][s]:
                    down[i].pop(s)
                    cnt += 1
            for w in range(len(waiting[i])-1, -1, -1):
                if len(down[i]) < 3 and time >= waiting[i][w]:
                    waiting[i].pop(w)
                    sr, sc = stairs[i]
                    down[i].append(time+A[sr][sc])
        if cnt == P:
            break
        time += 1
    result = min(result, time)

def comb(depth, k, goal):
    if depth == goal:
        arrive = [[], []]
        for j in range(P):
            if not selected[j]:
                dis = abs(stairs[0][0]-people[j][0]) + abs(stairs[0][1]-people[j][1])
                arrive[0].append(dis+1)
            else:
                dis = abs(stairs[1][0]-people[j][0]) + abs(stairs[1][1]-people[j][1])
                arrive[1].append(dis+1)
        stairDown(arrive)
        return
    for i in range(k, P):
        if selected[i]:
            continue
        selected[i] = 1
        comb(depth+1, i+1, goal)
        selected[i] = 0

# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1:
                people.append((i, j))
            elif 2 <= A[i][j] <= 10:
                stairs.append((i, j))
    P = len(people)

    selected = [0] * P
    for p in range(P+1):
        comb(0, 0, p)
    print("#{} {}".format(tc+1, result))
    # 1 9
    # 2 8
    # 3 9
    # 4 7
    # 5 8
    # 6 8
    # 7 11
    # 8 11
    # 9 18
    # 10 12