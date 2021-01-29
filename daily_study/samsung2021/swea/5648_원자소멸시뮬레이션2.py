import sys
sys.stdin = open("5648_input.txt")

# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def bfs():
    global Q
    result = 0
    while Q:
        collision = []                      # 충돌한 원자들의 좌표 리스트
        visited = []
        qlen = len(Q)
        for _ in range(qlen):
            r, c, d, k = Q.pop(0)
            nr = r + dr[d] * 0.5
            nc = c + dc[d] * 0.5
            # 격자 밖으로 나가면 더이상 충돌할 수 없기 때문에 그냥 두기
            if not (0 <= nr < 2001 and 0 <= nc < 2001):
                continue
            if (nr, nc) in visited:         # 이미 어떤 원자가 간 곳이면
                collision.append((nr, nc))  # 충돌 리스트에 넣기
                result += k                 # 에너지 방출
                continue
            visited.append((nr, nc))        # 첫 방문인 경우
            Q.append((nr, nc, d, k))

        # Q에 들어있는 값들 중 가장 먼저 도착하여 충돌한 원자로 처리.
        # 뒤에서부터 확인하는 이유는 인덱스 꼬이지 않게 하기 위해
        for i in range(len(Q) - 1, -1, -1):
            r, c, d, k = Q[i]
            if (r, c) in collision:
                result += k
                Q.pop(i)
    return result

T = int(input())
for tc in range(T):
    N = int(input())
    Q = []
    for i in range(N):
        c, r, d, k = map(int, input().split())
        # 격자를 수학적으로 일반적인 이차원 배열에 놓인 위치로 계산
        r = 2000 - (1000 + r)
        c = (1000 + c)
        Q.append((r, c, d, k))

    print("#{} {}".format(tc + 1, bfs()))