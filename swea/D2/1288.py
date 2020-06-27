import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    NN = N
    S = []
    count = 0
    while len(S) < 10:
        count += 1
        N = NN * count
        N = str(N)
        for i in N:
            if i not in S:
                S.append(i)
    print("#{} {}".format(tc+1, NN * count))