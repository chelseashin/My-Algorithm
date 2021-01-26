import sys
input = sys.stdin.readline

A = input().strip()
for i in range(9, -1, -1):
    for j in A:
        if int(j) == i:
            print(i, end="")