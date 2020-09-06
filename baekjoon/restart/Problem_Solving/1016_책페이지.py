# N쪽인 책의 첫 페이지는 1쪽이고, 마지막 페이지는 N쪽이다.
# 각 숫자가 모두 몇 번이 나오는지 출력하는 프로그램을 작성하시오.

# 참고 블로그
# https://pacific-ocean.tistory.com/240

N = 43
# N = int(input())
A = [0] * 10
point = 1
while True:
    if not N:
        break
    # N보다 작은 수 중에서 9를 만날 때까지
    while True:
        if N % 10 == 9:
            break
        for i in str(N):
            A[int(i)] += point
        N -= 1
    # 10보다 클 때와 작을 때 처리
    if N < 10:
        for i in range(N+1):
            A[i] += point
        A[0] -= point
        break
    else:
        for i in range(10):
            A[i] += (N//10 + 1) * point
    A[0] -= point
    point *= 10
    N //= 10

print(*A)