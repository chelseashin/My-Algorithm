# DFS는 시간초과.. DP로 접근해야 함
# https://www.acmicpc.net/problem/11055
# https://pacific-ocean.tistory.com/153 참고해보자

import sys
input = sys.stdin.readline

# main
N = int(input())
A = list(map(int, input().split()))
dp = [0] * N
dp[0] = A[0]
for i in range(1, N):
    temp = []
    for j in range(i-1, -1, -1):
        if A[i] > A[j]:
            temp.append(dp[j])
    if not temp:
        dp[i] = A[i]
    else:
        dp[i] = A[i] + max(temp)
    print(temp, max(temp))
print(dp)
# print(max(dp))