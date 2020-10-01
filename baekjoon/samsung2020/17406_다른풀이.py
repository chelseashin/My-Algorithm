import sys
sys.stdin = open('17406_input.txt')
input = sys.stdin.readline

# 우 하 좌 상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def rotate(r, c, k, B):
    for i in range(k+1):
        sr, sc = r-i, c-i
        temp = B[sr][sc]
        for d in range(4):
            for j in range(i*2):
                nr = sr + dr[d]
                nc = sc + dc[d]
                B[nr][nc], temp = temp, B[nr][nc]
                sr, sc = nr, nc
    # return B

def perm(depth):
    global result, cal
    if depth == K:
        A = [x[:] for x in raw]
        # 회전 연산
        for j in order:
            r, c, s = cal[j]
            rotate(r-1, c-1, s, A)
        # 배열 각 행의 합 중 최솟값
        for n in range(N):
            result = min(result, sum(A[n]))

    for i in range(K):
        if visit[i]:
            continue
        visit[i] = 1
        order.append(i)
        perm(depth+1)
        order.pop()
        visit[i] = 0

N, M, K = map(int, input().split())
raw = [list(map(int, input().split())) for _ in range(N)]
cal = [list(map(int, input().split())) for _ in range(K)]

result = float('inf')
order = []
visit = [0] * K
perm(0)
print(result)