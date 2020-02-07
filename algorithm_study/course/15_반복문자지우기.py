import sys
sys.stdin = open("15_input.txt")

T = int(input())
for tc in range(T):
    S = input()
    stack = []
    for i in S:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    print("#{} {}".format(tc+1, len(stack)))