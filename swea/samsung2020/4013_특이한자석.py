import sys
sys.stdin = open('4013_input.txt')

T = int(input())
for tc in range(T):
    K = int(input())
    M = [list(map(int, input().split())) for _ in range(4)]
    # print(M)
    for _ in range(K):
        n, d = map(int, input().split())    # 회전 자석 번호, 방향(1: 시계, -1: 반시계)
        n -= 1
        direction = [0] * 4
        direction[n] = d
        for i in range(n+1, 4):        # 오른쪽
            if M[i-1][2] != M[i][6]:
                direction[i] = -direction[i-1]
            else:
                break
        for i in range(n, 0, -1):      # 왼쪽
            if M[i][6] != M[i-1][2]:
                direction[i-1] = -direction[i]
            else:
                break

        for d in range(4):
            if direction[d] == 1:
                M[d] = [M[d][-1]] + M[d][:-1]
            elif direction[d] == -1:
                M[d] = M[d][1:] + [M[d][0]]

    result = M[0][0] * 1 + M[1][0] * 2 + M[2][0] * 4 + M[3][0] * 8
    print("#{} {}".format(tc+1, result))

    # 1 10
    # 2 14
    # 3 3
    # 4 13
    # 5 15
    # 6 10
    # 7 2
    # 8 6
    # 9 5
    # 10 4