# 정답.. 1위 달성

# 참고 링크 : https://chldkato.tistory.com/62
# 1. 막대를 좌우 순서대로 던질 수 있도록 변수를 설정한다 (1, -1 반복)
# 2. 미네랄을 파괴했다면 상하좌우에 미네랄이 있는지 확인한다. 있다면 떨어질 수 있는 후보이므로 저장해둔다
# 3. 큐에서 하나씩 꺼내서 bfs를 돌려본다.
#    이동하면서 아래 칸이 . 이면 떨어질 수 있는 클러스터의 맨 아래이므로 저장해둔다
#    만약 바닥까지 도착하면 떨어지지 않으므로 return
#    바닥에 도착하지 않으면 떨어져야 하므로 떨어지는 작업을 수행한다
# 4. fall 함수는 클러스터가 얼마만큼 떨어져야하는지 확인한 후 클러스터를 밑에서부터 순차적으로 떨어뜨린다
# 5. 모든 작업을 완료한 후 동굴 상태 출력

import sys
input = sys.stdin.readline
from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def destroy(i, temp):
    r, c = R-i, 0
    if temp == 1:   # 왼쪽에서 날아옴
        for k in range(C):
            if A[r][k] == 'x':
                A[r][k] = '.'
                c = k
                break
    else:
        for k in range(C-1, -1, -1):
            if A[r][k] == 'x':
                A[r][k] = '.'
                c = k
                break
    for d in range(4):      # 깨진 곳의 4방향을 확인
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if A[nr][nc] == 'x':        # 미네랄 있으면
            Q.append((nr, nc))      # 큐에 담기

def bfs(sr, sc):
    q = deque([(sr, sc)])
    check = [[0] * C for _ in range(R)]
    check[sr][sc] = 1
    fallLst = []
    left, right = sc, sc
    while q:
        r, c = q.popleft()
        if r == R-1:    # 땅에 붙어있는 클러스터이면 리턴
            return
        if A[r+1][c] == '.':    # 떨어질 수 있는 클러스터의 아랫부분만 저장
            fallLst.append((r, c))
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if A[nr][nc] == 'x' and not check[nr][nc]:
                check[nr][nc] = 1
                q.append((nr, nc))
                left = min(left, nc)
                right = max(right, nc)
    fall(check, fallLst, left, right)

def fall(check, fallLst, left, right):
    k, flag = 1, 0      # k 크기 1씩 늘려가며
    while True:
        for r, c in fallLst:
            if r+k == R-1:        # 땅을 만나거나
                flag = 1
                break
            if A[r+k+1][c] == 'x' and not check[r+k+1][c]:   # 다른 미네랄 만나면
                flag = 1
                break
        if flag:    # 그 때가 떨어질 수 있는 최대 k 값
            break
        k += 1
    for i in range(R-2, -1, -1):
        for j in range(left, right+1):
            # 클러스터 내린 상태 A에 반영
            if A[i][j] == 'x' and check[i][j]:
                A[i][j] = '.'
                A[i+k][j] = 'x'

# main
R, C = map(int, input().split())
A = [list(input().strip()) for _ in range(R)]
N = int(input())
info = list(map(int, input().split()))

Q = deque()
temp = 1
for idx in range(N):
    destroy(info[idx], temp)
    while Q:
        r, c = Q.popleft()
        bfs(r, c)
    temp *= -1

for row in A:
        print(''.join(row))