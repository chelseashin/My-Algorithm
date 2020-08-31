import sys
sys.stdin = open('2117_input.txt')

# https://hongsj36.github.io/2020/02/26/SWEA_2117/
# 집의 좌표를 담아 가능한 범위 안의 집 세기

# main
T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    MAX = float('-inf')

    houses = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                houses.append((i, j))
    print(houses)


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