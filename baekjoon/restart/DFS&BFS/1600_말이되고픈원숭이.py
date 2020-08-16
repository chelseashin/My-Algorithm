import sys
sys.stdin = open('1600_input.txt')

# 1. 이동 경로를 체크하는 배열을 3차로 구성
# 2. 말로 이동할 수 있는 횟수를 넘지 않으면 말로 이동하는 경우와 원숭이로 이동하는 경우를 둘 다 체크
#    말로 이동할 경우 세번째 차수에 1을 더해 말로 이동한 횟수를 체크하는 변수로 설정
# 3. 이동할 수 있는 횟수를 모두 사용한 경우 원숭이로만 이동
# 4. 목적지에 도착하면 이동 거리를 출력

from collections import deque

# 말의 움직임
hr = (-1, -2, -2, -1, 1, 2, 2, 1)
hc = (-2, -1, 1, 2, 2, 1, -1, -2)

# 원숭이 움직임
mr = (-1, 1, 0, 0)
mc = (0, 0, -1, 1)

# 말 움직이기
# def horse(r, c, k):
#     for i in range(8):
#         nr = r + hr[i]
#         nc = c + hc[i]
#         if not (0 <= nr < H and 0 <= nc < W):
#             continue
#         if A[nr][nc] == 0 and visited[nr][nc][k+1] == 0:
#             visited[nr][nc][k+1] = visited[r][c][k] + 1
#             Q.append((nr, nc, k+1))
#
# def monkey(r, c, k):
#     for i in range(4):
#         nr = r + mr[i]
#         nc = c + mc[i]
#         if not (0 <= nr < H and 0 <= nc < W):
#             continue
#         if A[nr][nc] == 0 and visited[nr][nc][k] == 0:
#             visited[nr][nc][k] = visited[r][c][k] + 1
#             Q.append((nr, nc, k))
#
# # 왼쪽 위에서 시작
# def bfs():
#     visited[0][0][0] = 1
#     Q.append((0, 0, 0))
#     # print(visited)
#     while Q:
#         r, c, cnt = Q.popleft()
#         if r == H-1 and c == W-1:
#             print(visited[r][c][cnt]-1)
#             return
#         if cnt < K:     # cnt 값 남아 있을 때, 말과 원숭이 움직이기
#             horse(r, c, cnt)
#             monkey(r, c, cnt)
#         elif cnt == K:    # cnt 다 사용했으면, 원숭이만 움직이기
#             monkey(r, c, cnt)
#     print(-1)



K = int(input())    # 움직일 수 있는 횟수
W, H = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
# visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
# Q = deque()
# bfs()
# print(visited)


# 다른 풀이
def bfs():
    visited = [[[0]*W for _ in range(H)] for __ in range(K+1)]
    visited[0][0][0] = 1
    Q = deque([(0, 0, 0)])
    while Q:
        r, c, cnt = Q.popleft()
        if r == H-1 and c == W-1:
            return visited[cnt][r][c] - 1
        if cnt < K:   # 말 걸음으로 갈 수 있는 기회 있을 때
            for i in range(8):
                nr = r + hr[i]
                nc = c + hc[i]
                if (0 <= nr < H and 0 <= nc < W):
                    if A[nr][nc] == 0 and visited[cnt+1][nr][nc] == 0:
                        visited[cnt+1][nr][nc] = visited[cnt][r][c] + 1
                        Q.append((nr, nc, cnt+1))
        # 원숭이 걸음으로 가기
        for i in range(4):
            nr = r + mr[i]
            nc = c + mc[i]
            if (0 <= nr < H and 0 <= nc < W):
                if A[nr][nc] == 0 and visited[cnt][nr][nc] == 0:
                    visited[cnt][nr][nc] = visited[cnt][r][c] + 1
                    Q.append((nr, nc, cnt))
    return -1

print(bfs())
