import sys
sys.stdin = open('4014_input.txt')

def check(L):
    cnt = 1
    for i in range(1, N):
        if L[i-1] == L[i]:
            cnt += 1
        # 현 위치가 전 위치보다 높은 경우
        elif L[i] - L[i-1] == 1 and cnt >= X:
                cnt = 1
        # 현 위치가 전 위치보다 낮은 경우
        elif L[i] - L[i-1] == -1 and cnt >= 0:
            cnt = -X+1
        else:
            return False
    if cnt >= 0:
        # print(L)
        return True

# main
T = int(input())
for tc in range(T):
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    # for a in A:
    #     print(a)
    # print()
    result = 0
    for row in A:
        if check(row):
            result += 1
    for col in zip(*A):
        if check(col):
            result += 1
    print("#{} {}".format(tc+1, result))

    # 1 7
    # 2 4
    # 3 11
    # 4 11
    # 5 15
    # 6 4
    # 7 4
    # 8 1
    # 9 5
    # 10 8