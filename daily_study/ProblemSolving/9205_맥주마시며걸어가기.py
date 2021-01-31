import sys
input = sys.stdin.readline
from collections import deque

def bfs(sx, sy):
    Q = deque()
    visited = []
    Q.append([sx, sy, 20])          # 시작 위치, 맥주 갯수
    visited.append([sx, sy, 20])
    while Q:
        x, y, beer = Q.popleft()
        if (x, y) == (fx, fy):      # 페스티벌 도착하면
            return "happy"
        for nx, ny in places:       # 갈 수 있는 전체 장소 탐색
            if [nx, ny, 20] not in visited:
                dis = abs(nx-x) + abs(ny-y)
                if beer * 50 >= dis:
                    Q.append([nx, ny, 20])      # 이동한 위치 넣으며 맥주 구매
                    visited.append([nx, ny, 20])
    return "sad"

T = int(input())
for _ in range(T):
    N = int(input())
    places = deque()        # 갈 수 있는 곳 위치 리스트
    hx, hy = map(int, input().split())
    for n in range(N):
        x, y = map(int, input().split())
        places.append((x, y))
    fx, fy = map(int, input().split())
    places.append((fx, fy))

    print(bfs(hx, hy))