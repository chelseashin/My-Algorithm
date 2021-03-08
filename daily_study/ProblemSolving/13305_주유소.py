import sys
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))
prices = list(map(int, input().split()))

# 방법 1
total = prices[0] * info[0]
MIN = prices[0]     # 최대 가격
for i in range(1, N-1):
    MIN = min(MIN, prices[i])
    total += MIN * info[i]
    # print(MIN, info[i])
print(total)

# 방법 2
# total = prices[0] * info[0]
# for i in range(1, N-1):
#     if prices[i-1] <= prices[i]:
#         total += info[i] * prices[i-1]
#         prices[i] = prices[i-1]
#     else:
#         total += info[i] * prices[i]
# print(total)