import sys
sys.stdin = open("13_input.txt")

def check(S):
    global ans
    gwalho = "{}()"
    G = ""
    for i in S:
        if i in gwalho:
            G += i

    S = []
    for g in G:
        if len(S) == 0:
            S.append(g)
        else:
            if S[-1] == "(":
                if g == ")": S.pop()
                else: S.append(g)
            elif S[-1] == "{":
                if g == "}": S.pop()
                else: S.append(g)

    if len(S): ans = 0
    return ans

T = int(input())
for tc in range(T):
    data = input()
    ans = 1
    check(data)
    print("#{} {}".format(tc+1, ans))