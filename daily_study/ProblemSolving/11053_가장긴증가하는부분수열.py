# LIS는 가장 전형적인 Dynamic Programming 문제!
# 수열의 크기가 N일 때, 기본적인 DP 알고리즘으로 O(N^2)으로 해결할 수 있다.
# dp[i] = array[i]를 마지막 원소로 가지는 부분수열의 최대 길이
# 모든 0 <= j < i에 대해, dp[i] = max(D[i], D[j] + 1 if A[j] < A[i]

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
    # print(i, dp)
print(max(dp))