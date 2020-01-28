import sys
sys.stdin = open("5373_input.txt")

# from collections import deque

T = int(input())
for tc in range(T):
    N = int(input())
    cube = [list([0] * 3 for _ in range(3)) for _ in range(6)]
    color = 0
    for i in range(6):
        for j in range(3):
            for k in range(3):
                cube[i][j][k] = color
        color += 1
    print("# start")
    method = list(input().split())
    # print(method)
    for m in method:
    #     if method[0] == "U":
        if m[0] == "L":
            if m[1] == "-":
                change = [3, 0, 2, 1]
                a = [cube[3][i][0] for i in range(3)]
                b = [cube[0][j][0] for j in range(3)]
                c = [cube[2][k][0] for k in range(3)]
                d = [cube[1][l][0] for l in range(3)]
            # else:    # "+"일 때

