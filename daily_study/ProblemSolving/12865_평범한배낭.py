# Dynamic Programming
# 핵심 아이디어 : 모든 무게에 대해 최대 가치를 저장하기
# D[i][j] = 배낭에 넣은 물품의 합이 j일 때 얻을 수 있는 최대 가치
# 각 물품의 번호 i에 따라 최대 가치 테이블 D[i][j]를 갱신하여 문제 해결.

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        if j < W:   # 물건의 무게보다 j가 작으면 바로 위의 값을 넣어줌
            dp[i][j] = dp[i-1][j]
        else:
            # 바로 위에 있던 값과 이전까지 구한 값과 현재 가치를 더한 값을 비교해서 더 큰 값을 넣어줌
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)
# print(dp)
print(dp[N][K])