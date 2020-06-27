import sys
sys.stdin = open('23_input.txt')

T = int(input())
for tc in range(T):
    N = list(map(str, input()))
    L = []
    for n in N:
        if n not in L:
            L.append(n)
        else:
            L.remove(n)
    print("#{} {}".format(tc+1, len(L)))
