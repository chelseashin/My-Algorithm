import sys
sys.stdin = open("2105_input.txt")

# 좌하, 우하, 우상, 좌상
dr = [1, 1, -1, -1]
dc = [-1, 1, 1, -1]

def check(r, c):
    global result, cafe
    result_arr = []
    r_range = parr[0]
    c_range = parr[1]
    for i in range(4):
        if i % 2:
            for i in range(1, r_range):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N):
                    return
                if cafe[nr][nc] in result_arr:
                    return
                result_arr.append(cafe[nr][nc])
        else:
            for j in range(1, c_range):
                nr = r + dr[j]
                nc = c + dc[j]
                if not (0 <= nr < N and 0 <= nc < N):
                    return
                if cafe[nr][nc] in result_arr:
                    return
                result_arr.append(cafe[nr][nc])
    if result < len(result_arr):
        result = len(result_arr)

def perm(n, r, c):
    if n == 2:
        flag = 1
        for z in parr:
            flag *= z
        if flag <= result:
            return
        else:
            check(r, c)
    else:
        for i in range(2, N):
            parr[n] = i
            perm(n+1, r, c)
            # parr[n] = 0

T = int(input())
for tc in range(T):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    result = -1
    parr = [0] * 2
    for r in range(N):
        for c in range(N):
            perm(0, r, c)

    print("#{} {}".format(tc+1, result))