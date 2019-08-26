import sys
sys.stdin = open("01_input.txt")

T = int(input())
for i in range(T):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    while N > 0:
        if N == 1:
            break
        else:
            if N % 2 == 0:
                a += 1
                N //= 2
            if N % 3 == 0:
                b += 1
                N //= 3
            if N % 5 == 0:
                c += 1
                N //= 5
            if N % 7 == 0:
                d += 1
                N //= 7
            if N % 11 == 0:
                e += 1
                N //= 11
    # print(a, b, c, d, e)
    print("#{} {} {} {} {} {}".format(i+1, a, b, c, d, e))
