# 답은 나오는데 시간초과.....
# 11 이후로 터지는 듯....
# 최적화 필요

def go(depth, k):
    global result
    # 가지치기
    for i in range(depth):
        # 직선 겹침
        if depth == vr[i]:  # 가로 위치 겹침
            return 0
        if k == vc[i]:    # 세로 위치 겹침
            return 0
        if abs(k - vc[i]) == abs(depth- vr[i]):   # 대각선 위치 겹침
            return 0


    # 종료조건
    if (depth == N-1):
        # 말단에서 퀸 배열이 성공적인지 체크
        # 만약 성공적이면 1 리턴
        return 1

    # 말의 현재 위치 기억
    vr[depth] = depth
    vc[depth] = k

    result = 0
    for i in range(N):
        result += go(depth+1, i)
    return result

N = 10
# N = int(input())

vr = [0] * (2*N - 1)
vc = [0] * (2*N - 1)
result = 0
for i in range(N):
    result += go(0, i)
print(result)


a = (0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596)
# print(a[int(input())])
# print(a[N])