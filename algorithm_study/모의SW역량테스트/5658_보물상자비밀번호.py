import sys
sys.stdin = open("5658_input.txt")

num = '0123456789'

def solve(C):
    global check
    for i in range(0, N, N//4):
        t = 0
        for j in range(N//4):
            # t += C[i+j]
            if C[i+j] in num:
                mul = N//4-j-1
                t += int(C[i+j]) * 16**mul
            else:
                temp = 0
                if C[i+j] == 'A':
                    temp == 10
                elif C[i+j] == 'B':
                    temp == 11
                elif C[i+j] == 'C':
                    temp == 12
                elif C[i+j] == 'D':
                    temp == 13
                elif C[i+j] == 'E':
                    temp == 14
                else:
                    temp == 15
                mul = N//4-j-1
                t += temp * 16**mul

        if t not in check:
            check.append(t)

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    raw = list(input())
    L = [raw]
    for i in range(N//4):
        P = L[-1]
        a = P[-1]
        new = [a] + P[:N-1]
        L.append(new)
    check = []
    for l in L:
        solve(l)
    check.sort(reverse=True)
    print(check)

    print("#{} {}".format(tc+1, check[K-1]))

#1 503
#2 55541
#3 334454
#4 5667473
#5 182189737