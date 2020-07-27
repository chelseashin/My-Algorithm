import sys
sys.stdin = open("1289_input.txt")

T = int(input())
for tc in range(T):
    N = list(input())
    n = len(N)
    temp = ['0'] * n
    cnt = 0
    for i in range(n):
        if temp[i] != N[i]:
            for j in range(i, n):
                temp[j] = N[i]
            cnt += 1
    print("#{} {}".format(tc+1, cnt))

#1 49
#2 1
#3 19
#4 23
#5 15
#6 19
#7 6
#8 27
#9 30
#10 8