import sys
sys.stdin = open("23_input.txt")

import itertools
def perm(P):
    global N, result, new, arr, Min
    A = list(itertools.permutations(result, 2))
    B = list(itertools.permutations(new, 2))
    # print('A', A)
    # print('B', B)
    A_p, B_p = 0, 0
    for i in range(len(A)):
        A_p += arr[A[i][0]][A[i][1]] + arr[A[i][1]][A[i][0]]
        B_p += arr[B[i][0]][B[i][1]] + arr[B[i][1]][B[i][0]]
    if abs(A_p - B_p) < Min:
        Min = abs((A_p-B_p))
    return A_p, B_p, Min

def make(L):
    global arr, result, Min, N, new
    raw = [i for i in range(N)]
    new = []
    for r in raw:
        if r not in L:
            new.append(r)
    print(new)
    print(perm(N))
    print()

def dfs(depth, k):
    global arr, count
    if depth == N//2:
        print(result)
        make(result)
        # count += 1
        return
    for i in range(k, N):
        if visited[i] == 1:
            continue
        result.append(i)
        visited[i] = 1
        dfs(depth+1, k)
        result.pop()
        visited[i] = 0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * (N+1)
Min = float('inf')
result = []
count = 0
dfs(0, 0)
# print(count)
print(Min)
