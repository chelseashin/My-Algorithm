import sys
sys.stdin = open('2112_input.txt')

# 메모리 실행시간 가장 좋음

# 성능 테스트
def check(F):
    check = 0
    for c in range(W):
        cnt = 1
        temp = F[0][c]
        for r in range(1, D):
            if F[r][c] == temp:
                cnt += 1
            else:
                temp = F[r][c]
                cnt = 1
            if cnt >= K:
                check += 1
                break
        if (c+1) != check:
            return False
    return True

# 약물 투입 횟수, 시작 행 위치
def dfs(depth, pos):
    global MIN
    if depth >= MIN:    # 가지치기
        return
    # 약물 투여 최대 횟수 K 넘으면 return
    if depth > K:
        return
    for i in range(pos, D):     # 행 선택
        if visited[i]:
            continue
        visited[i] = 1
        for j in range(2):
            film[i] = drug[j]
            if check(film):
                MIN = min(MIN, depth)
                visited[i] = 0
                film[i] = raw[i]
                return
            else:
                dfs(depth+1, i+1)
        visited[i] = 0
        film[i] = raw[i]

# main
T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    MIN = float('inf')
    if check(raw):
        MIN = 0
    else:
        film = [r[:] for r in raw]
        drug = [[0] * W, [1] * W]
        visited = [0] * D
        dfs(1, 0)

    print("#{} {}".format(tc+1, MIN))