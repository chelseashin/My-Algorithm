import sys
sys.stdin = open('16236_input.txt')

from collections import deque

# 상 좌 하 우
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

def bfs(sr, sc):
    Q = deque([(sr, sc)])
    visited = set([(sr, sc)])
    time = 0
    shark = 2   # 상어 크기
    eat = 0     # 현재까지 먹은 물고기 수
    flag = False    # 물고기 먹었는지 여부
    answer = 0

    while Q:
        size = len(Q)
        Q = deque(sorted(Q))    # 상 > 좌 순으로 큐의 우선순위 정렬

        for _ in range(size):
            r, c = Q.popleft()
            if S[r][c] and S[r][c] < shark:
                S[r][c] = 0
                eat += 1
                flag = True

                if eat == shark:
                    shark += 1
                    eat = 0

                # 먹고 난 뒤, 현재 위치를 기준으로 다시 근처를 탐색해야 하기 때문에,
                # BFS queue 와 visited 를 초기화 해준다.
                Q = deque()
                visited = set([(r, c)])

                # 먹었을 때의 시간을 저장해둔다.
                answer = time

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if (nr, nc) in visited:
                    continue
                if S[nr][nc] <= shark:
                    Q.append((nr, nc))
                    visited.add((nr, nc))

            # 현재 위치에서 먹었다면, 더 이상 위 반복문을 돌 필요가 없다.
            if flag:
                flag = False
                break
        time += 1
    return answer
# main
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

# 1. 초기 상어의 위치를 파악, 해당 자리 비우기
for i in range(N):
    for j in range(N):
        if S[i][j] == 9:
            sr, sc = i, j  # 시작 상어 위치
            S[sr][sc] = 0

# 2. 시작점에서 BFS 진행
print(bfs(sr, sc))