import sys
sys.stdin = open("10_input.txt")

def palindrome(S):
    global N, M, ans
    # 가로 회문
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if S[i][j+k] != S[i][j+M-1-k]:
                    flag = 0
                    break
            if flag:
                for m in range(M):
                    ans += S[i][j+m]
    #  세로 회문
    for i in range(N):
        for j in range(N-M+1):
            flag = 1
            for k in range(M//2):
                if S[j+k][i] != S[j+M-1-k][i]:
                    flag = 0
                    break
            if flag:
                for m in range(M):
                    ans += S[j+m][i]
    return ans


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    ans = ""
    palindrome(data)

    print("#{} {}".format(tc+1, ans))