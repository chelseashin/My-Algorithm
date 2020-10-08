import sys
sys.stdin = open('5650_input.txt')

# 시뮬레이션 문제

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
rev = (1, 0, 3, 2)

changeDir = [(),
             (1, 3, 0, 2),
             (3, 0, 1, 2),
             (2, 0, 3, 1),
             (1, 2, 3, 0),
             (1, 0, 3, 2)]

def move(r, c, d):
    global wormholes
    cnt = 0
    nr = r + dr[d]
    nc = c + dc[d]
    while True:
        if not (0 <= nr < N and 0 <= nc < N):
            cnt += 1
            d = rev[d]
            nr += dr[d]
            nc += dc[d]
        # 시작점에 도착하거나 블랙홀이면
        if (nr == r and nc == c) or A[nr][nc] == -1:
            break
        elif 1 <= A[nr][nc] <= 5:
            cnt += 1
            d = changeDir[A[nr][nc]][d]
        elif 6 <= A[nr][nc] <= 10:
            nr, nc = wormholes[(nr, nc)]
        nr += dr[d]
        nc += dc[d]
    return cnt

# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    wormholes = dict()  # 웜홀 pair 정보 저장
    visited = [0] * 11
    for i in range(N):
        for j in range(N):
            if 6 <= A[i][j] <= 10:
                if not visited[A[i][j]]:
                    visited[A[i][j]] = (i, j)
                else:
                    wormholes[visited[A[i][j]]] = (i, j)
                    wormholes[(i, j)] = visited[A[i][j]]

    score = float('-inf')
    for r in range(N):
        for c in range(N):
            if not A[r][c]:

                for d in range(4):
                    temp = move(r, c, d)
                    score = max(score, temp)
    print("#{} {}".format(tc+1, score))