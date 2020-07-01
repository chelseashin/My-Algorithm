import sys
sys.stdin = open("5658_input.txt")

def divide(num):
    for i in range(0, N, N//4):
        temp = []
        for j in range(N//4):
            temp.append(num[i+j])
        if ''.join(temp) not in total:
            total.append(''.join(temp))


T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    S = list(input())
    L = [''.join(S)]
    total = []
    for i in range(N//4):
        S = [S.pop()] + S
        L.append(''.join(S))
    print(L)

    for l in L:
        divide(l)
    print("#{} {}".format(tc+1, int(sorted(total, reverse=True)[K - 1], 16)))