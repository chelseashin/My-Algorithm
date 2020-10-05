import sys
sys.stdin = open('5656_input.txt')
from collections import deque

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def gravity(chk):
    cnt = 0         # chk에 담긴 정보로 터트린 갯수
    for i in range(H):
        for j in range(W):
            if chk[i][j] and A[i][j]:
                A[i][j] = 0
                cnt += 1
    # 중력
    for c in range(W):
        L = []
        for r in range(H):
            if A[r][c]:
                L.append(A[r][c])
                A[r][c] = 0
        row = H-1
        while L:
            A[row][c] = L.pop()
            row -= 1
    return cnt

# 지울 영역 check에 표시
def bfs(sr, sc, check):
    Q = deque([(sr, sc)])
    while Q:
        r, c = Q.popleft()
        power = A[r][c]
        if power == 0:
            continue
        check[r][c] = 1
        for d in range(4):
            for p in range(1, power):
                nr = r + dr[d] * p
                nc = c + dc[d] * p
                if not (0 <= nr < H and 0 <= nc < W):
                    continue
                if not A[nr][nc]:
                    continue
                if check[nr][nc]:
                    continue
                Q.append((nr, nc))
                check[nr][nc] = 1

# 사용한 구슬 갯수, 깬 벽돌 갯수
def dfs(depth, bricks):
    global MIN, A
    if depth == N or not bricks:
        MIN = min(MIN, bricks)
        return
    arr = [a[:] for a in A]
    for c in range(W):
        for r in range(H):
            if A[r][c]:
                # bomb 함수에서 깰 수 있는 벽돌 갯수 리턴
                check = [[0] * W for _ in range(H)]
                bfs(r, c, check)
                dfs(depth+1, bricks-gravity(check))
                A = [a[:] for a in arr]
                break

# main
T = int(input())
for tc in range(T):
    N, W, H = map(int, input().split())
    A = []
    b = 0      # 맵에 있는 전체 벽돌의 수
    for h in range(H):
        A.append(list(map(int, input().split())))
        for w in range(W):
            if A[h][w]:
                b += 1

    MIN = float('inf')
    dfs(0, b)
    print("#{} {}".format(tc+1, MIN))

    # 1 12
    # 2 27
    # 3 4
    # 4 8
    # 5 0