import sys
sys.stdin = open('04_input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    # print(L)

    D = {i:L.count(i) for i in set(L)}