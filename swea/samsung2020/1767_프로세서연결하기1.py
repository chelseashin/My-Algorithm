import sys
sys.stdin = open('1767_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def connect(sr, sc, dir):
    count = 0
    r, c = sr, sc
    while True:
        r += dr[dir]
        c += dc[dir]
        if not (0 <= r < N and 0 <= c < N):     # 벽 만나면 연결 길이 리턴
            return count
        if raw[r][c]:       # 도중에 값 만나면 연결 불가
            return 0
        count += 1
        raw[r][c] = 2

# 현재 depth, 실제 연결 갯수, 전선 길이
def dfs(depth, cnt, length):
    global max_cnt, min_length, raw
    if depth == C:      # 끝까지 도달했을 때 확인
        if cnt > max_cnt:
            max_cnt = cnt
            min_length = length
        elif cnt == max_cnt:
            min_length = min(min_length, length)
        return
    R = [x[:] for x in raw]
    r, c = cores[depth]     # 현재 확인하는 코어의 좌표
    for d in range(4):
        temp = connect(r, c, d)     # 연결했을 때 길이
        if temp:
            dfs(depth+1, cnt+1, length+temp)
        raw = [x[:] for x in R]
    dfs(depth+1, cnt, length)       # 4방향 모두 연결하지 못한 경우

# main
T = int(input())
for tc in range(T):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    min_length = float('inf')      # 전선의 최소 길이
    max_cnt = 0     # 최대 연결한 코어의 수
    cores = []      # 코어의 위치 좌표
    for r in range(1, N-1):
        for c in range(1, N-1):
            if raw[r][c]:
                cores.append((r, c))
    C = len(cores)
    dfs(0, 0, 0)

    print("#{} {}".format(tc+1, min_length))