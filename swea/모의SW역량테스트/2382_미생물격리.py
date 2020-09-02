import sys
sys.stdin = open('2382_input.txt')

# 메모리, 실행시간 너무 심하게 많이 소모
# 개선 필요
# 맵 하나로 계속 풀어가보자

# 상 하 좌 우
dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

def change_dir(n):
    if n == 1: return 2
    elif n == 2: return 1
    elif n == 3: return 4
    elif n == 4: return 3

def move(A):
    new = [[[] for _ in range(N)] for _ in range(N)]
    movement = set()
    for r in range(N):
        for c in range(N):
            if A[r][c]:
                cnt, dir = A[r][c]
                nr = r + dr[dir]
                nc = c + dc[dir]
                if not (1 <= nr < N-1 and 1 <= nc < N-1):
                    new[nr][nc].append([A[r][c][0]//2, change_dir(dir)])
                    movement.add((nr, nc))
                    continue
                new[nr][nc].append(A[r][c])
                movement.add((nr, nc))

    for r, c in movement:
        if len(new[r][c]) == 1:
            new[r][c] = new[r][c][0]
        elif len(new[r][c]) > 1:
            L = sorted(new[r][c], reverse=True)
            temp = 0
            for n, d in L:
                temp += n
            max_dir = L[0][1]
            new[r][c] = [temp, max_dir]
    return new

# main
T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())
    A = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        r, c, n, d = map(int, input().split())
        A[r][c] = [n, d]

    for _ in range(M):
        A = move(A)

    # 남은 미생물의 수
    microbe = 0
    for i in range(N):
        for j in range(N):
            if A[i][j]:
                microbe += A[i][j][0]

    print("#{} {}".format(tc+1, microbe))