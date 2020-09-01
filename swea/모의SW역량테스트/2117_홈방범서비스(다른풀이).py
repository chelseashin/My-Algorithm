import sys
sys.stdin = open('2117_input.txt')

# 집의 좌표를 담아 가능한 범위 안의 집 세기

# main
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]

    houses = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))

    MAX = 1      # K가 1일 때 초기값(최소 1개 이상 집이 있기 때문)
    for K in range(2, N+2):     # K 크기 결정
        for r in range(N):
            for c in range(N):
                cnt = 0     # 범위 안의 집 세기
                for y, x in houses:
                    if abs(r-y) + abs(c-x) < K:
                        cnt += 1
                # 손해 안 나면서 더 많은 집이 가능할 경우 갱신
                if cnt > MAX and cnt * M >= K**2 + (K-1)**2:
                    MAX = cnt

    print("#{} {}".format(tc+1, MAX))

    # 1 5
    # 2 4
    # 3 24
    # 4 48
    # 5 3
    # 6 65
    # 7 22
    # 8 22
    # 9 78
    # 10 400