import sys
sys.stdin = open('19236_input.txt')

# Simulation + Brute Force(DFS)
# 상어가 먹을 수 있는 물고기 번호의 최대값 구하기
# 즉, 모든 경우에 대해서 끝까지 진행하고 최종적으로 판단해야 함
#

# 8방향
dr = (-1, -1, 0, 1, 1, 1, 0, -1)
dc = (0, -1, -1, -1, 0, 1, 1, 1)

def find_fish(idx, A):
    for i in range(4):
        for j in range(4):
            if A[i][j][0] == idx:
                # 위치 정보, 방향 리턴
                return [i, j, A[i][j][1]]
    return 0
#
def fish_move(A):
    for idx in range(1, 17):
        find = find_fish(idx, A)
        if find:
            r, c, d = find
            flag = 0
            while True:
                if flag:
                    break
                nr = r + dr[d]
                nc = c + dc[d]
                if not (0 <= nr < 4 and 0 <= nc < 4):    # 범위 벗어나거나
                    d = (d+1) % 8
                    continue
                if A[nr][nc][0] == 0:   # 상어가 있는 곳이면
                    d = (d+1) % 8
                    continue
                if A[nr][nc][0]:
                    # print(A[nr][nc][0], A[r][c][0])
                    # 번호 바꾸기
                    A[nr][nc][0], A[r][c][0] = A[r][c][0], A[nr][nc][0]
                    A[nr][nc][1], A[r][c][1] = d, A[nr][nc][1]
                    flag = 1
    return A

# 상어의 위치, 배열, 먹은 물고기 번호의 합
def dfs(r, c, arr, eat):
    global result
    A = [x[:] for x in arr]
    # 이동할 곳 없으면 상어는 집에 간다
    if not (0 <= r < 4 and 0 <= c < 4):
        result = max(result, eat)
        return
    eat += A[r][c][0]
    A[r][c][0] = 0      # 해당 위치의 물고기 먹기
    dir = A[r][c][1]
    # 물고기 이동
    fish_move(A)
    print('물고기 이동 끝')
    for aa in A:
        print(aa)
    # 상어 이동 - 맵의 크기가 4*4이므로 상어는 최대 3칸 이동 가능
    for i in range(1, 4):
        snr = r + dr[dir] * i
        snc = c + dc[dir] * i
        if not (0 <= snr < 4 and 0 <= snc < 4):     # 범위 벗어나면 집으로
            break
        if A[snr][snc][0] == 0:     # 물고기 없으면 넘어감
            continue
        fish = A[snr][snc][:]       # 물고기 있는 이동 위치 저장
        A[r][c] = []                # 원래 상어 자리 비우기
        A[snr][snc][0] = 0
        print(fish)


# main
raw = [[] for _ in range(4)]
for i in range(4):
    L = list(map(int, input().split()))
    for j in range(0, 7, 2):
        a = [L[j], L[j+1]-1]
        raw[i].append(a)
# print(raw)
result = float('-inf')
dfs(0, 0, raw, 0)