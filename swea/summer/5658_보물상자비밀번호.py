import sys
sys.stdin = open("5658_input.txt")

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    S = list(input())
    L = [''.join(S)]
    total = []
    for i in range(N//4):
        S = [S.pop()] + S
        L.append(''.join(S))
    # print(L)

    for num in L:
        for i in range(0, N, N // 4):
            temp = []
            for j in range(N // 4):
                temp.append(num[i + j])
            if ''.join(temp) not in total:
                total.append(''.join(temp))

    print("#{} {}".format(tc+1, int(sorted(total, reverse=True)[K - 1], 16)))

# 16진수 10진수로 변환
# print(int('1F7', 16))