import sys
sys.stdin = open('14890_input.txt')

N, L = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# 가로
for i in range(N):
    H = A[i][0]
    cnt = 1
    for j in range(1, N):
        if A[i][j] == H:
            pass
        # 땅의 높이가 이전 땅의 높이보다 1 낮을 때
        elif A[i][j] + 1 == H and cnt >= 0:
            H = A[i][j]
            cnt = -L
        # 땅의 높이가 이전 땅의 높이보다 1 높을 때
        elif A[i][j] - 1 == H and cnt >= L:
            H = A[i][j]
            cnt = 0
        else:
            break
        cnt += 1
    # break에 걸리지 않았으면 실행
    else:
        if cnt >= 0:
            ans += 1

# 세로
for j in range(N):
    H = A[0][j]
    cnt = 1
    for i in range(1, N):
        if A[i][j] == H:
            pass
        # 땅의 높이가 이전 땅의 높이보다 1 낮을 때
        elif A[i][j] + 1 == H and cnt >= 0:
            H = A[i][j]
            cnt = -L
        # 땅의 높이가 이전 땅의 높이보다 1 높을 때
        elif A[i][j] - 1 == H and cnt >= L:
            H = A[i][j]
            cnt = 0
        else:
            break
        cnt += 1
    else:
        if cnt >= 0:
            ans += 1
print(ans)