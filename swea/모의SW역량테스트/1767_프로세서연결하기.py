import sys
sys.stdin = open('1767_input.txt')

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def runProcessor(pr, pc, d, depth):
    cnt = 0
    while True:
        pr += dr[d]
        pc += dc[d]
        if not (0 <= pr < N and 0 <= pc < N):   # 전원 만나면 길이 리턴
            return cnt
        if raw[pr][pc]:     # 길 막혔으면 길이 0 리턴
            return 0
        cnt += 1
        raw[pr][pc] = 10 + depth

def cleanLine(pr, pc, d, depth):
    while True:
        pr += dr[d]
        pc += dc[d]
        if not (0 <= pr < N and 0 <= pc < N):
            return
        if raw[pr][pc] != 10 + depth:
            return
        raw[pr][pc] = 0

def dfs(depth, length, core):
    global core_cnt, max_cores, min_length
    if depth == core_cnt:
        if core == max_cores:
            min_length = min(min_length, length)
        elif core > max_cores:
            max_cores = core
            min_length = length
        return
    r, c = cores[depth]
    for i in range(4):      # 같은 depth에서 4방향 탐색
        line_cnt = runProcessor(r, c, i, depth)
        if line_cnt:        # 전원에 연결하면 다음 코어 연결 시도
            dfs(depth+1, length+line_cnt, core+1)
        cleanLine(r, c, i, depth) # 연결 못했다면 시도하던 연결선 제거
    dfs(depth+1, length, core)

# main
T = int(input())
for tc in range(T):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    max_cores = float('-inf')
    min_length = float('inf')

    cores = []
    core_cnt = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            if raw[i][j]:
                cores.append((i, j))
                core_cnt += 1


    # 연결 확인한 코어, 현재 전선의 길이, 코어의 수
    dfs(0, 0, 0)
    # print(raw)
    print("#{} {}".format(tc+1, min_length))