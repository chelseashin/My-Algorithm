import sys
sys.stdin = open('17779_input.txt')

# 가장 직관적인 코드
# 하나하나 따져주기 힘들겠지만
# 한번쯤 고생해서 해볼만 하겠다..

# main
N = int(input())
A = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
MIN = float('inf')

for sr in range(2, N):
    for sc in range(1, N-1):
        for d2 in range(1, N-sr+1):
            for d1 in range(1, min(N-(sc+d2) + 1, sr)):
                # 시작점(sr, sc)와 거리 정해질 때마다 각 구역 인구 합 구하기
                zone = [0] * 5
                # 구역 1
                for r in range(1, sr):
                    for c in range(1, sc+d1+1):
                        if r+c < sr+sc:
                            zone[0] += A[r][c]
                # 구역 2
                for r in range(1, sr-d1+d2+1):
                    for c in range(sc+d1+1, N+1):
                        if r-c < sr-sc-d1*2:
                            zone[1] += A[r][c]
                # 구역 3
                for r in range(sr, N+1):
                    for c in range(1, sc+d2):
                        if r-c > sr-sc:
                            zone[2] += A[r][c]
                # 구역 4
                for r in range(sr-d1+d2+1, N+1):
                    for c in range(sc+d2, N+1):
                        if r+c > sr+sc+d2*2:
                            zone[3] += A[r][c]
                # 구역 5
                for r in range(1, 1+N):
                    for c in range(1, 1+N):
                        if sr+sc <= r+c <= sr+sc+d2*2:
                            if sr-sc-d1*2 <= r-c <= sr-sc:
                                zone[4] += A[r][c]
                # print(zone, max(zone)-min(zone))
                temp = max(zone)-min(zone)
                MIN = min(MIN, temp)

print(MIN)