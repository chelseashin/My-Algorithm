import sys
sys.stdin = open('4311_input.txt')

from collections import deque

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)



# main
K_List = [0] + [k * k + (k-1) * (k-1) for k in range(1, 21)]
print(K_List)

T = int(input())
for tc in range(T):
    N, O, M = map(int, input().split())
    touch_num = list(map(int, input().split()))
    touch_op = list(map(int, input().split()))
    W = int(input())
    MIN = float('inf')

    # for i in range(N):
    #     for j in range(N):

    print('#{} {}'.format(tc+1, MIN))