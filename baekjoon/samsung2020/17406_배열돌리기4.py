import sys
sys.stdin = open('17406_input.txt')
input = sys.stdin.readline

# 우 하 좌 상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def rotate(r, c, k, A):
    sr, sc = r-k, c-k
    er, ec = r+k, c+k
    while True:
        if er <= sr and ec <= sc:   # 종료조건 : 우하단 좌표가 좌상단 좌표보다 작거나 같아질 때까지
            break
        dir = 0
        r, c, start = sr, sc, A[sr][sc]
        while True:
            if dir == 4:
                break
            nr = r + dr[dir]
            nc = c + dc[dir]
            # 범위 넘어가면 방향 전환
            if not (sr <= nr <= er and sc <= nc <= ec):
                dir += 1
                continue
            A[nr][nc], start = start, A[nr][nc]
            r, c = nr, nc
            # 시작점에 도착하면
            if r == sr and c == sc:
                sr += 1
                sc += 1
                er -= 1
                ec -= 1
    return A

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
            temp = sum(A[n])
            result = min(result, temp)

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