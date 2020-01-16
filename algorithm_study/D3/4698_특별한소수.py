import sys
sys.stdin = open("4698_input.txt")

def check_special(N):
    global D, flag
    S = str(N)
    for s in S:
        if D == int(s):
            flag = 1
    return

T = int(input())
for tc in range(T):
    D, A, B = map(int, input().split())
    # sosu = []
    total = 0
    for n in range(A, B + 1):
        cnt = 0
        for i in range(1, n + 1):
            if cnt > 2:
                continue
            if n % i == 0:
                cnt += 1
            # print(cnt)
        if cnt == 2:
            flag = 0
            check_special(n)
            if flag:
                total += 1
    print("#{} {}".format(tc+1, total))