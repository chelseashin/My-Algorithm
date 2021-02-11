# from 10:30 to ???
# 11%에서 틀림.. 반례도 다 맞음,, 오늘은 여기까지..
# 이제 11%에서 시간 초과.....

import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 탐색 시작열과 마지막열 인자로 넣으면 떨어질 수 있는 가장 작은 차이를 리턴
def down(left, right):
    min_gap = R
    for c in range(left, right+1):
        flag = False
        cnt = 0
        for r in range(R):
            if visited[r][c] == 2:
                flag = True
                cnt = 0
            elif flag and visited[r][c] == 0 and cave[r][c] == '.':
                cnt += 1
            elif visited[r][c] == 1:
                break
        min_gap = min(min_gap, cnt)
    return min_gap

def bfs(sr, sc, num):
    global visited, cave
    visited[sr][sc] = num
    Q = deque([(sr, sc)])
    minerals = [(sr, sc)]
    downLst = []
    while Q:
        r, c = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if cave[nr][nc] == 'x' and not visited[nr][nc]:
                visited[nr][nc] = num
                Q.append((nr, nc))
                if num == 2 and cave[nr+1][nc] == '.':
                    downLst.append((nr, nc))
                    minerals.append((nr, nc))
    if num == 2:
        gap = down(downLst)     # 떨어질 수 있는 최소 차이
        for i in range(R - 2, -1, -1):
            for j in range(C):
                # 클러스터 내린 상태 A에 반영
                if cave[i][j] == 'x' and visited[i][j] == 2:
                    cave[i][j] = '.'          # 미네랄의 새 위치 담으면서 빈 공간으로 만들어주기
                    visited[i][j] = 0
                    cave[i+gap][j] = 'x'    # 미네랄 새 위치에 뿌리기
                    visited[i+gap][j] = 1

def down(downLst):
    global visited
    k, flag = 1, 0  # k 크기 1씩 늘려가며(클러스터로부터 떨어질 수 있는 최대 차이를 찾기 위해)
    while True:
        for r, c in downLst:
            if r + k == R - 1:  # 땅을 만나거나
                flag = 1
                break
            if cave[r+k+1][c] == 'x' and not visited[r+k+1][c]:  # 다른 미네랄 만나면
                flag = 1
                break
        if flag:  # 그 때가 떨어질 수 있는 최대 k 값
            break
        k += 1
    return k

# 땅에 붙어 있는 클러스터는 1 표시, 공중에 떠 있는 클러스터는 2 표시
def check():
    global visited
    for c in range(C):
        if cave[R-1][c] == 'x' and not visited[R-1][c]:
            bfs(R-1, c, 1)     # 땅에 붙어 있는 미네랄이면 방문처리

    for r in range(R-1):
        for c in range(C):
            if cave[r][c] == 'x' and not visited[r][c]:
                bfs(r, c, 2)    # 공중에 떠있는 클러스터

# main
R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input())
info = list(map(int, input().split()))

heights = [R - info[i] for i in range(N)]    # 높이 정보 변환
for i in range(N):
    tag = 0
    if not i % 2:   # 짝수 인덱스일 때 왼쪽에서 날아옴
        for j in range(C):
            if cave[heights[i]][j] == 'x':
                cave[heights[i]][j] = '.'
                tag = 1
                break
    else:           # 홀수 인덱스일 때 오른쪽에서 날아옴
        for j in range(C-1, -1, -1):
            if cave[heights[i]][j] == 'x':
                cave[heights[i]][j] = '.'
                tag = 1
                break
    # print(i, "번 막대기 던진 후 동굴 상태 =============================")
    # for c in cave:
    #     print(c)
    if tag:         # 미네랄 깼으면
        visited = [[0] * C for _ in range(R)]
        check()     # 각 클러스터가 땅에 붙어있는지

# print("visited 상태")
# for v in visited:
#     print(v)

for row in cave:
        print(''.join(row))
