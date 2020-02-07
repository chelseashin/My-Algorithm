import sys
sys.stdin = open("08_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    A = sorted(list(map(int, input().split())))
    new = []
    for i in range(5):
        new.append(A[-i-1])
        new.append(A[i])
    print("#{}".format(tc+1), *new)