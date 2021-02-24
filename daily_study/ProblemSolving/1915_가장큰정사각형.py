# 23:15 start
# 23:39 시간초과.. DP로 접근해야 한다!
# 참고해보자 https://cagongman.tistory.com/18
# 어렵지 않은 DP 문제

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for i in range(N):
    s = input()
    A.append(list(map(int, list(s))))

# A 탐색하면서 채울 DP 테이블
dp = [[0] * (M+1) for _ in range(N+1)]
size = 0    # 최대 변의 길이

for i in range(1, N+1):
    for j in range(1, M+1):
        if A[i-1][j-1]:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
            size = max(size, dp[i][j])
print(size ** 2)

# data[i-1][j-1]가 0일 경우 정사각형을 만들 수 없으므로 1일 경우에만 체크합니다.
# dp[i][j]에는 data[i - 1][j - 1]를 정사각형의 우측하단 꼭짓점으로하여 만들  수 있는 정사각형의 변의 길이를 저장합니다.
# side에 새로 만들어진 변의 길이가 최대 길이인지 확인하고 수정합니다.
print("---------------")
for d in dp:
    print(d)


# 시간초과,, 무조건 DP로 풀어야 함
# def check(sr, sc, size):
#     for i in range(sr, sr+size):
#         for j in range(sc, sc+size):
#             if A[i][j] == '0':
#                 return 0
#     return size
#
# # main
# N, M = map(int, input().split())
# A = [list(input().strip()) for _ in range(N)]
#
# MAX = 0
# for r in range(N):
#     for c in range(M):
#         for size in range(min(N-r, M-c), 0, -1):
#             MAX = max(MAX, check(r, c, size))
# print(MAX**2)