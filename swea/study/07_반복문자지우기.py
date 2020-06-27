import sys
sys.stdin = open("07_input.txt")

T = int(input())
for tc in range(T):
    abc = str(input())
    S = []
    for i in abc:
        if len(S) == 0:
            S.append(i)
        else:
            if S[-1] != i:
                S.append(i)
            else:
                S.pop()

    print("#{} {}".format(tc+1, len(S)))