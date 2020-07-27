import sys
sys.stdin = open('1204_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    cnt = [0] * 101
    for i in L:
        cnt[i] += 1
    temp = 0
    for j in range(101):
        if temp <= cnt[j]:
            temp = cnt[j]
            ans = j
    print("#{} {}".format(tc+1, ans))