import sys
sys.stdin = open("17136_input.txt")

# testcase는 모두 맞음. 20%에서 틀림
# 재귀로 짤 필요가 있음

def dfs(sr, sc, size):
    global P, N, MIN, total, temp
    cnt = 0
    for i in range(size):
        for j in range(size):
            if not (0 <= sr+i < N and 0 <= sc+j < N):
                # continue
                return
            if P[sr+i][sc+j] == 0:
                return
            if P[sr+i][sc+j]:
                cnt += 1
    if cnt == size * size:
        temp = 1
        for i in range(size):
            for j in range(size):
                P[sr+i][sc+j] = 0
    return

N = 10
P = [list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')
check = [0] * 6   # 색종이 크기별 사용 횟수를 List로 만듦
total = 0
# 색종이 5*5 ~ 1*1 크기 순으로 탐색
for x in range(5, 0, -1):
    for i in range(N):
        for j in range(N):
            if P[i][j]:
                if check[x] < 5:
                    temp = 0
                    dfs(i, j, x)
                    check[x] += temp
                    total += temp
                else:    # 사용 횟수가 5회 넘어갔을 때
                    if x != 1:
                        continue
                    else: MIN = -1

if total < MIN:
    MIN = total
if MIN == float('inf'):
    MIN = 0

print(MIN)