# from 11:12 to 12:45
# 12:25 마지막 tc만 안 맞음..
# 1h 33m
# check 함수에서 c의 범위를 잘못 설정함. N이 아니라 M으로 고치고 통과
# check 함수에서 벽 만날 때 chk 리턴하는 것이 아니라 해당 방향에서만 break 해줘야 함.
# 4방향 모두 본 후 chk 리턴

import sys
input = sys.stdin.readline

# 상 좌 하 우
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

cctv_dir = [[],
            [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)],
            [(1, 0, 1, 0), (0, 1, 0, 1)],
            [(1, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 1), (1, 0, 0, 1)],
            [(1, 1, 1, 0), (1, 1, 0, 1), (1, 0, 1, 1), (0, 1, 1, 1)],
            [(1, 1, 1, 1)]]

# 시작 위치, 방향, cctv 번호
def check(sr, sc, direction):
    chk = 0
    for d in range(4):
        if direction[d]:
            r, c = sr, sc
            while True:
                r += dr[d]
                c += dc[d]
                if not (0 <= r < N and 0 <= c < M) or raw[r][c] == 6:   # 벽이면
                    break
                if raw[r][c] == 0:
                    chk += 1        # 빈 공간 감시할 때만 +1
                    raw[r][c] = 9
                elif 1 <= raw[r][c] <= 5:
                    continue
    return chk

# 현재 확인하고 있는 cctv 갯수, 감시한 칸의 수
def dfs(depth, cnt):
    global space, MIN, raw
    if depth == cctv_cnt:
        MIN = min(MIN, space-cnt)
        return
    cr, cc, cctv_num = cctv_info[depth]     # 현재 확인하는 함수
    A = [x[:] for x in raw]
    for direction in cctv_dir[cctv_num]:
        temp = check(cr, cc, direction)   # 감시한 칸의 수 리턴
        dfs(depth+1, cnt+temp)
        raw = [a[:] for a in A]

# main
N, M = map(int, input().split())
raw = []
cctv_info = []
cctv_cnt = 0
space = 0
for i in range(N):
    raw.append(list(map(int, input().split())))
    for j in range(M):
        if 1 <= raw[i][j] <= 5:
            cctv_info.append((i, j, raw[i][j]))    # cctv (위치, 번호) 정보 저장
            cctv_cnt += 1
        elif raw[i][j] == 0:
            space += 1
MIN = space
dfs(0, 0)
print(MIN)