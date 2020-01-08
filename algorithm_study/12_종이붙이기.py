import sys
sys.stdin = open("12_input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    L = [1, 3]

    for i in range(2, N//10):
        a = L[i-2] * 2 + L[i-1]
        L.append(a)

    print("#{} {}".format(tc+1, L[-1]))