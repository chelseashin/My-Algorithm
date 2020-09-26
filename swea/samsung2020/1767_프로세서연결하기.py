import sys
sys.stdin = open('1767_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def connect(r, c, dir):
    line = 0
    while True:
        r += dr[dir]
        c += dc[dir]
        if not (0 <= r < N and 0 <= c < N):
            return line
        if raw[r][c]:
            return 0
        line += 1
        raw[r][c] = 1


# 현재 확인하는 코어 번호, 실제 연결한 코어의 수, 전선의 길이
def dfs(depth, cnt, length):
    global maxCnt, minLength, raw
    if depth == len(coreLst):
        if maxCnt <= cnt:
            if maxCnt < cnt:
                minLength = min(minLength, length)
            else:
                minLength = length
            maxCnt = cnt
        return

    r, c = coreLst[depth]
    R = [x[:] for x in raw]
    for d in range(4):
        temp = connect(r, c, d)
        if temp:
            dfs(depth+1, cnt+1, length+temp)
        raw = [x[:] for x in R]
    dfs(depth+1, cnt, length)

# main
T = int(input())
for tc in range(T):
    N = int(input())
    raw = [list(map(int, input().split())) for _ in range(N)]
    maxCnt = 0            # 최대 연결한 코어의 수
    minLength = float('inf')   # 전선 길의 최소 합
    coreLst = []
    for r in range(1, N-1):
        for c in range(1, N-1):
            if raw[r][c]:
                coreLst.append((r, c))
    dfs(0, 0, 0)
    print("#{} {}".format(tc+1, minLength))