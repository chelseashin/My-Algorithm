from sys import stdin
input = stdin.readline

H, W = map(int, input().split())
A = list(map(int, input().split()))

# 풀이 1 (참고 : https://incastle-study.tistory.com/2)
# raindrop = 0
# for i in range(W):
#     maxLeft = max(A[:i+1])   # 현재 인덱스의 왼쪽에서 가장 높은 건물의 높이
#     maxRight = max(A[i:])    # 현재 인덱스의 오른쪽에서 가장 높은 건물의 높이
#     which_low = min(maxLeft, maxRight)  # 둘중에 어떤 값이 더 큰가?
#     raindrop += abs(A[i]-which_low)     # 현 위치와의 차이의 절대값을 더해줌
# print(raindrop)

# 풀이 2 (참고 : https://namhandong.tistory.com/139)
maxIdx = A.index(max(A))    # 가장 큰 높이의 인덱스

total = 0
# 왼쪽부터 가장 큰 높이의 탑까지 작아지지 않는 큰 수들을 더해줌
temp = 0
for i in range(maxIdx+1):
    if A[i] > temp:
        temp = A[i]
    total += temp
# 오른쪽부터 가장 큰 높이의 탑까지 작아지지 않는 큰 수들을 더해줌
temp = 0
for i in range(W-1, maxIdx, -1):
    if A[i] > temp:
        temp = A[i]
    total += temp
# 빗물이 고인부분만 구하려면 전체 빗물에서 각 높이의 합을 빼주면 됨
print(total-sum(A))

# 풀이 3 (참고 : https://jjangsungwon.tistory.com/121)
# 깔끔한 풀이. 변수명 잘 지음!