import sys
sys.stdin = open('5648_input.txt')

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    global Q, result
    while Q:
        collision = []  # 충돌한 원자들의 위치 리스트
        visited = []
        qlen = len(Q)
        for _ in range(qlen):
            r, c, d, k = Q.pop(0)
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < 4001 and 0 <= nc < 4001):
                continue
            if (nr, nc) in collision:
                result += k
                continue
            if (nr, nc) not in visited:
                visited.append((nr, nc))
                Q.append((nr, nc, d, k))
                continue
            collision.append((nr, nc))
            result += k

        for i in reversed(range(len(Q))):
            r, c, d, k = Q[i]
            if (r, c) in collision:
                result += k
                Q.pop(i)

# main
T = int(input())
for tc in range(T):
    N = int(input())
    result = 0

    Q = []
    for _ in range(N):
        c, r, d, k = map(int, input().split())
        r = 4000 - (1000 + r) * 2
        c = (1000 + c) * 2
        Q.append((r, c, d, k))
    # print(Q)
    bfs()
    print("#{} {}".format(tc+1, result))
