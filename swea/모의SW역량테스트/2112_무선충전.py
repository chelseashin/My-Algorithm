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

T = int(input())
for tc in range(T):
    D, W, K = map(int, input().split())
    raw = [list(map(int, input().split())) for _ in range(D)]
    film = [r[:] for r in raw]
    MIN = float('inf')
    
    if test(film):
        MIN = 0
    else:
        MIN = "이제 구하기"


    print("#{} {}".format(tc+1, MIN))