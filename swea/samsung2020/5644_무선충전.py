import sys
sys.stdin = open('5644_input.txt')
from collections import deque

# 상 우 하 좌
dr = (0, -1, 0, 1, 0)
dc = (0, 0, 1, 0, -1)

def bfs(i, sr, sc, dis, p):
    visited = [[-1] * N for _ in range(N)]
    visited[sr][sc] = 0
    Q = deque([(sr, sc)])
    while Q:
        qlen = len(Q)
        for _ in range(qlen):
            r, c = Q.popleft()
            if visited[r][c] == dis+1:
                return
            A[r][c].append([p, i+1])
            for d in range(1, 5):
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if visited[nr][nc] >= 0:
                    continue
                visited[nr][nc] = visited[r][c] + 1
                Q.append((nr, nc))
    
# main
T = int(input())
for tc in range(T):
    N = 10
    A = [[[] for _ in range(N)] for _ in range(N)]
    M, BC = map(int, input().split())
    info_A = list(map(int, input().split()))
    info_B = list(map(int, input().split()))
    for idx in range(BC):
        x, y, C, P = map(int, input().split())
        bfs(idx, y-1, x-1, C, P)
    for i in range(10):
        for j in range(10):
            A[i][j].sort(reverse=True)    # 내림차순

    result = 0  # 모든 사용자가 충전한 양의 합의 최댓값
    ar, ac = 0, 0
    br, bc = 9, 9
    for m in range(M+1):    # 시간에 따라
        # a, b = 0, 0
        # A 있고 B 없으면 A만 더함
        if A[ar][ac] and not A[br][bc]:
            result += A[ar][ac][0][0]
        # B 있고 A 없으면 B만 더함
        elif A[br][bc] and not A[ar][ac]:
            result += A[br][bc][0][0]
        # A, B 모두 값이 있고
        elif A[ar][ac] and A[br][bc]:
            if A[ar][ac][0][1] != A[br][bc][0][1]:  # 번호 다르면 각각 더함
                result += A[ar][ac][0][0] + A[br][bc][0][0]
            else:   # 번호 같으면 각각의 두 번째 수를 비교하여 큰 값을 더함
                temp = 0
                if len(A[ar][ac]) > 1:
                    temp = A[ar][ac][1][0]
                if len(A[br][bc]) > 1:
                    temp = max(temp, A[br][bc][1][0])
                result += A[ar][ac][0][0] + temp
        if m == M:
            break
        ad = info_A[m]
        ar += dr[ad]
        ac += dc[ad]
        bd = info_B[m]
        br += dr[bd]
        bc += dc[bd]
    print("#{} {}".format(tc+1, result))

    # 1 1200
    # 2 3290
    # 3 16620
    # 4 40650
    # 5 52710