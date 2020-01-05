import sys
sys.stdin = open("07_input.txt")

def binarySearch(P, S):
    l = 1
    r = P
    cnt = 0

    while l <= r:
        cnt += 1
        c = int((l+r)/2)
        if c < S:
            l = c
        elif c > S:
            r = c
        else:
            return cnt

T = int(input())
for tc in range(T):
    P, Pa, Pb = map(int, input().split())

    cnt_a = binarySearch(P, Pa)
    cnt_b = binarySearch(P, Pb)

    if cnt_a > cnt_b: ans = "B"
    elif cnt_b > cnt_a: ans = "A"
    else: ans = 0
    print("#{} {}".format(tc+1, ans))