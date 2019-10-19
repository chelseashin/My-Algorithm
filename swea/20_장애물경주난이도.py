import sys
sys.stdin = open('20_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    block = list(map(int, input().split()))

    UP = float('-inf')
    DOWN = float('-inf')

    for i in range(N-1):
        up, down = 0, 0

        if block[i] < block[i+1]:
            up = block[i+1] - block[i]

        elif block[i] > block[i+1]:
            down = block[i] - block[i+1]

        elif block[i] == block[i+1]:
            up = 0
            down = 0
        if DOWN < down:
            DOWN = down
        if UP < up:
            UP = up

    print("#{} {} {}".format(tc+1, UP, DOWN))