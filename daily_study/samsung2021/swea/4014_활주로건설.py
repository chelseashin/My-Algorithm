# 10:20 start
# finish

import sys
sys.stdin = open("4104_input.txt")

T = int(input())
for tc in range(T):
    N, X = map(int, input())
    A = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    print("#{} {}".format(tc+1, result))

    # 1 7
    # 2 4
    # 3 11
    # 4 11
    # 5 15
    # 6 4
    # 7 4
    # 8 1
    # 9 5
    # 10 8