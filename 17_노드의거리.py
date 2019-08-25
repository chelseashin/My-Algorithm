import sys
sys.stdin = open("17_input.txt")

T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    arr = [[0] * (V + 1) for _ in range(V + 1)]
    for e in range(E):
        start, end = map(int, input().split())
        arr[start][end] = 1
    S, G = map(int, input().split())
    print(arr)