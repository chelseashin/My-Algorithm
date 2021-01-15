import sys
sys.stdin = open("1767_input.txt")

# 4방향
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def connect(r, c, d, depth):
    cnt = 0
    while True:
        r += dr[d]
        c += dc[d]
        if not (0 <= r < N and 0 <= c < N):
            return cnt
        if A[r][c]:     # 코어에 해당하거나 다른 전선이 연결된 자리라면
            return 0
        A[r][c] = 10 + depth   # 연결하는 부분 10+depth로 표시
        cnt += 1

def remove(r, c, d, depth):
    while True:
        r += dr[d]
        c += dc[d]
        if not (0 <= r < N and 0 <= c < N):
            return
        if A[r][c] != 10 + depth:
            return
        A[r][c] = 0      # 연결 해제한 부분 2로 표시


# 현재 체크한 코어 수, 전선 연결한 코어 수, 연결한 전선 길이의 합
def dfs(depth, connectedCores, connectedlength):
    global A, minLength, maxCores
    # 가지치기
    # 현재까지 연결한 코어 수 + 체크할 남은 코어 수와 합한 것이 연결한 최댓값보다 작다면 리턴
    if connectedCores + (coreCnt - depth) < maxCores:
        return

    if depth == coreCnt:
        if connectedCores < maxCores:   # 연결한 갯수가 최대 연결 갯수보다 이미 작으면
            return

        # 연결 갯수가 최대 연결 갯수보다 크다면
        if connectedCores > maxCores:
            maxCores = connectedCores
            minLength = connectedlength
        # 연결 갯수가 최대 연결 갯수와 같다면 최소 연결 길이 갱신
        elif connectedCores == maxCores:
            minLength = min(minLength, connectedlength)
        return

    sr, sc = coreLst[depth]
    for d in range(4):
        temp = connect(sr, sc, d, depth)    # 코어 위치, 방향 넘겨주면
        if temp:    # 연결 가능하면
            dfs(depth+1, connectedCores+1, connectedlength+temp)
        remove(sr, sc, d, depth)            # 연결하던 도중 끊긴 것들도 제거

    # 연결 실패하면
    dfs(depth+1, connectedCores, connectedlength)

# main
T = int(input())
for tc in range(T):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    coreLst = []    # 코어 위치 좌표 담기
    coreCnt = 0     # 코어 갯수
    for i in range(1, N-1):
        for j in range(1, N-1):
            if A[i][j]:
                coreLst.append((i, j))
                coreCnt += 1
    maxCores = 0                # 연결한 코어의 수 - 최댓값 갱신용
    minLength = float('inf')    # 전선 길이의 합 - 최솟값 갱신용
    dfs(0, 0, 0)
    print("#{} {}".format(tc+1, minLength))