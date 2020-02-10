import sys
sys.stdin = open("16637_input.txt")

def backtracking(i, res):
    global ans
    if i == N:
        # ans = max(res, ans)
        if ans < res:
            ans = res
        return
    if S[i] == "+":
        backtracking(i+2, res+int(S[i+1]))
        if i == N-2:
            return
        a = int(S[i+1])
        o = S[i+2]
        b = int(S[i+3])
        if o == '+':
            backtracking(i+4, res+(a+b))
        elif o == '-':
            backtracking(i+4, res+(a-b))
        else:
            backtracking(i+4, res+(a*b))

    elif S[i] == "-":
        backtracking(i+2, res-int(S[i+1]))
        if i == N-2:
            return
        a = int(S[i+1])
        o = S[i+2]
        b = int(S[i+3])
        if o == '+':
            backtracking(i+4, res-(a+b))
        elif o == '-':
            backtracking(i+4, res-(a-b))
        else:
            backtracking(i+4, res-(a*b))
    else:
        backtracking(i+2, res*int(S[i+1]))
        if i == N-2:
            return
        a = int(S[i+1])
        o = S[i+2]
        b = int(S[i+3])
        if o == '+':
            backtracking(i+4, res*(a+b))
        elif o == '-':
            backtracking(i+4, res*(a-b))
        else:
            backtracking(i+4, res*(a*b))

N = int(input())
S = input()
ans = -2^32

backtracking(1, int(S[0]))
print(ans)