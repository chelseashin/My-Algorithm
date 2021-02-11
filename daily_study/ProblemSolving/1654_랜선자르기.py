# 이진탐색으로 풀기

import sys
input = sys.stdin.readline

K, N = map(int, input().split())     # 항상 K <= N
A = []
start, end = 1, 0
for _ in range(K):
    a = int(input())
    A.append(a)
    end = max(end, a)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for line in A:
        lines += line // mid
    if lines >= N:
        start = mid + 1
    else:
        end = mid - 1
    print(mid)
print(end)


# 이분탐색 함수
# def binarySearch(array, value, low, high):
#     if low > high:
#         return False
#     mid = (low+high) / 2
#     if array[mid] > value:
#         return binarySearch(array, value, low, mid-1)
#     elif array[mid] < value:
#         return binarySearch(array, value, mid+1, high)
#     else:
#         return mid