import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while N:
        if N == 1:
            break
        else:

            if N % 11 == 0:
                e += 1
                N //= 11
            if N % 7 == 0:
                d += 1
                N //= 7
            if N % 5 == 0:
                c += 1
                N //= 5
            if N % 3 == 0:
                b += 1
                N //= 3
            if N % 2 == 0:
                a += 1
                N //= 2

    print("#{} {} {} {} {} {}".format(tc+1, a, b, c, d, e))