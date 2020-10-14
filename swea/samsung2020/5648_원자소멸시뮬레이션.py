import sys
sys.stdin = open('5648_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    global Q
    result = 0
    while Q:
        collision = []
        visited = []
        qlen = len(Q)
        for _ in range(qlen):
            r, c, d, k = Q.pop(0)
            nr = r + dr[d] * 0.5
            nc = c + dc[d] * 0.5
            if not (0 <= nr < 2001 and 0 <= nc < 2001):
                continue
            if (nr, nc) in visited:
                collision.append((nr, nc))
                result += k
                continue
            visited.append((nr, nc))
            Q.append((nr, nc, d, k))
        for i in range(len(Q)-1, -1, -1):
            r, c, d, k = Q[i]
            if (r, c) in collision:
                result += k
                Q.pop(i)
    return result

# main
T = int(input())
for tc in range(T):
    N = int(input())
    Q = []
    for _ in range(N):
        c, r, d, k = map(int, input().split())
        r = 2000 - (1000 + r)
        c = (1000 + c)
        Q.append((r, c, d, k))

    print("#{} {}".format(tc+1, bfs()))

    # 1 24
    # 2 0
    # 3 8
    # 4 17
    # 5 16
    # 6 10
    # 7 7
    # 8 1111