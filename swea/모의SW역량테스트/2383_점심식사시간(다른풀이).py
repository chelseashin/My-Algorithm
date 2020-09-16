import sys
sys.stdin = open('2383_input.txt')

# comb 부분 조금 다름

def calc(selected):
    global result
    waiting = [[], []]
    for i in range(P):
        stairNum = selected[i]
        pr, pc = person[i]          # 사람 위치
        sr, sc = stairs[stairNum]   # 선택한 계단의 좌표
        time = abs(pr-sr) + abs(pc-sc) + 1
        waiting[stairNum].append(time)
    # print(waiting)

    second = 0
    stair = [[], []]
    while len(max(*stair)) + len(max(*waiting)):
        second += 1     # 시간 흐름
        if second >= result:
            return
        # 계단별로 처리
        for i in range(2):
            for s in reversed(range(len(stair[i]))):
                if second >= stair[i][s]:
                    stair[i].pop(s)
            for w in reversed(range(len(waiting[i]))):
                if len(stair[i]) < 3 and second >= waiting[i][w]:
                    waiting[i].pop(w)
                    sr, sc = stairs[i]
                    down = A[sr][sc]
                    stair[i].append(second + down)
    result = min(result, second)

def comb(depth):
    if depth == P:
        calc(select)
        # print(select)
        return
    comb(depth+1)
    select[depth] = 1
    comb(depth+1)
    select[depth] = 0

# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    S, P = 0, 0
    stairs, person = [], []
    for i in range(N):
        for j in range(N):
            if A[i][j] > 1:
                stairs.append((i, j))
                S += 1
            elif A[i][j] == 1:
                person.append((i, j))
                P += 1
    select = [0] * P
    comb(0)
    print("#{} {}".format(tc+1, result))


a = [9, 8, 3, 2, 5]
# b = [9, 8, 7]
# print(max(a, b))
print(sorted(a, reverse=True))