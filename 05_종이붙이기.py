import sys
sys.stdin = open('05_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    # print(N)

    L = [1, 3]
    for i in range(2, N//10):
        x = L[i-2] * 2 + L[i-1]
        L.append(x)

    print("#{} {}".format(tc+1, L[-1]))
