import sys
sys.stdin = open("17136_input.txt")


def dfs(sr, sc, size):
    global P, N, MIN, total, temp
    if temp > 5:
        total = -1
        return
    cnt = 0
    for i in range(size):
        for j in range(size):
            if not (0 <= sr+i < N and 0 <= sc+j < N):
                continue
            if P[sr+i][sc+j] == 0:
                return
            if P[sr+i][sc+j]:
                cnt += 1
    if cnt == size * size:
        temp += 1
        for i in range(size):
            for j in range(size):
                P[sr+i][sc+j] = 0
    return

N = 10
P = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')
check = [0] * 6
total = 0
for i in range(N):
    for j in range(N):
        if P[i][j]:
            for x in range(5, 0, -1):
                if check[x] < 5:
                    temp = 0
                    dfs(i, j, x)
                    check[x] += temp
                    total += temp
                else:
                    if x != 1:
                        continue
                    else: MIN = -1
# total = sum(check)
if total < MIN:
    MIN = total
if MIN == float('inf'):
    MIN = 0

print(MIN)