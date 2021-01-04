import sys
sys.stdin = open("20057_input.txt")
input = sys.stdin.readline

# 좌 하 우 상
dr = (0, 1, 0, -1)
dc = (-1, 0, 1, 0)

# y 기준 날리는 모래 (위치, 비율) 리스트
weight = (0.01, 0.01, 0.07, 0.07, 0.02, 0.02, 0.1, 0.1, 0.05)
# 좌 하 우 상
move = [[(-1, 1), (1, 1), (-1, 0), (1, 0), (-2, 0), (2, 0), (-1, -1), (1, -1), (0, -2)],
        [(-1, -1), (-1, 1), (0, -1), (0, 1), (0, -2), (0, 2), (1, -1), (1, 1), (2, 0)],
        [(-1, -1), (1, -1), (-1, 0), (1, 0), (-2, 0), (2, 0), (-1, 1), (1, 1), (0, 2)],
        [(1, -1), (1, 1), (0, -1), (0, 1), (0, -2), (0, 2), (-1, -1), (-1, 1), (-2, 0)]]

def spread(r, c, d, sand):
    global A, res
    orgSand = sand
    for n in range(9):
        tr, tc = move[d][i]
        value = int(orgSand * weight[i])
        sand -= value
        nr = r + tr
        nc = c + tc
        if not (0 <= nr < N and 0 <= nc < N):
            res += value
            continue
        A[nr][nc] += value
    return sand

# main
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

r, c = N//2, N//2
d = -1
res = 0
for i in range(1, N):   # 이동 길이
    for j in range(2):  # 같은 길이 2개씩 반복
        d = (d + 1) % 4
        for k in range(i):  # 이동
            r = r + dr[d]
            c = c + dc[d]
            nr = r + dr[d]
            nc = c + dc[d]
            print((r, c), "=> 알파 위치", (nr, nc))
            # print(A[r][c], A[nr][nc])
            # 알파 위치가 격자 밖으로 나가면
            if not (0 <= nr < N and 0 <= nc < N):
                res += spread(r, c, d, A[r][c])
            else:
                A[nr][nc] += spread(r, c, d, A[r][c])

        print(i, j, d)
for a in A:
    print(a)