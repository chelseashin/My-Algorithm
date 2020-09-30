import sys
sys.stdin = open('17471_input.txt')
input = sys.stdin.readline
from collections import deque

# 올바른 구역 나누기인지 확인
def bfs(L):
    Q = deque([L[0]])
    check = [0] * N
    check[L[0]] = 1
    cnt = 1
    temp = 0
    while Q:
        s = Q.popleft()
        temp += population[s]
        for e in G[s]:
            if e in L and not check[e]:
                check[e] = 1
                Q.append(e)
                cnt += 1
    if len(L) == cnt:
        return temp
    return 0

# 가능한 모든 가짓 수
def comb(depth, k, goal):
    global result
    if depth == goal:
        # print(selected)

        a, b = [], []
        for n in range(N):
            if selected[n]:
                a.append(n)
            else:
                b.append(n)
        A = bfs(a)
        if not A:
            return
        B = bfs(b)
        if not B:
            return
        result = min(result, abs(A-B))
        return
    for i in range(k, N):
        selected[i] = 1
        comb(depth+1, i+1, goal)
        selected[i] = 0

# main
N = int(input())
population = list(map(int, input().split()))
G = [[] for _ in range(N)]

for i in range(N):
    for j in list(map(int, input().split()))[1:]:
        G[i].append(j-1)
# print(G)
result = float('inf')
selected = [0] * N
for g in range(1, N//2+1):
    comb(0, 0, g)

if result == float('inf'):
    print(-1)
else:
    print(result)