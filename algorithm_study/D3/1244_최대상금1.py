import sys
sys.stdin = open("1244_input.txt")

# N은 주어진 수의 길이, k는 기회 수
def dfs(N, L, I):
    global MAX
    if N == 0:
        L = int(''.join(map(str, L)))
        if MAX < L:
            MAX = L
        return

    for i in range(I, size):
        for j in range(i+1, size):
            if L[j] >= L[i]:
                temp = [i for i in L]
                temp[i], temp[j] = temp[j], temp[i]
                dfs(N-1, temp, i)

T = int(input())
for tc in range(T):
    S, N = input().split()
    S = list(map(int, list(S)))
    N = int(N)
    size = len(S)
    MAX = 0
    dfs(N, S, 0)

    print("#{} {}".format(tc+1, MAX))


#1 321
#2 7732
#3 857147
#4 87664
#5 88832
#6 777770
#7 966354
#8 954311
#9 332211
#10 987645