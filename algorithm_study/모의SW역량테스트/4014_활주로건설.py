import sys
sys.stdin = open("4014_input.txt")

T = int(input())
for tc in range(T):
    N, X = map(int, input().split())
    land = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    # 가로
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            # 땅 높이가 전의 높이와 같을 때
            if land[i][j] == land[i][j-1]:
                cnt += 1
            # 땅이 1만큼 솟아 있을 때
            elif land[i][j-1] == land[i][j]+1 and cnt >= 0:
                cnt = -X+1
            # 땅이 1만큼 내려갈 때
            elif land[i][j-1]+1 == land[i][j] and cnt >= X:
                cnt = 1
            else:
                break
        else:
            if cnt >= 0:
                total += 1
    # 세로
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            # 땅 높이가 전의 높이와 같을 때
            if land[i-1][j] == land[i][j]:
                cnt += 1
            # 땅이 1만큼 솟아 있을 때
            elif land[i-1][j] == land[i][j]+1 and cnt >= 0:
                cnt = -X+1
            # 땅이 1만큼 내려갈 때
            elif land[i-1][j]+1 == land[i][j] and cnt >= X:
                cnt = 1
            else:
                break
        else:
            if cnt >= 0:
                total += 1
    print("#{} {}".format(tc+1, total))
    
# 1 7
# 2 4
# 3 11
# 4 11
# 5 15
# 6 4
# 7 4
# 8 1
# 9 5
# 10 8