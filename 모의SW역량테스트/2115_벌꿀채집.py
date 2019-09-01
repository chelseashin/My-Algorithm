import sys
sys.stdin = open('2115_input.txt')

# 열 선택
# def combination(r, depth, k):
#     if depth == 2:
#         check(L)
#         return
#     for i in range(k, 6):
#         L.append(i)
#         combination(depth + 1, i)
#         L.pop()

# 행 선택
def combination(depth, k):
    if depth == 2:
        # 꿀양 계산 해주는 함수 호출 여기서 해주면 됨.
        check(L)
        return
    for i in range(k, 6):
        L.append(i)
        combination(depth + 1, i)
        L.pop()

def check(H):
    global honey, N
    if H[0] + H[1] > N:
        return
    else:
        # H[0] : A가 선택한 행, H[1] : B가 선택한 행

        if H[0] == H[1]:
            for i in range(N-):
                for j in range(i+1, N-M+1)
                    cal(H[0][i])
        else:
            for i in range(N-M+1):
                # honey[H[0]][i]
                # 시작 좌표 r, c, 뽑을 수 있는 1 ~ M
                cal(H[0], i, M) + cal(H[1], i, M)

T = int(input())
for tc in range(T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    # 두 명의 양봉업자가 선택할 수 있는 행 : ex) L = [0, 0] ~ [N-1, N-1]
    L = []
    combination(2, 0, 0)


    print("#{} {}".format(tc+1, total))