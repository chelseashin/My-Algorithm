# 20:10 start
# 21:09 시간초과 - 일일이 구현하면 안 됨..

from sys import stdin
input = stdin.readline

# 상, 우
dr = (-1, 0)
dc = (0, 1)
# 좌, 상, 좌상
lr = (0, -1, -1)
lc = (-1, 0, -1)

def growLarva():
    r, c, d = M-1, 0, 0
    check[r][c] = order[0]
    honeycomb[r][c] += check[r][c]
    for i in range(1, 2*M-1):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < M and 0 <= nc < M):
            d += 1
            nr = r + dr[d]
            nc = c + dc[d]
        check[nr][nc] = order[i]
        honeycomb[nr][nc] += order[i]
        r, c = nr, nc
    for r in range(1, M):
        for c in range(1, M):
            maxGrowth = 0
            for d in range(3):
                nr = r + lr[d]
                nc = c + lc[d]
                maxGrowth = max(maxGrowth, check[nr][nc])
            check[r][c] = maxGrowth
            honeycomb[r][c] += check[r][c]

# main
M, N = map(int, input().split())
honeycomb = [[1] * M for _ in range(M)]
for _ in range(N):
    A = list(map(int, input().split()))
    order = []
    for i in range(3):
        order.extend([i] * A[i])
    check = [[-1] * M for _ in range(M)]
    growLarva()
    # print("모든 애벌레 자라기 완료")
    # for row in check:
    #     print(row)
    
for honey in honeycomb:
    print(*honey)