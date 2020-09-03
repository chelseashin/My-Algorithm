import sys

sys.stdin = open('2112_input.txt')


def test(F):
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
        if (c + 1) != check:
            return False
    return True

def dfs(depth, pos, K):
    global MIN
    if depth == K:
        print(selected)
        MIN = min(MIN, depth)
        return
    for i in range(pos, D):
        if selected[i]:
            continue
        selected[i] = 1
        for j in range(2):
            film[i] = drug[j]
            if test(film):

                selected[i] = 0
                film[i] = raw[i]
                return
            else:
                dfs(depth + 1, i + 1, K)
        # dfs(depth+1, i+1, K)
        selected[i] = 0
        film[i] = raw[i]

T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    film = [r[:] for r in raw]
    drug = [[0] * W, [1] * W]
    selected = [0] * D
    MIN = float('inf')

    if test(film):
        MIN = 0
    else:
        for i in range(1, K+1):
            dfs(0, 0, i)


    print("#{} {}".format(tc + 1, MIN))