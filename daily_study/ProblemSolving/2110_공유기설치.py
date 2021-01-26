# 집의 갯수 N은 최대 200,000개. 집의 좌표는 1,000,000,000까지 있음.
# 이진 탐색을 이용하여 O(NlogX)에 문제 해결 가능.
# 가장 인접한 두 공유기 사이의 최대 Gap을 이진 탐색으로 찾음.
# 이진탐색으로 찾기 => 반복문 이용

N, C = map(int, input().split(' '))
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()
start = 1
end = A[-1] - A[0]
result = 0

while start <= end:
    mid = (start + end) // 2        # 두 공유기 사이의 거리 의미
    value = A[0]
    cnt = 1
    for i in range(1, N):
        if A[i] >= value + mid:
            value = A[i]
            cnt += 1
    if cnt >= C:    # C개 이상의 공유기를 설치할 수 있는 경우
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)