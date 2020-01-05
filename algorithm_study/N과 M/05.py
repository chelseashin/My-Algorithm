import sys
sys.stdin = open("input1.txt")

def dfs(depth):
    global N, M, A

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
order = []
visited = [0] * (N+1)
dfs(0)