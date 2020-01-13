import sys
sys.stdin = open("16_input.txt")

T = int(input())
for tc in range(T):
    C = input().split()
    S = []
    ans = "error"
    for i in C:
        if i == "+" or i == "-" or i == "*" or i == "/":
            if len(S) == 1:
                break
            else:
                a = S.pop(-2)
                b = S.pop(-1)
                if i == "+":
                    S.append(a+b)
                elif i == "-":
                    S.append(a-b)
                elif i == "*":
                    S.append(a*b)
                elif i =="/":
                    S.append(a//b)
        else:
            if i == ".":
                if len(S) == 1:
                    ans = S[-1]
                else:
                    break
            else:
                S.append(int(i))
    print("#{} {}".format(tc+1, ans))